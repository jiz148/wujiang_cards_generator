from typing import (
    Union,
)

from pydantic import BaseModel

from ..constants import config_constants


class ConfigModel(BaseModel):

    card_height: int = config_constants.DEFAULT_CARD_HEIGHT
    card_weight: int = config_constants.DEFAULT_CARD_WIDTH

    title_font: str = config_constants.DEFAULT_TITLE_FONT
    info_font: str = config_constants.DEFAULT_INFO_FONT
    stats_font: str = config_constants.DEFAULT_STATS_FONT
    title_size: Union[int, float] = config_constants.DEFAULT_TITLE_SIZE
    info_size: Union[int, float] = config_constants.DEFAULT_INFO_SIZE
    stats_size: Union[int, float] = config_constants.DEFAULT_STATS_SIZE
