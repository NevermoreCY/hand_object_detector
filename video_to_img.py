import os
import subprocess
from pathlib import Path


def extract_frames(video_path, output_folder):
    """
    使用FFmpeg从视频文件中提取图像帧，并保存到指定的输出文件夹。

    :param video_path: 视频文件路径
    :param output_folder: 输出文件夹路径
    """
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # FFmpeg命令 -i 表示输入文件，%04d.jpg 表示输出文件命名格式，每秒提取一帧
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', 'fps=25',  # 每秒抽取一帧
        os.path.join(output_folder, '%04d.jpg')
    ]

    # 调用FFmpeg
    subprocess.run(command, check=True)

def process_videos_in_directory(directory,out_dir):
    """
    遍历指定目录下的所有视频文件，并为每个视频调用extract_frames函数。

    :param directory: 包含视频文件的目录
    """
    # 获取目录下的所有文件
    for video_file in Path(directory).iterdir():
        if video_file.is_file() and video_file.suffix in ['.mp4', '.avi', '.mkv', '.mov']:
            # 创建与视频同名的文件夹
            video_name = video_file.stem
            output_folder = os.path.join(out_dir, video_name)

            print(f"处理视频: {video_file.name} -> 目标文件夹: {output_folder}")
            extract_frames(str(video_file), output_folder)

if __name__ == "__main__":
    # 指定包含视频的文件夹
    video_directory = '2024_11_06/bili_good'
    out_dir = '2024_11_06/bili_good_img'

    # 处理该文件夹下的所有视频
    process_videos_in_directory(video_directory, out_dir)