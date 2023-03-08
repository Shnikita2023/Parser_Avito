from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from datetime import datetime

import time
import csv


def start_browser():
    """Запуск драйвера Селeниум"""
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Отключение режима веб-драйвера
    options.add_argument('headless')  # Отключение фонового режима
    s = Service(r"C:\Users\79991\PycharmProjects\Parser\Parser_Avito\driver\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.maximize_window()
    return browser


def get_count_pages(citi: str):
    """Получение количество страниц"""
    try:
        with start_browser() as browser:
            browser.get(url=f"https://www.avito.ru/{citi}/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg")
            time.sleep(2)
            count_page_element = browser.find_elements(By.CLASS_NAME, "pagination-item-JJq_j")
            count_page = int([count.text for count in count_page_element][-2])
            parsing_page(browser, count_page)
        print("Парсер закончен")

    except Exception as Ex:
        print(Ex)
        print("Ошибка данных")


def parsing_page(browser, count_page):
    """Парсинг имён, цен, описание, ссылка на полный продукт"""
    try:
        name_file = datetime.now().strftime("%d_%m_%Y_%H_%M")
        with open(f"citi_{name_file}.csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ("Количество комнат", "Цена", "Описание")
            )
        for page in range(1, 2):
            print(f"#INFO# Парсер {page} страницы")
            url = f"https://www.avito.ru/all/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?p={page}"
            browser.get(url=url)
            names_flats = browser.find_elements(By.CLASS_NAME, "iva-item-titleStep-pdebR")
            prices_flats = browser.find_elements(By.CLASS_NAME, "price-text-_YGDY.text-text-LurtD.text-size-s-BxGpL")
            description_flats = browser.find_elements(By.CLASS_NAME, "iva-item-text-Ge6dR.iva-item-description-FDgK4.text-text-LurtD.text-size-s-BxGpL")
            total = zip(names_flats, prices_flats, description_flats)
            for name, price, description in total:
                with open(f"citi_{name_file}.csv", "a", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow((name.text, price.text, description.text))

    except Exception as Ex:
        print(Ex)


def main():
    pass


if __name__ == '__main__':
    main()
