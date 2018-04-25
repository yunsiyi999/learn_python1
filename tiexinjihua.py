#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert
import selenium.common.exceptions


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.sit.nonobank.com/Admin/Login")
#driver.maximize_window()
driver.set_window_size(1920,1200)
driver.find_element_by_id("username").send_keys("xuxuadmin")
driver.find_element_by_name("password").send_keys("it789123")
driver.find_element_by_id("resend_sms_code").click()

#driver.implicitly_wait(2)  #智能等待2秒

current_window = driver.current_window_handle  # 获取当前窗口handle name

all_windows = driver.window_handles
for window in all_windows:
    if window != current_window:
        driver.switch_to.window(window)
        alert1 = driver.switch_to_alert()
        if alert1.text=="请稍后重试，1分钟一次!":
            time.sleep(60)
            alert1.accept()
            driver.find_element_by_id("resend_sms_code").click()

        else:
            pass

driver.find_element_by_name("sms_code").send_keys("888888")
driver.find_element_by_name("submit").click()
#driver.find_element_by_xpath("//html/body/xml/div/div/dl/dd/ul/li[@href='']")
time.sleep(2)
driver.switch_to_frame('main') #页面使用iframe框架，需要移交表单操作页面
driver.find_element_by_xpath('//a[@href="/Admin/Licai/FinancePlanList"]').click()
time.sleep(1)
driver.switch_to_default_content() #跳出iframe框架
time.sleep(1)
driver.switch_to_frame('main')
time.sleep(1)
driver.find_element_by_xpath('//input[@value="新增诺诺精选计划"]').click()
time.sleep(3)
driver.switch_to_default_content()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
driver.set_window_size(1920,1200)

driver.find_element_by_xpath("//input[@id='platform_type2']").click()
driver.find_element_by_xpath("//input[@id='homepage_is_show2']").click()
driver.find_element_by_xpath("//input[@name='fp_homepage_recommend_sort_num']").send_keys("1")
driver.find_element_by_xpath("//input[@name='fp_title']").send_keys("招财进宝自动")
driver.find_element_by_name("fp_debt_expect_price").send_keys("100000")
driver.find_element_by_name("fp_price_min").send_keys("1000")
driver.find_element_by_name("fp_price_max").send_keys("50000")
driver.find_element_by_id("fp_price_increment").send_keys("1")
driver.find_element_by_id("fp_scope").find_element_by_xpath("//span/select/option[2]").click()  #贴心智投
driver.find_element_by_xpath("//td/select[@id='fp_is_index']/option[@value='2']").click()  #展示范围
driver.find_element_by_id("fp_expect_text").send_keys("2") #招财卡锁定期
driver.find_element_by_id("planRateSet").click()
time.sleep(2)

# driver.find_element_by_xpath("//div/div/table/tbody/tr[10]/td[2]").send_keys("15")

A=["baseRate","finalRate","mostRate"]
B=["7.20","7.30","7.30"]
j=0

for i in range(len(A)):
    for j in range(len(B)):
        if j==i:
            driver.find_element_by_id(A[i]).send_keys(B[j])
        else:
            pass

driver.find_element_by_xpath("//td[@style='padding-left:220px']/input[@id='prodRate']").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//input[@id='fp_publish_date']").send_keys(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
driver.find_element_by_xpath("//td[@colspan='8']/input[@class='inputbutx_1'and @onclick='saveFinancePlan()']").click()  #保存
driver.find_element_by_xpath("//input[@id='submitBtn']").click()  #二次确认页面确定
time.sleep(1)
driver.switch_to_alert().accept()
time.sleep(1)
driver.switch_to_alert().accept()

driver.quit()


