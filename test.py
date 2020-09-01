from selenium import webdriver
driver = webdriver.Chrome('C:\drivers\chromedriver.exe')
driver.get("http:/www.wikipedia.org/")
search_field = driver.find_element_by_id('searchInput').send_keys('Test Automation')
search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")
search_button.click()
assert "Test Automation" in driver.title
driver.quit()
