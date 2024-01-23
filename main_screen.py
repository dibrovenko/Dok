import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By


def test_fullpage_screenshot(url: str, filename: str):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1400,2100")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)
        time.sleep(2)

        ele = driver.find_element(By.TAG_NAME, 'body')
        height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, height)

        #driver.save_screenshot(f"screenshots/{filename}")
        driver.save_screenshot(f"screenshots.png")
        print(f"Screenshot")
    except Exception:
        pass
    finally:
        driver.close()
        driver.quit()

"""if __name__ == "__main__":
    test_fullpage_screenshot("https://tproger.ru", "tproger.png")
    test_fullpage_screenshot("https://stackoverflow.com", "stackoverflow.png")
"""