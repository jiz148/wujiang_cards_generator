"""
Wujiang
"""

from typing import Optional
import textwrap
from numbers import Number

from PIL import Image, ImageDraw, ImageFont

from ..utils.config_utils import get_config_model
from ..models.wujiang_model import WujiangModel
from ..models.config_model import ConfigModel
from ..utils.font_utils import load_font


class Wujiang:

    def __init__(
            self,
            wujiang_model: WujiangModel,
    ) -> None:
        self.level: int = wujiang_model.level
        self.role: str = wujiang_model.role
        self.type: str = wujiang_model.type
        self.race: str = wujiang_model.race
        self.item_bag: int = wujiang_model.item_bag
        self.name: str = wujiang_model.name
        self.attack: Number = wujiang_model.attack
        self.defense: Number = wujiang_model.defense
        self.speed: Number = wujiang_model.speed
        self.range: Number = wujiang_model.range
        self.mana: Number = wujiang_model.mana
        self.spells: Optional[str] = wujiang_model.spells
        self.properties: Optional[str] = wujiang_model.properties

    def to_game_card_image(self) -> Image:

        config: ConfigModel = get_config_model()

        card: Image = Image.new(
            mode="RGB",
            size=(config.card_weight, config.card_height),
            color=(0, 0, 0),
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
            outline="white",
            width=3,
        )

        title_text: str = f"{self.name} {self.level}"
        draw.text(
            xy=(margin+boarder_width, boarder_width),
            text=title_text,
            fill="white",
            font=font_title,
        )

        role_text: str = f"{self.role}  {self.race}  {self.type}"
        draw.text(
            xy=(margin+boarder_width, boarder_width + height_in_boarder * 0.05),
            text=role_text,
            fill="white",
            font=font_info,
        )

        stats_text: str = (f"攻 {self.attack}  守 {self.defense}  速 {self.speed}  "
                           f"范 {self.range}  魔 {self.mana} 槽位 {self.item_bag}")
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.15),
            text=stats_text,
            fill="white",
            font=font_stats,
        )

        spells_text: str = f"{self.spells if self.spells else ''}"
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.2),
            text="技能\n" + textwrap.fill(text=spells_text, width=int(config.card_weight / 20)),
            fill="white",
            font=font_info,
        )

        properties_text: str = f"{self.properties if self.properties else ''}"
        draw.text(
            xy=(margin+boarder_width, height_in_boarder * 0.7),
            text="特性\n" + textwrap.fill(text=properties_text, width=int(config.card_weight / 20)),
            fill="white",
            font=font_info,
        )

        return card


if __name__ == '__main__':
    wujiang_model: WujiangModel = WujiangModel(
        level=8,
        role='法师',
        type='暗',
        race='人类',
        item_bag=0,
        name='艾莉',
        attack=2,
        defense=2,
        speed=1,
        range=1,
        mana=5,
        spells='魔墙 吸魔【1魔力牵引（一回合最多使用一次；可以对对方或者己方使用，被击中单位向指定方向移动1-3格，若是对方单位，'
               '则下个回合不能移动）￥诅咒（将自己的血下降0.5，场上一单位每2回合血*1/2）￥美杜莎（攻3守无限范1，一回合一次瞬移，攻4次）'
               '￥实验（己方一单位全能力+2，6回合后死亡） ￥水晶球（8回合内可攻击和技能场上任何单位）',
        properties='使用结束过主动技能单位当回合无法对此单位造成伤害',
    )

    wujiang: Wujiang = Wujiang(wujiang_model)
    card_image: Image = wujiang.to_game_card_image()

    # card_image.save("wujiang_card.png")
    card_image.show()
