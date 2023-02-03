from PIL import Image

"""
注意：
1、运行前请确保安装了python3环境
2、请先安装PIL库，命令是： pip install PIL
3、遇到任何问题可通过关注公众号【Python之禅】获得作者的帮助
"""


def main():
    avatar = Image.open("header.jpg")  # 加载头像
    flag = Image.open("国旗.png")  # 加载国旗

    width = min(flag.size)  # 取长宽比较小的那个
    flag = flag.crop((0, 0, width, width))  # 裁剪图片成正方形
    avatar_width, avatar_height = avatar.size  # 获取头像宽高
    flag = flag.resize(avatar.size)  # 将国旗缩放成头像大小比例

    weight = 2  # 透明度

    for w in range(avatar_width):
        for h in range(avatar_height):
            rgba = flag.getpixel((w, h))
            alpha = 255 - w // weight
            if alpha < 0:
                alpha = 0
            new_rgba = rgba[:-1] + (alpha,)
            flag.putpixel((w, h), new_rgba)

    avatar.paste(flag, (0, 0), mask=flag)
    avatar.show()
    avatar.save("new_avatar1.jpg")  # 保存新头像


if __name__ == '__main__':
    main()
