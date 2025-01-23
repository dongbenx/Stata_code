gen 地区分组 = .

local east "北京 天津 河北 辽宁 上海 江苏 浙江 福建 山东 广东 海南"
local middle "山西 吉林 黑龙江 安徽 江西 河南 湖北 湖南"
local west "内蒙古 广西 重庆 四川 贵州 云南 西藏 陕西 甘肃 青海 宁夏 新疆"

foreach prov of local east {
    replace 地区分组 = 1 if 地区 == "`prov'"
}
foreach prov of local middle {
    replace 地区分组 = 2 if 地区 == "`prov'"
}
foreach prov of local west {
    replace 地区分组 = 3 if 地区 == "`prov'"
}


label define 地区lab 1 "东部" 2 "中部" 3 "西部"
label values 地区分组 地区lab


