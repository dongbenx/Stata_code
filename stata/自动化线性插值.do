// 设置面板数据 id是省份 year年份
xtset id year

// 定义要遍历的变量名
local varlist  // 替换为您的变量名列表

// 遍历指定的变量名
foreach var of local varlist {

  // 计算变量的样本量 
  count if !missing(`var')

  // 如果样本量小于3597
  if `r(N)' < 372 {
    
    // 进行线性插值
    by id: ipolate `var' year, gen(n_`var') epolate
    
  }
  
}
