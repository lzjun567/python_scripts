from PIL import Image, ImageDraw, ImageFont

LEFT_PART_VERTICAL_BLANK_MULTIPLY_FONT_HEIGHT = 2
LEFT_PART_HORIZONTAL_BLANK_MULTIPLY_FONT_WIDTH = 1 / 4
RIGHT_PART_VERTICAL_BLANK_MULTIPLY_FONT_HEIGHT = 1
RIGHT_PART_HORIZONTAL_BLANK_MULTIPLY_FONT_WIDTH = 1 / 4
RIGHT_PART_RADII = 10

BG_COLOR = '#000000'  # 黑色图片背景
BOX_COLOR = '#F7971D'  # 右侧背景颜色（黄）
LEFT_TEXT_COLOR = '#FFFFFF'  # 左侧文字颜色（白）
RIGHT_TEXT_COLOR = '#000000'  # 右侧文字颜色（黑）
FONT_SIZE = 50


def create_left_img(text):
    font = ImageFont.truetype('ArialEnUnicodeBold.ttf', FONT_SIZE)
    font_width, font_height = font.getsize(text)
    offset_y = font.font.getsize(text)[1][1]
    blank_height = font_height * 2
    right_blank = int(font_width / len(text) * 0.25)
    img_height = font_height + offset_y + blank_height * 2
    image_width = font_width + right_blank

    image_size = image_width, img_height
    image = Image.new('RGBA', image_size, BG_COLOR)
    draw = ImageDraw.Draw(image)
    draw.text((0, blank_height), text, fill=LEFT_TEXT_COLOR, font=font)
    image.save("left.png")
    return image


def create_right_img(text: str, font_size: int):
    radii = RIGHT_PART_RADII
    font = ImageFont.truetype('ArialEnUnicodeBold.ttf', font_size)
    font_width, font_height = font.getsize(text)
    offset_y = font.font.getsize(text)[1][1]
    blank_height = font_height
    left_blank = int(font_width / len(text) * 0.25)
    image_width = font_width + 2 * left_blank
    image_height = font_height + offset_y + blank_height * 2
    image = Image.new('RGBA', (image_width, image_height), BOX_COLOR)
    draw = ImageDraw.Draw(image)
    draw.text((left_blank, blank_height), text, fill=RIGHT_TEXT_COLOR, font=font)

    # 圆
    magnify_time = 10
    magnified_radii = radii * magnify_time
    circle = Image.new('L', (magnified_radii * 2, magnified_radii * 2), 0)  # 创建一个黑色背景的画布
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, magnified_radii * 2, magnified_radii * 2), fill=255)  # 画白色圆形

    # 画4个角（将整圆分离为4个部分）
    magnified_alpha_width = image_width * magnify_time
    magnified_alpha_height = image_height * magnify_time
    alpha = Image.new('L', (magnified_alpha_width, magnified_alpha_height), 255)
    alpha.paste(circle.crop((0, 0, magnified_radii, magnified_radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((magnified_radii, 0, magnified_radii * 2, magnified_radii)),
                (magnified_alpha_width - magnified_radii, 0))  # 右上角
    alpha.paste(circle.crop((magnified_radii, magnified_radii, magnified_radii * 2, magnified_radii * 2)),
                (magnified_alpha_width - magnified_radii, magnified_alpha_height - magnified_radii))  # 右下角
    alpha.paste(circle.crop((0, magnified_radii, magnified_radii, magnified_radii * 2)),
                (0, magnified_alpha_height - magnified_radii))  # 左下角
    alpha = alpha.resize((image_width, image_height), Image.ANTIALIAS)
    image.putalpha(alpha)
    image.save("right.png")
    return image


def create(left_text, right_text):
    left_img = create_left_img(left_text)
    right_img = create_right_img(right_text, FONT_SIZE)
    blank = 30
    bg_img_width = left_img.width + right_img.width + blank * 2
    bg_img_height = left_img.height
    bg_img = Image.new('RGBA', (bg_img_width, bg_img_height), BG_COLOR)
    bg_img.paste(left_img, (blank, 0))
    bg_img.paste(right_img, (blank + left_img.width, int((bg_img_height - right_img.height) / 2)), mask=right_img)
    bg_img.save(f'{left_text}{right_text}.png')


if __name__ == "__main__":
    create("Git", "Hub")
