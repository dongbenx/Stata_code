
// 按城市求变量平均值
egen avg_tax = mean(  ), by(id year)


* 生成唯一标识符
egen unique_id = group(id year)

* 去重，只保留每组的第一条记录
bysort unique_id: keep if _n == 1

* 删除唯一标识符
drop unique_id
