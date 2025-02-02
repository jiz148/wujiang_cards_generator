"""
Wujiang Model
"""
from typing import (
    Optional,
    Union,
)


from pydantic import BaseModel


class WujiangModel(BaseModel):

    level: int
    role: str
    type: str
    race: str
    item_bag: int
    name: str
    attack: Union[int, float]
    defense: Union[int, float]
    speed: Union[int, float]
    range: Union[int, float]
    mana: Union[int, float]
    spells: Optional[str]
    properties: Optional[str]
