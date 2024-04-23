from fastapi import FastAPI, Request, HTTPException, Response
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware
from config.redis import redis_client
from datetime import timedelta, datetime
import time
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return "Welcome To The FastAPI Project!!"
app.include_router(router)

request_per_day = 50

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    user_id = request.headers.get("user_id")
    if not user_id:
        return Response("User ID is required in the headers.", status_code=400)

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    next_day = current_date + timedelta(days=1)
    next_day_timestamp = time.mktime(next_day.timetuple())

    redis_key = f"request_tracker:{user_id}:{current_date}"
    request_count = redis_client.get(redis_key)

    if request_count is None:
        redis_client.set(redis_key, 1, ex=int(next_day_timestamp - current_datetime.timestamp()))
        request_count = 1
    else:
        request_count = int(request_count)
        if request_count > request_per_day:
            return Response("Too many requests for the day.", status_code=429)
        redis_client.incr(redis_key)

    response = await call_next(request)
    response.headers["X-RateLimit-Remaining"] = str(request_per_day - request_count)
    return response

    