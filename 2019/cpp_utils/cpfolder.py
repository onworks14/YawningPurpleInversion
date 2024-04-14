import os
import shutil

def copy_and_rename_files(source_folder, target_folder):
    """
    将指定文件夹中的文本文件复制到新的文件夹，并重命名文件。

    :param source_folder: 源文件夹路径，例如：'input'
    :param target_folder: 目标文件夹路径，例如：'txt'
    """
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        # 检查文件是否以'input'结尾
        if filename.endswith('_input'):
            # 构造源文件路径
            source_file_path = os.path.join(source_folder, filename)
            # 构造目标文件路径，将文件名从'day_XX_input'改为'day_XX.txt'
            target_file_path = os.path.join(target_folder, filename.replace('_input', '.txt'))
            # 复制文件
            shutil.copy(source_file_path, target_file_path)
            print(f"复制并重命名了文件：{filename} -> {target_file_path}")

if __name__ == "__main__":
    # 提示用户输入源文件夹和目标文件夹路径
    source_folder = input("请输入源文件夹路径：")
    target_folder = input("请输入目标文件夹路径：")

    # 调用函数
    copy_and_rename_files(source_folder, target_folder)