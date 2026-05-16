from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T10:30:00",
    }
    try:
        station = SpaceStation(**valid_data)  # type: ignore
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        if station.is_operational:
            status_str = "Operational"
        else:
            status_str = "Maintenance"
        print(f"Status: {status_str}")
    except ValidationError as e:
        print(f"Unexpected validation error: {e}")
    print()
    print("========================================")
    invalid_data = {
        "station_id": "ISS002",
        "name": "Overcrowded Station",
        "crew_size": 25,
        "power_level": 190.0,
        "oxygen_level": 195.0,
        "last_maintenance": "2024-01-16T12:00:00",
    }
    print("Expected validation error:")
    try:
        SpaceStation(**invalid_data)  # type: ignore
    except ValidationError as e:
        for error in e.errors():
            campo = error["loc"][0]
            mensaje = error["msg"]
            print(f"Error in the field '{campo}': {mensaje}")


if __name__ == "__main__":
    main()
