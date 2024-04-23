from redis import Redis
from dotenv import load_dotenv
load_dotenv()
import os

redis_port = os.getenv("REDIS_PORT")

redis_client = Redis("localhost", redis_port, db=0)


