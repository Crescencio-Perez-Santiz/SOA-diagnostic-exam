from typing import List, Optional
import uuid
from dataclasses import dataclass, field
from student.Domain.Entity.Contact import Contact

@dataclass
class Student:
    
    student: str = field(default_factory=uuid.uuid4, init=False)
    student_name: str
    enrolment: int
    contact: Contact
    tutor_uuid: Optional[str] = None
    subjects: Optional[List[str]] = None
    