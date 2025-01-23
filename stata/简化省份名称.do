g 省份 = 地区
replace 省份 = subinstr(省份, "市", "", .)
replace 省份 = subinstr(省份, "省", "", .)
replace 省份 = subinstr(省份, "自治区", "", .)
replace 省份 = subinstr(省份, "壮族", "", .)
replace 省份 = subinstr(省份, "回族", "", .)
replace 省份 = subinstr(省份, "维吾尔", "", .)


