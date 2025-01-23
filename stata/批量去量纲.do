xtset id year
local varlist 
*************归一化***********
foreach var of local varlist {
	qui sum `var'
g nor_`var'=(`var'-r(min))/(r(max)-r(min))
}



xtset id year
local varlist 
***********标准化************
foreach var of local varlist {
	qui sum `var'
g std_`var'=(`var'-r(mean))/r(sd)
}




xtset id year
local varlist 
***********取对数************
foreach var of local varlist {
	qui sum `var'
g ln_`var'=ln(`var')
}
