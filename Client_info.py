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
    """Диалог с пользователем"""
    print("### Добро пожаловать на парсер Авито по квартирам ###")
    try:
        print("###[INFO]### В каком городе желаете посмотреть цены?\nПример:[Волгоград, Москва, Лысьва]")
        while True:
            new_citi = ""
            citi = input("###[INFO]### Ввод города: ").lower()
            if citi not in citi_tuple:
                print('###[INFO]### Введите корректное название города')
            else:
                for char in citi:
                    new_citi += dict_translate[char]
                print("###[INFO]### Ожидайте...")
                get_count_pages(new_citi)
                print("###[INFO]### Хотите ещё сыграть?[да\нет]")
                replay = input("###[INFO]### Ввод: ").lower()
                if replay == "нет":
                    print("###[INFO]### Конец парсингу!")
                    break

    except Exception as Ex:
        print("###[INFO]### Ошибка ввода данных")
        print(Ex)
