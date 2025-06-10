from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_driver():
    """Configure and return a Chrome WebDriver instance."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--lang=ko-KR")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login_pictory(driver, email: str, password: str) -> None:
    """Log in to pictory.ai using provided credentials."""
    driver.get("https://app.pictory.ai/login")
    time.sleep(3)

    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("✅ 로그인 시도 완료")
    time.sleep(10)


def input_script(driver, script_text: str) -> None:
    """Input a script into pictory.ai to generate a video."""
    try:
        driver.find_element(By.XPATH, "//*[contains(text(),'Script to Video')]//ancestor::button").click()
        print("▶ Script to Video 선택 완료")
        time.sleep(5)

        script_area = driver.find_element(By.TAG_NAME, "textarea")
        script_area.clear()
        script_area.send_keys(script_text)
        time.sleep(2)

        proceed_button = driver.find_element(By.XPATH, "//button[contains(., 'Proceed')]" or "//button[contains(., 'Next')]")
        proceed_button.click()
        print("✍ 스크립트 입력 완료, 다음 단계로 이동")
        time.sleep(15)

    except Exception as e:
        print(f"❌ 스크립트 입력 실패: {e}")


def main():
    # TODO: Replace with your own pictory.ai credentials
    email = "your_email@example.com"
    password = "your_password"
    script_text = (
        "외국인이 가장 많이 보는 한국 영상 TOP 3\n"
        "1. 한국 길거리 음식 - 세계인들이 놀라는 다양한 한국 길거리 음식들\n"
        "2. K-드라마 명장면 - 외국 팬들이 감동한 최고의 드라마 장면\n"
        "3. 한국 여행 브이로그 - 한국의 자연과 도시를 소개하는 인기 영상\n"
        "영상으로 한국의 매력을 함께 느껴보세요!"
    )

    driver = setup_driver()
    login_pictory(driver, email, password)
    input_script(driver, script_text)

    print("✅ 자동화 완료 - 후속 조치는 사용자 선택")


if __name__ == "__main__":
    main()
