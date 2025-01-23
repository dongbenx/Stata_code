* 按 id 分组，按 year 排序，计算累乘
by id: gen cumulative_de = .
by id: replace cumulative_de = de if _n == 1
by id: replace cumulative_de = cumulative_de[_n-1] * de if _n > 1
