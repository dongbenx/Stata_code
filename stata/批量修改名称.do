* 定义变量名
local varname " "

* 遍历所有变量并重命名
foreach var of local varname {
    rename `var' new`var'
}


