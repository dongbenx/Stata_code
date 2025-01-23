* Step 2: 设置面板数据结构
xtset id year

* Step 3: 计算每个城市的观测次数
bysort id: gen city_count = _N

* Step 4: 删除不满足条件（每个城市应该有13个年份数据）的城市组
drop if city_count != 13

* Step 5: 查看数据是否删除正确
list id year , sepby(id)
