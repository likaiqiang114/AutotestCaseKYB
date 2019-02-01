from util.capability import driver

def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('LKQ')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('666666')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

