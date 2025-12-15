from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\User\AndroidStudioProjects\7labatesting\app\build\outputs\apk\debug\app-debug.apk"
options.app_package = "com.example.a7labatesting"
options.app_activity = ".MainActivity"

driver = None

try:
    driver = webdriver.Remote("http://localhost:4723", options=options)
    print("Приложение запущено!")

    time.sleep(2)

    # Находим кнопку и кликаем
    button = driver.find_element(AppiumBy.ID, "com.example.a7labatesting:id/add_note_button")
    button.click()
    print("Кнопка нажата!")

    time.sleep(2)

    # Проверяем текст
    text = driver.find_element(AppiumBy.ID, "com.example.a7labatesting:id/notes_list").text
    print("Текст после клика:", text)

    time.sleep(3)

except Exception as e:
    print("Ошибка:", e)
finally:
    if driver:
        driver.quit()
    print("Тест завершён.")
