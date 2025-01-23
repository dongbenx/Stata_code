import pandas as pd

# 定义省份列表
provinces = [
    "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽",
    "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
    "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆"
]

# 定义年份范围
years = list(range(2011, 2022+1))

# 创建面板数据
data = {
    "地区": [province for province in provinces for _ in years],
    "时间": years * len(provinces)
}

df = pd.DataFrame(data)

# 显示生成的数据
print(df)

# 将文件保存到当前工作目录
df.to_excel("./panel_data.xlsx")
