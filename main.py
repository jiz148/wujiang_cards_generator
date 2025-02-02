import pandas as pd

from wujiang_cards_generator_package import WujiangCardGeneratorService

wujiang_data: pd.DataFrame = pd.read_excel('武将规则.xlsx')

wujiang_cards_generator_service: WujiangCardGeneratorService = WujiangCardGeneratorService(
    wujiang_data=wujiang_data,
    save_path='generated_cards',
)

wujiang_cards_generator_service.save_to_cards()
