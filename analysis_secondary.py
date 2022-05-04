# -*- coding: utf-8 -*-                                                       
# @Time       :   2022/5/2 23:06
import pandas as pd
import numpy as np
import os
from pathlib import Path
import time

file_path = r'D:\pycharm_community\IntelligenceProject\csvFile'
p = Path(file_path)
# 所有以xlsx结尾的文件
csv_list = []  # 文件列表
name_list = []  # 商品名称列表
csv_info = []  # csv信息列表
df_array = []  # 统计数据列表
for file in p.rglob('*.csv'):
    csv_list.append(file)
    f = open(file, 'r', encoding='GB18030')
    data_ = pd.read_csv(f)
    csv_info.append(data_)
    df_array.append(data_.describe())

for _ in range(len(df_array)):
    print("====================")
    print(str(csv_list[_]).split('\\')[4][0:-4].split('_')[1])
    name_list.append(str(csv_list[_]).split('\\')[4][0:-4].split('_')[1])
    print(df_array[_])

print("====================")

for _ in range(len(df_array)):
    # df_array[_].to_excel(excel_writer=r"D:\pycharm_community\IntelligenceProject\csvFile\analysis_all.xlsx",
    #                      encoding="GB18030")
    print(str(csv_list[_]).split('\\')[4][0:-4].split('_')[1])
    var = csv_info[_].loc[1, 'changPriceRemark_趋势变动']
    print(var)
# df_array[0].to_excel(excel_writer=r"D:\pycharm_community\IntelligenceProject\csvFile\analysis_all.xlsx",
#                      encoding="GB18030")
