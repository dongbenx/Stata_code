// 设置面板数据 id是省份 year年份
xtset id year

// 定义要遍历的变量名
local varlist 

// 遍历指定的变量名
foreach var of local varlist {

  // 计算变量的样本量 
  count if !missing(`var')

  // 如果样本量小于12
  if `r(N)' < 12 {
    
    // 进行线性插值
    by id: ipolate `var' year, gen(n_`var') epolate
    
    // 删除原始变量
    drop `var'
    
    // 重命名插值变量
    rename n_`var' `var'
  }
}
