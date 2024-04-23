from bson import ObjectId
from fastapi import APIRouter, HTTPException, Header, Request
from fastapi.encoders import jsonable_encoder
from config.database import collection_name
from models.students import Student, UpdateStudent
from schemas.schema import list_students, student_helper, singleStudent
router = APIRouter()

@router.post("/students", status_code=201)
async def create_students(student: Student):
    
    student = jsonable_encoder(student)
    inserted_student = collection_name.insert_one(dict(student))
    return {"id": str(inserted_student.inserted_id)}

# Fetch all Students
@router.get("/students")
async def get_students(country: str | None = None, age: int | None = None):
    query = {}
    if country:
        query['address.country'] = country
    if age:
        query['age'] = {'$gte': age}
    students =  list_students(collection_name.find(query))
    return {"data": students}

# Fetch Single Student
@router.get("/students/{id}")
async def get_single_student(id: str):
    student = collection_name.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found!")
    student = singleStudent(student)
    return student

@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudent):
    student_data = {k: v for k, v in student.dict().items() if v is not None}
    if len(student_data) < 1:
        raise HTTPException(status_code=400, detail="No valid fields provided for update")
    try:
        result = collection_name.update_one({"_id": ObjectId(id)}, {"$set": student_data})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/students/{id}", status_code=200)
async def delete_student(id: str):
    result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    # print(result)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}



    


    

    

