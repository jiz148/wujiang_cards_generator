"""
Wujiang Loader
"""
from typing import (
    List,
    Optional,
)

import pandas as pd
from pandas import DataFrame

from ..constants import wujiang_constants
from ..models.wujiang_model import WujiangModel


class WujiangLoader:
    
    def __init__(
            self,
            wujiang_data: DataFrame,
    ):
        self.wujiang_data: DataFrame = wujiang_data
        
        self.wujiangs: List[WujiangModel] = []
        
        self._load_wujiang()
        pass
    
    def _load_wujiang(self):
        for _, row in self.wujiang_data.iterrows():
            spells: Optional[str] = \
                None if pd.isna(row[wujiang_constants.SPELLS_COL]) else row[wujiang_constants.SPELLS_COL]
            properties: Optional[str] = \
                None if pd.isna(row[wujiang_constants.PROPERTIES_COL]) else row[wujiang_constants.PROPERTIES_COL]
            wujiang_model: WujiangModel = WujiangModel(
                level=row[wujiang_constants.LEVEL_COL],
                role=row[wujiang_constants.ROLE_COL],
                type=row[wujiang_constants.TYPE_COL],
                race=row[wujiang_constants.RACE_COL],
                name=row[wujiang_constants.NAME_COL],
                attack=row[wujiang_constants.ATTACK_COL],
                defense=row[wujiang_constants.DEFENSE_COL],
                speed=row[wujiang_constants.SPEED_COL],
                range=row[wujiang_constants.RANGE_COL],
                mana=row[wujiang_constants.MANA_COL],
                spells=spells,
                properties=properties,
            )
            self.wujiangs.append(wujiang_model)

    def get_wujiangs(self) -> List[WujiangModel]:
        return self.wujiangs
