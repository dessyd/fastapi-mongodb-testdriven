from fastapi import APIRouter, Body, Response, status, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List

from ..database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from ..models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter(
    prefix="/students",
    tags=['Students']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_description="Student added")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return new_student

@router.get("/", response_model=List[StudentSchema], response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    print(students)
    return students


@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Student with id: {id} is unknown")
    return student

@router.put("/{id}")
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )

@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)

    if not deleted_student:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Student with id: {id} is unknown")

    return ResponseModel(
        "Student with ID: {} removed".format(id), "Student deleted successfully")
