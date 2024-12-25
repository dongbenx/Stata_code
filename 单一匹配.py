import pandas as pd

# 文件路径
std_file_path = '/Users/zhuyenan/Downloads/master.xlsx'
data_file_path = '/Users/zhuyenan/Downloads/上市企业数实融合.xlsx'  # 确保文件扩展名正确
output_file_path = '/Users/zhuyenan/Downloads/merged_file2.xlsx'

# 读取Excel文件
std_df = pd.read_excel(std_file_path)
data_df = pd.read_excel(data_file_path)

# 合并DataFrame
df_main = std_df.merge(data_df, on=['地区', '时间'], how='left')

# 保存合并后的结果
df_main.to_excel(output_file_path, index=False, engine='openpyxl')
