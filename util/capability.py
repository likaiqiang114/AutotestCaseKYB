from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62025'
desired_caps['platforVersion']='5.1.1'



desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

#不重置用户的首次打开应用状态-
desired_caps['noReset']='True'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#隐式等待
driver.implicitly_wait(5)

def check_cancelBtn():
    print('check_can')
    try:
        cacelBtn=driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no CancelBtn')
    else:cacelBtn.click()

def check_skipBtn():
    print("check_skipBtn")
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()

