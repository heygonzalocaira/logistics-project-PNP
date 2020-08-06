from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()
elem = driver.find_element_by_id("uname").send_keys("jaime")
elem = driver.find_element_by_id("psw").send_keys("Jaimes123")
login = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div/button").click()

assert "No se encontro elemento:" not in driver.page_source
