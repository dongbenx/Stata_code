import os
import pandas as pd

# 文件路径
file_main = '/Users/zhuyenan/Downloads/面板.xlsx'  # 主文件路径
data_folder = '/Users/zhuyenan/Downloads/数据'  # 数据文件夹路径

# 读取主文件
df_main = pd.read_excel(file_main)

# 遍历数据文件夹中的每个文件
for filename in os.listdir(data_folder):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(data_folder, filename)
        
        # 读取数据文件
        df_data = pd.read_excel(file_path)
        
        # 删除倒数4行
        df_data = df_data.iloc[:-4]
        
        # 获取第二个指标值作为数值列的标题
        num_col_title = df_data.iloc[0, 0]
        
        # 删除指标列
        df_data.drop(columns=['指标'], inplace=True)

        # 删除分类列
        df_data.drop(columns=['分类'], inplace=True)
        
        # 重命名数值列
        df_data.rename(columns={'数值': num_col_title}, inplace=True)
        
        # 使用merge函数将两个DataFrame合并
        df_main = pd.merge(df_main, df_data, on=['地区', '时间'], how='left')

# 将最终结果保存到新的Excel文件
output_file = '/Users/zhuyenan/Downloads/merged_file.xlsx'
df_main.to_excel(output_file, index=False, engine='openpyxl')

print(f"All merged data saved to {output_file}")
