from typing import List, Optional
from dataclasses import dataclass, field
import uuid

@dataclass
class Tutor:
    tutor_uuid: str = field(default_factory=uuid.uuid4, init=False)
    tutor_name: str
    students: Optional[List[int]] = field(default_factory=list)