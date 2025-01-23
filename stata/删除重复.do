* 按id和year排序，并在每组内排序
bysort id year: gen dup = _n == 1

* 删除重复的记录
drop if dup == 0

* 删除辅助变量
drop dup
