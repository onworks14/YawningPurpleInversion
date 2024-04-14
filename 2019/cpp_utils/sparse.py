import os
import subprocess

def clone_specific_folder(repo_url, folder_path):
    """
    克隆指定的GitHub仓库中的特定文件夹。

    :param repo_url: 仓库的URL，例如：https://github.com/vss2sn/advent_of_code.git
    :param folder_path: 要克隆的文件夹路径，例如：2019/cpp
    """
    # 克隆仓库
    subprocess.run(["git", "clone", repo_url], check=True)
    
    # 获取仓库名称
    repo_name = repo_url.split('/')[-1].split('.')[0]
    
    # 进入仓库目录
    os.chdir(repo_name)
    
    # 启用sparse-checkout
    subprocess.run(["git", "config", "core.sparseCheckout", "true"], check=True)
    
    # 指定要检出的文件夹
    with open('.git/info/sparse-checkout', 'w') as f:
        f.write(f"{folder_path}/*\n")
    
    # 更新工作目录
    subprocess.run(["git", "read-tree", "-mu", "HEAD"], check=True)
    
    print(f"成功克隆了文件夹：{folder_path}。")

if __name__ == "__main__":
    # 提示用户输入仓库URL和文件夹路径
    repo_url = input("请输入仓库的URL：")
    folder_path = input("请输入要克隆的文件夹路径：")
    
    # 调用函数
    clone_specific_folder(repo_url, folder_path)