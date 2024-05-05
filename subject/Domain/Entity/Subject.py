from dataclasses import dataclass, field
import uuid

@dataclass
class Subject:
    subject_uuid: str = field(default_factory=uuid.uuid4, init=False)
    subject_name: str