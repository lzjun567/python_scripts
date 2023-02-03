"""

注意：

1. 第一次运行时需要安装了python环境
2. 第一次运行时需要安装 pandas 包， 命令是： pip install pandas
3. 将要待合并的excel文件（如果是压缩包请先解压）放在和本脚本同级目录下的data文件夹中（没有data文件夹就创建个新的）
4. 打开cmd命令行，切换到本脚本所在目录，开始执行   python excel_merge.py
5. 观察输出的提示内容， 等待合并结果

"""


import os


import datetime
import pandas as pd

cwd = os.path.abspath('data')
files = os.listdir(cwd)

print("一共有" + str(len(files)) + "个文件待合并")
df = pd.DataFrame()
print("开始合并。。。。。")
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel("data/" + file), ignore_index=True)
df.head()

now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
new_name = f"合并文件_{now}.xlsx"

df.to_excel(new_name)
print(f"合并完成，生成文件:{new_name}")
