import glob
from moviepy.editor import *
import cv2
from PIL import Image


def convert_mp4_to_jpgs(input_file):
    # 先将mp4文件的所有帧读取出保存为图片
    video_capture = cv2.VideoCapture(input_file)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"output/frame_{frame_count:03d}.jpg", image)
        # read next image
        still_reading, image = video_capture.read()
        frame_count += 1


def convert_images_to_gif(output_file):
    # 读取目录下图片，用Pillow模块的Image和所有图片合并
    # 成一张gif
    images = glob.glob(f"output/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frame_one = frames[0]
    frame_one.save(output_file, format="GIF", append_images=[f for i, f in enumerate(frames[1:]) if i % 2 == 0],
                   save_all=True, duration=40, loop=0)


def convert_mp4_to_gif(input_file, output_file):
    convert_mp4_to_jpgs(input_file)
    convert_images_to_gif(output_file)


def mp4_to_gif2():

    clip = VideoFileClip("demo.mp4")
    clip.write_gif("output2.gif")


if __name__ == "__main__":
    mp4_to_gif2()
    # convert_mp4_to_gif("demo.mp4", "output2.gif")


def convert_gif_to_mp4():
    import moviepy.editor as mp
    clip = mp.VideoFileClip("demo.gif")
    clip.write_videofile("output.mp4")
