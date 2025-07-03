import os
print("当前工作目录:", os.getcwd())  # 输出程序运行时的工作目录

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 切换到代码文件所在目录
# __file__ 获取当前文件的路径（如 script.py）。
# os.path.abspath 转为绝对路径（避免相对路径问题）。
# os.path.dirname 提取目录部分。
print("当前工作目录:", os.getcwd())  # 输出程序运行时的工作目录