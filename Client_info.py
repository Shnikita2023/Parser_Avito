from Parser_Avito import get_count_pages

dict_translate = {
    "а": "a", "б": "b", "в": "v", "г": "g",
    "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s",
    "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "sch", "ь": "", "ы": "y",
    "ъ": "", "э": "e", "ю": "yu", "я": "ya"
}
citi_tuple = ("москва", "cанкт-петербугр", "сочи", "лысьва", "чусовой")


def name_citi():
    print("### Добро пожаловать на парсер Авито по квартирам ###")
    try:
        print("В каком городе желаете посмотреть цены?\nПример:[Волгоград, Москва, Лысьва]\n"
              "Если желаете выйти,то напишите 'выход'")
        while True:
            new_citi = ""
            citi = input("Ввод города: ").lower()
            if citi == "выход":
                print("Конец парсингу!")
                break

            if citi not in citi_tuple:
                print('Введите корректное название города')
            else:
                for char in citi:
                    new_citi += dict_translate[char]
                print("Ожидайте...")
            get_count_pages(new_citi)


    except Exception as Ex:
        print(Ex)


