# 开发时间：2023/12/8 21:57
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


additional_info_list =["固定资产投资额"]
for additional_info in additional_info_list:

    # 构建完整的URL
    url = f"{base_url}{additional_info}"

    # 用户输入需要点击的子节点文本信息
    target_text = additional_info

# '北京', '天津', '上海', '安康', '安庆', '安顺', '安阳', '鞍山', '巴彦淖尔', '巴中', '白城', '白山', '白银', '百色',
#         '蚌埠', '包头', '宝鸡', '保定', '保山', '北海',
#         '本溪', '毕节', '滨州', '亳州', '沧州', '常德', '常州', '朝阳', '潮州', '郴州', '成都', '承德', '池州', '赤峰',
#         '崇左', '滁州', '达州', '大连', '大庆',
#         '大同', '丹东', '德阳', '德州', '定西', '东莞', '东营', '鄂尔多斯', '鄂州', '防城港', '佛山', '福州', '抚顺',
#         '抚州', '阜新', '阜阳', '赣州', '固原',
#         '广安', '广元', '广州', '贵港', '贵阳', '桂林', '哈尔滨', '海东', '海口', '邯郸', '汉中', '杭州', '合肥', '河池',
#         '河源', '贺州', '鹤壁', '鹤岗', '黑河',
#         '衡水', '衡阳', '呼和浩特',
    # 城市列表
    cities = [
         '北京市', '上海市','天津市','重庆市','黑龙江省','吉林省','辽宁省','内蒙古自治区'
    ,'河北省','新疆维吾尔自治区','甘肃省','青海省','陕西省','宁夏回族自治区','河南省','山东省',
          '山西省','安徽省','湖北省','湖南省','江苏省','四川省','贵州省','云南省','广西壮族自治区','浙江省','江西省','广东省','福建省','海南省'
    ]

    # 创建Chrome WebDriver
    driver = webdriver.Chrome(r'/workspaces/stata/chromedriver.exe')

    # 访问指定的URL
    driver.get(url)

    # 切换窗口，在单个测试用例中打开多个窗口并在它们之间切换
    driver.switch_to.window(driver.window_handles[-1])
    sleep(3)

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

    start_select = driver.find_element(By.CSS_SELECTOR, '#root > div.container > div.main.valueSearch_main__2mDQS > div '
                                                        '> div.valueSearch_left__31CpW > div.valueSearch_search-header__2xkaa '
                                                        '> div.valueSearch_nj-year__fzIxV > div:nth-child(2) > div')
    start_year = start_select.find_element(By.XPATH, "//li/a[text()='2013']").click()

    driver.execute_script("var q=document.documentElement.scrollTop=0")
    sleep(3)
    # 终止年份
    end = driver.find_element(By.XPATH,
                              '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[2]/div')
    end.click()

    end_select = driver.find_element(By.CSS_SELECTOR,
                                     '#root > div.container > div.main.valueSearch_main__2mDQS > div '
                                     '> div.valueSearch_left__31CpW > div.valueSearch_search-header__2xkaa '
                                     '> div.valueSearch_nj-year__fzIxV > div:nth-child(4) > div')
    # 74==2021年
    end_year = end_select.find_element(By.XPATH,
                                       '//*[@id="root"]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[2]/ul/li[75]').click()

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
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody.valueSearch_s-tab-tbody__3NF7f')))
                # 使用BeautifulSoup解析网页
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                # 找到<tbody>标签的class为"valueSearch_s-tab-tbody__b5cry"的节点
                tbody = soup.find('tbody', class_='valueSearch_s-tab-tbody__3NF7f')

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
    output_file_path = f"C:/Users/86136/Desktop/爬虫数据/{additional_info}.xlsx"
    save_data_to_excel(df_all, output_file_path)

    # 关闭浏览器窗口
    driver.quit()


