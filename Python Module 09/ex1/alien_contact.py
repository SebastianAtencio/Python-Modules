from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires"
                             "at least 3 witnesses")
        if self.signal_strength > 7.0:
            if not self.message_received or not self.message_received.strip():
                raise ValueError("Strong signals (> 7.0) should"
                                 "include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-15T14:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
    }

    try:
        contact = AlienContact(**valid_data)  # type: ignore
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except ValidationError as e:
        print(f"Unexpected validation error: {e}")

    print("========================================")
    invalid_data = {
        "contact_id": "_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": "telepathic",
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": None,
    }

    print("Expected validation error:")
    try:
        AlienContact(**invalid_data)  # type: ignore
    except ValidationError as e:
        for error in e.errors():
            mensaje = error["msg"]
            print(mensaje)


if __name__ == "__main__":
    main()
