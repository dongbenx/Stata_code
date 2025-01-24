//权重矩阵生成

//安装命令spwmatrix
// ssc install spwmatrix

//安装命令spatwmat
//1.输入命令 findit spatwmat
//2.点击界面链接 "sg162 from http://www.stata.com/stb/stb60"
//3.找到INSTALLATION FILES,点击 "click here to install"

cd "C:\Users\Desktop"
use "C:\Users\Desktop\STATA代码\空间计量\30坐标.dta"

//导入经纬度坐标,lat纬度,lng经度,并重命名
  //纬度赋值x
  //经度赋值y

//1.1 基于距离的邻接权重矩阵wbin_1、wbin

*spatwmat
//band()为邻接参数,可手动调整,band(0 10)即距离band在0~10之间的单位视为邻接,赋权重1,否则赋权重0,下述db(0 10)同理
spatwmat, name(wbin_1) xcoord(x) ycoord(y) band(0 10) binary
matrix list wbin_1            //查看权重矩阵wbin_1
putexcel set wbin_1, replace  //将权重矩阵wbin_1导入excel文件中
putexcel A1 = matrix(wbin_1)  //从A1单元格导入

*spwmatrix
spwmatrix gecon x y, wn(wbin) wtype(bin) db(0 10) cart   //wtype()为权重矩阵类型,wtype(bin)为邻接权重矩阵,其他参数可参考 help spwmatrix
matrix list wbin
putexcel set wbin, replace
putexcel A1 = matrix(wbin)

*1.2 基于近邻数量的邻接权重矩阵wnear

*spmatrix_knn
//knn(10)即距离最近的10个单位赋权重1,其他赋权重0
spwmatrix gecon x y, wname(wnear) cart knn(10)
matrix list wnear
putexcel set wnear, replace
putexcel A1 = matrix(wnear)

*1.3 计算一阶反距离权重矩阵winv
spwmatrix gecon x y, wn(winv) wtype(inv) cart alpha(1)
matrix list winv
putexcel set winv, replace
putexcel A1 = matrix(winv)

*1.4 计算二阶反距离权重矩阵winv2
spwmatrix gecon x y, wn(winv2) wtype(inv) cart alpha(2)
matrix list winv2
putexcel set winv2, replace
putexcel A1 = matrix(winv2)

*1.5 计算经济地理权重矩阵wecon
//econvar(var)为所设定的经济变量,测量经济距离,此处设定的经济变量var为peo,即各地人口数量
spwmatrix gecon x y, wn(wecon) wtype(econ) econvar(peo)
matrix list wecon
putexcel set wecon, replace
putexcel A1 = matrix(wecon)

*1.6 计算反经济地理权重矩阵winvecon
//测量反经济距离
spwmatrix gecon x y, wn(winvecon) wtype(invecon) econvar(edu)
matrix list winvecon
putexcel set winvecon, replace
putexcel A1 = matrix(winvecon)

//之后打开当前目录下各自的.xls文件,将生成的权重矩阵导入.dta文件中即可
