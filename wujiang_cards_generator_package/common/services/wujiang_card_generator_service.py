"""
Wujiang Card Generator Service
"""
import os

from typing import (
    List,
)

from pandas import DataFrame

from ..models.wujiang_model import WujiangModel
from ..loaders.wujiang_loader import WujiangLoader


class WujiangCardGeneratorService:

    def __init__(
            self,
            wujiang_data: DataFrame,
            save_path: str = 'generated_cards/',
    ):
        self.save_path: str = save_path
        wujiang_loader: WujiangLoader = WujiangLoader(
            wujiang_data=wujiang_data,
        )
        self.wujiangs: List[WujiangModel] = wujiang_loader.get_wujiangs()

    def save_to_cards(
            self,
    ):
        for wujiang in self.wujiangs:
            wujiang.to_game_card_image().save(
                os.path.join(self.save_path, f"01x card {wujiang.name.strip('*')}.png")
            )
        pass
