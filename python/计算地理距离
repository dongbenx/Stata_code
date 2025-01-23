import numpy as np
import pandas as pd

# 地球半径 (单位: 千米)
R = 6371.0

# 城市坐标 (经度, 纬度)
cities = {
    '北京市': (116.39, 39.9),
    '天津市': (117.25, 39.1),
    '河北省': (114.48, 38.04),
    '山西省': (112.52, 37.83),
    '内蒙古自治区': (111.66, 40.82),
    '辽宁省': (123.41, 41.79),
    '吉林省': (125.31, 43.89),
    '黑龙江省': (126.64, 45.74),
    '上海市': (121.46, 31.23),
    '江苏省': (118.77, 32.04),
    '浙江省': (120.15, 30.26),
    '安徽省': (117.27, 31.86),
    '福建省': (119.29, 26.07),
    '江西省': (115.89, 28.67),
    '山东省': (117.00, 36.66),
    '河南省': (113.65, 34.75),
    '湖北省': (114.29, 30.56),
    '湖南省': (112.98, 28.20),
    '广东省': (113.26, 23.11),
    '广西壮族自治区': (108.31, 22.80),
    '海南省': (110.34, 20.03),
    '重庆市': (106.54, 29.55),
    '四川省': (104.08, 30.66),
    '贵州省': (106.71, 26.57),
    '云南省': (102.70, 25.04),
    '西藏自治区': (91.132, 29.65),
    '陕西省': (108.94, 34.26),
    '甘肃省': (103.75, 36.06),
    '青海省': (101.78, 36.60),
    '宁夏回族自治区': (106.27, 38.46),
    '新疆维吾尔自治区': (87.606, 43.79)
}

def haversine(lon1, lat1, lon2, lat2):
    """
    计算两点之间的地理距离
    """
    # 转换为弧度
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    # 经度差和纬度差
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Haversine公式
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    
    # 计算距离
    distance = R * c
    return distance

# 计算所有城市对的地理距离
results = []

for city1, (lon1, lat1) in cities.items():
    for city2, (lon2, lat2) in cities.items():
        distance = haversine(lon1, lat1, lon2, lat2)
        results.append((city1, city2, distance))

# 转换为 DataFrame
df = pd.DataFrame(results, columns=['城市1', '城市2', '距离 (公里)'])

# 导出到 Excel 文件
df.to_excel('城市距离计算结果.xlsx', index=False, engine='openpyxl')

print("已成功导出到 '城市距离计算结果.xlsx'")
