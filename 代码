# -*- coding = utf-8 -*-
# @Time : 2023/11/21 11:14

from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def save_data_to_excel(df, output_path):
    df.to_excel(output_path, index=False)
    print(f'数据已保存到 {output_path}')


# 固定的爬虫链接部分
base_url = "https://data.cnki.net/valueSearch/index?ky="
# 用户输入需要补充到链接中的信息
additional_info = input("爬取指标: ")
# 构建完整的URL
url = f"{base_url}{additional_info}"

# 用户输入需要点击的子节点文本信息
target_text = input("筛选条件: ")

# 城市列表
cities = [
    # '七台河', '三明', '三门峡', '上饶', '东营', '中山', '临沂', '丽水',
    #  '乌鲁木齐', '九江', '亳州', '佛山', '保定', '保山', '信阳', '六安',
    #  '兰州', '北京', '北海', '十堰', '南京', '南充', '南宁', '南平', '南昌',
    #  '南通', '南阳', '厦门', '双鸭山', '台州', '合肥', '吉安', '吉林',
    #  '周口', '咸宁', '咸阳', '哈尔滨', '唐山', '商丘', '商洛', '嘉兴',
    #  '四平', '大同', '大庆', '威海', '娄底', '孝感', '宁德', '安庆',
    #  '安康', '安阳', '安顺', '定西', '宜昌', '宜春', '宝鸡', '宣城',
    #  '宿州', '岳阳', '崇左', '常德', '平顶山', '广州', '庆阳', '廊坊',
    #  '延安', '开封', '张家口', '徐州', '德州', '怀化', '惠州', '成都',
    #  '承德', '抚州', '新乡', '新余', '无锡', '日照', '昆明', '晋中',
    #  '景德镇', '曲靖', '朔州', '朝阳', '来宾', '杭州', '松原', '枣庄',
    #  '株洲', '桂林', '梅州', '梧州', '榆林', '武威', '武汉', '永州',
    #  '汉中', '汕头', '汕尾', '江门', '池州', '沧州', '河源', '泉州',
    #  '泰安', '泰州', '洛阳', '济南', '济宁', '海口', '淄博', '淮北',
    #  '淮南', '清远', '湖州', '湘潭', '湛江', '滁州', '滨州', '漯河',
    #  '漳州', '潍坊', '潮州', '濮阳', '烟台', '焦作', '牡丹江', '玉林',
    #  '玉溪', '珠海', '白城', '白山', '百色', '益阳', '石家庄', '福州',
    #  '秦皇岛', '绥化', '聊城', '舟山', '芜湖', '茂名', '荆州', '荆门',
    #  '莆田', '菏泽', '萍乡', '蚌埠', '衡水', '衡阳', '衢州', '西宁',
    #  '西安', '许昌', '贵港', '贵阳', '赣州', '辽源', '运城', '通辽',
    #  '遂宁', '遵义', '邢台', '邯郸', '邵阳', '郑州', '郴州', '鄂州',
    #  '酒泉', '金华', '金昌', '钦州', '铜川', '铜陵', '银川',
    '镇江',
     '长春', '长沙', '长治', '阜阳', '防城港', '阳泉', '随州', '青岛',
     '韶关', '马鞍山', '驻马店', '鸡西', '鹤壁', '鹰潭', '黄冈', '黄山',
     '黑河', '齐齐哈尔', '龙岩'
]

# 创建Chrome WebDriver
driver = webdriver.Chrome(r'/Users/zhuyenan/PycharmProjects/pythonProject/知网/chromedriver')

# 访问指定的URL
driver.get(url)

# 切换窗口，在单个测试用例中打开多个窗口并在它们之间切换
driver.switch_to.window(driver.window_handles[-1])
sleep(2)

# 设置全局隐式等待时间
driver.implicitly_wait(3)

# 模糊、精确选择
model = driver.find_element(By.XPATH,
                            '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/div')
model.click()
model_select = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/ul')
model_confirm = model_select.find_element(By.XPATH, "//li/a[text()='精确']").click()

# 起始年份
start = driver.find_element(By.XPATH,
                            '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[1]/div')
start.click()

start_select = driver.find_element(By.CSS_SELECTOR, '#root > div.container > div.main.valueSearch_main__8GdKu > div '
                                                    '> div.valueSearch_left__3y_VZ > div.valueSearch_search-header__3JBKW '
                                                    '> div.valueSearch_nj-year__20S9j > div:nth-child(2) > div')
start_year = start_select.find_element(By.XPATH, "//li/a[text()='2011']").click()

driver.execute_script("var q=document.documentElement.scrollTop=0")
sleep(2)
# 终止年份
end = driver.find_element(By.XPATH,
                          '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[2]/div')
end.click()

end_select = driver.find_element(By.CSS_SELECTOR,
                                 '#root > div.container > div.main.valueSearch_main__8GdKu > div '
                                 '> div.valueSearch_left__3y_VZ > div.valueSearch_search-header__3JBKW '
                                 '> div.valueSearch_nj-year__20S9j > div:nth-child(4) > div')
# 74==2021年
end_year = end_select.find_element(By.XPATH,
                                   '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[2]/ul/li[74]').click()

# 找到包含 "50" 字符的子节点并点击
content_number = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[2]/span/span[3]')
content_number.click()
sleep(3)


def get_info():
    df_all = pd.DataFrame()  # 创建一个空的DataFrame，储存每一页的内容

    try:
        # 向下滑动
        driver.execute_script("window.scrollBy(0, 300);")

        # # 点击统计年鉴
        # resources = driver.find_element(By.CSS_SELECTOR,
        #                                 '#root > div.container > div.main.valueSearch_main__8GdKu'
        #                                 ' > div > div.valueSearch_right__3Ik2F > div:nth-child(3)'
        #                                 ' > div > span')

        # # 点击指标
        resources = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div[2]/div[4]/div')

        resources.click()
        sleep(2)
        try:

            # # 统计年鉴选择
            # resource = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/div[3]/ul')

            # 指标选择
            resource = driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div[2]/div[1]/div/div[2]/div[4]/ul')

            lis = resource.find_elements_by_tag_name("li")
            found = False  # 标记是否找到符合条件的元素
            # 循环遍历子节点
            min_len = float('inf')  # 初始化最小长度为正无穷
            min_li = None  # 初始化最小长度的节点为None

            # 循环遍历子节点
            for li in lis:
                # 判断子节点文本
                if target_text in li.text:
                    # 获取子节点文本长度
                    li_len = len(li.text)
                    # 判断是否为最小长度的节点
                    if li_len < min_len:
                        min_len = li_len
                        min_li = li
            # 如果找到符合条件的元素
            if min_li:
                # 点击最小长度的节点
                min_li.click()
                sleep(2)
                found = True

            if not found:
                for li in lis:
                    li_text = li.text
                    if ',' in li_text:
                        left_part, right_part = li_text.split(',', 1)  # 分割成左右两部分，只分割一次
                        if target_text == right_part.strip():
                            # 点击与预定词匹配的 li 元素
                            li.click()
                            sleep(2)
                            break  # 在点击了匹配的 li 元素后停止迭代


        except:
            pass
    except:
        pass

    while True:
        try:

            sleep(2)
            # 等待表格加载完成
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody.valueSearch_s-tab-tbody__1QPXw')))
            # 使用BeautifulSoup解析网页
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # 找到<tbody>标签的class为"valueSearch_s-tab-tbody__b5cry"的节点
            tbody = soup.find('tbody', class_='valueSearch_s-tab-tbody__1QPXw')

            # 将每个<tr>标签转换为一行数据，存储到DataFrame中
            rows = []
            for tr in tbody.find_all('tr'):
                tds = tr.find_all('td')
                try:
                    row = {
                        '序号': tds[0].get_text(),
                        '时间': tds[1].get_text(),
                        '地区': tds[2].get_text(),
                        '指标': tds[3].get_text(),
                        '数值': tds[4].get_text(),
                        '单位': tds[5].get_text(),
                        '来源': tds[6].get_text(),
                        '页码': tds[7].get_text(),
                    }
                    rows.append(row)
                except:
                    pass
            df = pd.DataFrame(rows)
            print(df)

            # 将每个页面的数据添加到DataFrame
            df_all = pd.concat([df_all, df], ignore_index=True)
            sleep(2)
            # # 点击下一页按钮
            try:
                next_button = driver.find_element_by_class_name("btn-next")
                next_button.click()
                sleep(7)
            except:
                break

        except:
            break

    return df_all


# 储存所有页的内容
all_dfs = []

# 循环遍历城市列表
count = 0
for city in cities:
    driver.execute_script("var q=document.documentElement.scrollTop=0")
    # 输入城市名
    search_box = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[2]/input')
    search_box.clear()
    sleep(1)
    search_box.send_keys(city)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[5]/span').click()
    sleep(2)

    # 获取数据
    df_all = get_info()
    all_dfs.append(df_all)

    # 输出信息
    count += 1
    print(f'{city} 数据获取完成。({count}/{len(cities)})')

# 将数值列转化为数字，无法识别的行将被删除
df_all = pd.concat(all_dfs, ignore_index=True)
df_all['数值'] = pd.to_numeric(df_all['数值'], errors='coerce')
df_all.dropna(inplace=True)

# 将DataFrame保存为Excel文件，使用用户指定的输出文件名
output_file_path = f"/Users/zhuyenan/Downloads/{additional_info}.xlsx"
save_data_to_excel(df_all, output_file_path)

# 关闭浏览器窗口
driver.quit()
