from PIL import Image

"""
注意：
1、运行前请确保安装了python3环境
2、请先安装PIL库，命令是： pip install PIL
3、遇到任何问题可通过关注公众号【Python之禅】获得作者的帮助
"""


def main():
    avatar = Image.open("header.jpg")  # 加载头像
    flag = Image.open("flag.jpg")  # 加载国旗
    avatar_width, avatar_height = avatar.size  # 获取头像宽高
    flag_size = (int(avatar_width / 3), int(avatar_height / 3))
    flag = flag.resize(flag_size, Image.ANTIALIAS)  # 将国旗大小缩放到头像的 1/9
    avatar.paste(flag, (avatar_width - flag_size[0], avatar_height - flag_size[1]))  # 放置在头像右下角
    avatar.show()
    avatar.save("new_avatar.jpg")  # 保存新头像


if __name__ == '__main__':
    main()
