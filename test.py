from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

# options = Options()
# options.headless = True  # Run in headless mode to avoid opening a browser window
driver = webdriver.Chrome()
date = '2024-02-26'
end_date = '2024-02-26'
currency_code = '美元'

driver.get("https://www.boc.cn/sourcedb/whpj/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "erectDate")))

# Fill in the date and currency code in the form
date_input = driver.find_element(By.NAME, "erectDate")
date_input.clear()
date_input.send_keys(date)
end_Input = driver.find_element(By.NAME, "nothing")
end_Input.clear()
end_Input.send_keys(end_date)
ele = driver.find_element(By.NAME, "pjname")
select_ele = Select(ele)
select_ele.select_by_value(currency_code)
time.sleep(2)
button = driver.find_element_by_xpath('//*[@id="historysearchform"]/div/table/tbody/tr/td[7]')
button.click()

# Wait for the results to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[6]"))
)

# Extract the exchange sell rate
exchange_rate = driver.find_element(By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[6]").text

print(exchange_rate)
