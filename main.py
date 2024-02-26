from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from get_currency import getName

def get_exchange_rate(date,currency_code):
    # 配置Chrome选项，以无头模式运行
    # options = Options()
    # options.headless = True
    driver = webdriver.Chrome()

    try:
        # 打开中国银行外汇牌价网站
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        # 输入日期
        date_input = driver.find_element(By.NAME, "erectDate")
        date_input.clear()
        date_input.send_keys(date)

        end_Input = driver.find_element(By.NAME, "nothing")
        end_Input.clear()
        end_Input.send_keys(date)

        # 输入货币代码
        ele = driver.find_element(By.NAME, "pjname")
        select_ele = Select(ele)
        select_ele.select_by_value(currency_code)
        time.sleep(2)
        button = driver.find_element_by_xpath('//*[@id="historysearchform"]/div/table/tbody/tr/td[7]')
        button.click()

        # 等待页面加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[6]"))
        )

        # 获取现汇卖出价
        exchange_rate = driver.find_element(By.XPATH, "//div[@class='BOC_main publish']/table/tbody/tr[2]/td[6]").text
        return exchange_rate
    except Exception as e:
        print("没有得到汇率重试:", str(e))
        return None
    finally:
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <date> <currency_code>")
        sys.exit(1)

    date = sys.argv[1]
    currency_code = sys.argv[2]
    currency_code = getName(currency_code)
    print(currency_code)
    exchange_rate = get_exchange_rate(date,currency_code)

    if exchange_rate:
        # 将结果写入result.txt文件
        result = ' '.join([date, currency_code, exchange_rate])
        print(result)
        with open("result.txt", "w",encoding='utf-8') as file:
            file.write(result)
    else:
        print("Failed to retrieve exchange rate.")