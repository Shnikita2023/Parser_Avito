from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from datetime import datetime

import time
import json

dict_flats = {}
number_flat = 1

def start_browser():
    """Запуск драйвера Селeниум"""
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Отключение режима веб-драйвера
    # options.add_argument('headless')  # Отключение фонового режима
    s = Service(r"C:\Users\79991\PycharmProjects\Parser\Parser_Avito\driver\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    return browser


def get_count_pages(citi: str) -> None:
    """Получение количество страниц"""
    try:
        time_file = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        with start_browser() as browser:
            url = f"https://www.avito.ru/{citi}/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg"
            browser.get(url=url)
            count_page_element = browser.find_elements(By.CLASS_NAME, "pagination-item-JJq_j")
            count_page = int([count.text for count in count_page_element][-2])
            print(count_page)
            for page in range(1, 2):
                print(f"###[INFO]### Парсер {page} страницы")
                browser.get(url=f"{url}?p={page}")
                parsing_page(browser)
        append_data_csv(time_file)



    except Exception as Ex:
        print("###[INFO]### Ошибка данных при получение количество страниц")
        print(Ex)


def parsing_page(browser: webdriver):
    """Парсинг имён, цен, описание, ссылка на полный продукт"""
    try:
       data_flats = browser.find_elements(By.CLASS_NAME, "iva-item-body-KLUuy")
       for data in data_flats:
           global number_flat
           link_flat = data.find_element(By.TAG_NAME, "a").get_attribute("href")
           price_flat = data.find_element(By.CLASS_NAME, "iva-item-priceStep-uq2CQ").text
           count_room = data.find_element(By.CLASS_NAME, "iva-item-titleStep-pdebR").text
           description_flat = data.find_element(By.CLASS_NAME, "iva-item-autoParamsStep-WzfS8").text
           addres_flat = data.find_element(By.CLASS_NAME, "iva-item-developmentNameStep-qPkq2").text.replace("\n", " ").replace(",", "")
           dict_flats[number_flat] = [count_room, price_flat, description_flat, addres_flat, link_flat]
           number_flat += 1

    except Exception as Ex:
        print("Ошибка парсинга")
        print(Ex)


# def create_title_csv(time_file: str) -> None:
#     """Создание столбцов в таблице"""
#     try:
#         with open(f"citi_{time_file}.csv", "w", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 ("Количество комнат", "Цена", "Описание")
#             )
#
#     except Exception as Ex:
#         print("###[INFO]### Cтолбцы не созданы")
#         print(Ex)


def append_data_csv(time_file: str) -> None:
    """Добавление данных в таблицу"""
    try:
        with open(f"citi_{time_file}.json", "w", encoding="utf-8") as file:
            json.dump(dict_flats, file, ensure_ascii=False, indent=4)


    except Exception as Ex:
        print("###[INFO]### Файлы не добавлены")
        print(Ex)


def main():
    pass


if __name__ == '__main__':
    main()
