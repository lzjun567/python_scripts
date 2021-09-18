import os.path

import pygame as pg


def load_img(name):
    try:
        data_dir = os.path.join(os.path.dirname(__file__), "images")
        fullname = os.path.join(data_dir, name)
        image = pg.image.load(fullname)
    except pg.error:
        print("Cannot load image:", name)
        exit()
    image = image.convert()
    return image, image.get_rect()


class Fist(pg.sprite.Sprite):
    """

    """

    def __init__(self):
        super(Fist, self).__init__()
        self.image, self.rect = load_img("d1.png")
        print(self.rect)
        print(pg.display.get_surface().get_height()/2)


def main():
    pg.init()
    screen = pg.display.set_mode([500, 120])
    pg.display.set_caption("hell oworld")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    if pg.font:
        # 设置文本
        font = pg.font.Font(None, 30)
        text = font.render("hello world", True, (0, 0, 0))
        background.blit(text, ((background.get_width() - text.get_width()) / 2, 0))

    screen.blit(background, (0, 0))
    pg.display.flip()

    color = pg.time.Clock()
    fist = Fist()
    groups = pg.sprite.Group((fist,))

    going = True
    while going:
        color.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            pass
        groups.update()

        screen.blit(background, (0, 0))
        groups.draw(screen)
        pg.display.update()


if __name__ == '__main__':
    main()
