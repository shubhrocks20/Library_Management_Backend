from dataclasses import Field
from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: str | None = None
    age: str | None = None
    address: Address | None = None