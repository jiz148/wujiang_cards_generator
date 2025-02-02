from PIL import ImageFont


def load_font(
        font_name: str,
        font_size: int
) -> ImageFont.FreeTypeFont:
    try:
        font_path: str = font_name
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        raise Exception(f"Font {font_name} could not be loaded.")
