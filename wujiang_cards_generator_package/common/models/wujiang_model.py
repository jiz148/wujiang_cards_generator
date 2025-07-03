"""
Wujiang Model
"""
from typing import (
    Optional,
    Union,
)
import textwrap

from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont

from ..utils.config_utils import get_config_model
from ..models.config_model import ConfigModel
from ..utils.font_utils import load_font


class WujiangModel(BaseModel):

    level: int
    role: str
    type: str
    race: str
    name: str
    attack: Union[int, float]
    defense: Union[int, float]
    speed: Union[int, float]
    range: Union[int, float]
    mana: Union[int, float]
    spells: Optional[str]
    properties: Optional[str]

    def to_game_card_image(self) -> Image:

        config: ConfigModel = get_config_model()

        card: Image = Image.new(
            mode="RGB",
            size=(config.card_weight, config.card_height),
            color=(225, 112, 0),
        )
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(im=card)

        font_title: ImageFont.FreeTypeFont = load_font(
            font_name=config.title_font,
            font_size=config.title_size,
        )
        font_info: ImageFont.FreeTypeFont = load_font(
            font_name=config.info_font,
            font_size=config.info_size,
        )
        font_stats: ImageFont.FreeTypeFont = load_font(
            font_name=config.stats_font,
            font_size=config.stats_size,
        )

        boarder_width: int = 10
        margin: int = 5
        height_in_boarder: int = config.card_height - boarder_width * 2

        draw.rectangle(
            xy=[boarder_width, boarder_width, config.card_weight - boarder_width, config.card_height - boarder_width],
            outline="black",
            width=3,
        )

        title_text: str = f"{self.name} {self.level}"
        draw.text(
            xy=(margin+boarder_width, boarder_width),
            text=title_text,
            fill="black",
            font=font_title,
        )

        role_text: str = f"{self.role}  {self.race}  {self.type}"
        draw.text(
            xy=(margin+boarder_width, boarder_width + height_in_boarder * 0.05),
            text=role_text,
            fill="black",
            font=font_info,
        )

        stats_text: str = (f"攻 {self.attack}  守 {self.defense}  速 {self.speed}  "
                           f"范 {self.range}  魔 {self.mana}")
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.15),
            text=stats_text,
            fill="black",
            font=font_stats,
        )

        spells_text: str = f"{self.spells if self.spells else ''}"
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.2),
            text="技能\n" + textwrap.fill(text=spells_text, width=int(config.card_weight / 20)),
            fill="black",
            font=font_info,
        )

        properties_text: str = f"{self.properties if self.properties else ''}"
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.7),
            text="特性\n" + textwrap.fill(text=properties_text, width=int(config.card_weight / 20)),
            fill="black",
            font=font_info,
        )

        return card
