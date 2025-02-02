import os

from dotenv import load_dotenv

from ..models.config_model import ConfigModel
from ..constants import env_constants


def get_config_model() -> ConfigModel:
    load_dotenv()
    config_model: ConfigModel = ConfigModel(
        card_height=int(os.getenv(env_constants.CARD_HEIGHT, None)),
        card_weight=int(os.getenv(env_constants.CARD_WIDTH, None)),
        title_font=str(os.getenv(env_constants.TITLE_FONT, None)),
        info_font=str(os.getenv(env_constants.INFO_FONT, None)),
        stats_font=str(os.getenv(env_constants.STATS_FONT, None)),
        title_size=int(os.getenv(env_constants.TITLE_SIZE, None)),
        info_size=int(os.getenv(env_constants.INFO_SIZE, None)),
        stats_size=int(os.getenv(env_constants.STATS_SIZE, None)),
    )
    return config_model
