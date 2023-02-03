import datetime
import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

import xlsxwriter
from selenium import webdriver

basedir = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = TimedRotatingFileHandler(os.path.join(basedir, 'crawler.log'), when="D", interval=1,
                                        backupCount=10, encoding='utf-8')
# file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_opt.add_experimental_option("prefs", prefs)


if os.name == 'posix':
    driver = webdriver.Chrome(executable_path="/Users/wuchangfang/Downloads/chromedriver",
                              options=chrome_opt)
else:
    driver = webdriver.Chrome(executable_path="C:/ProgramData/chromedriver_win32/chromedriver.exe",
                              )

driver.set_window_position(-10, 0)

file_name = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx'
workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet("数据")
bold = workbook.add_format({'bold': True})
worksheet.write('A1', '名字', bold)
worksheet.write('B1', '职称', bold)
worksheet.write('C1', '医院', bold)
worksheet.write('D1', '科室', bold)
worksheet.write('E1', '擅长', bold)
worksheet.write("F1", "疗效", bold)
worksheet.write('G1', '态度', bold)
row = 1


def login():
    row = 1
    for i in range(1, 201):
        url = f"https://www.haodf.com/doctor/list-all-xinlizixunke.html?p={i}"
        driver.get(url)
        time.sleep(1)
        # 找到 医生列表的ul
        # driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/ul")
        elements = driver.find_elements_by_class_name("js-fam-doc-li")
        for element in elements:
            name = element.find_element_by_class_name("doc-name").text
            print(name)
            zhicheng = element.find_element_by_class_name("ml15").text
            print(zhicheng)
            hospital = element.find_element_by_class_name("mt5").text
            department = element.find_element_by_class_name("mt5").find_element_by_class_name("ml5").text
            print(department)
            hospital = hospital.replace(department, "")
            print(hospital)
            good_at = element.find_element_by_class_name("doc-speciaty").text.replace("擅长: ", "")
            print(good_at)

            taidu = element.find_element_by_class_name("taidu").text.replace("态度：\n", "")
            print(taidu)
            liaoxiao = element.find_element_by_class_name("liaoxiao").text.replace("疗效：\n", "")
            print(liaoxiao)
            worksheet.write(row, 0, name)
            worksheet.write(row, 1, zhicheng)
            worksheet.write(row, 2, hospital)
            worksheet.write(row, 3, department)
            worksheet.write(row, 4, good_at)
            worksheet.write(row, 5, liaoxiao)
            worksheet.write(row, 6, taidu)
            row += 1

        # driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/div[2]").click()
        #
        # driver.find_element_by_id("account_input").send_keys("nr_9l85370p7")
        # driver.find_element_by_id("password_input").send_keys("854976")
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="pwd_confirm"]').click()
        # driver.find_element_by_xpath('//*[@id="zhou-bang"]').click()
        import random
        time.sleep(random.choice(range(1, 10)))
    workbook.close()


if __name__ == '__main__':
    try:
        login()
        # update_username_by_nickname("vttalk")
        driver.close()
    except Exception as e:
        import traceback

        traceback.print_exc()
