* 标记包含 "ST" 或 "*ST" 的记录
gen byte to_delete = strpos(公司名称, "ST") > 0

* 删除标记的记录
drop if to_delete

* 清理临时变量
drop to_delete
