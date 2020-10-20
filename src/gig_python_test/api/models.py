from datetime import datetime, date
from enum import Enum
from typing import Tuple, List, Optional

from pydantic import BaseModel


class CharacterStatus(str, Enum):
    DEAD = 'DEAD'
    ALIVE = 'ALIVE'


class Character(BaseModel):
    name: str
    birthday: date
    occupation: Optional[List[str]]
    img: Optional[str]
    status: CharacterStatus
    nickname: Optional[str]
    appearance: Optional[List[str]]
    portrayed: Optional[str]
    category: Optional[List[str]]

    class Config:
        use_enum_values = True


class Location(BaseModel):
    timestamp: datetime
    coordinates: Tuple[float, float]

    class Config:
        use_enum_values = True
