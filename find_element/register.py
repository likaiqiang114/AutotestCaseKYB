from util.capability import driver

#进入注册页面并且选头像
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

driver.find_element_by_id('com.tal.kaoyan:id/iv_picture').click()
driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()
