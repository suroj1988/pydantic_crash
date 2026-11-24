from pydantic import BaseModel,Field,EmailStr,AnyUrl
from typing import Annotated,List,Dict,Optional


class Student(BaseModel):
    name: Annotated[str,Field(max_length=10,title="name of patient",examples=["Suroj","Kesab"])]
    age:Annotated[int,Field(gt = 0,lt=120,strict=True)]
    email:EmailStr
    url:AnyUrl
    married: Annotated[Optional[bool],Field(default=None)]
    allergies:List[str]
    contact_details:Dict[str,str]

def create_student(student:Student):
    print(student.name)
    print(student.age)
    print(student.married)
    print(student.allergies)

student_info = {"name":"Suroj","age":32,"email":"abc@gmail.com","url":"http://linkedin.com",
                "allergies":["cold","dust"],"contact_details":{"phone":"98760"}}

student1 = Student(**student_info)
create_student(student1)

