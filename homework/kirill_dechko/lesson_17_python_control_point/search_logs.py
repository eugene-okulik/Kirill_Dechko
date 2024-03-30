import datetime
import os
import argparse  # для обработки аргументов командной строки
from colorama import init, Style, Fore

init()
# Создание парсера: argparse.ArgumentParser, который содержит спецификации аргументов и опций
parser = argparse.ArgumentParser(
    # Описание программы
    prog="Logs_parser",
    description=Fore.LIGHTGREEN_EX + "The program analyzes the file or file directory and finds logs according to the"
                                     " parameters that you specified."
                                     " Attention! To use the program, you need to enter some parameters:"
                                     " Mandatory: start date, operator, path to the directory or to the file."
                                     " Date format: yyyy-mm-dd hh:mm:ss.SSS, operator format: '<', '>', '=' or '><',"
                                     " path to the directory: ...your path to file.log"
                                     " Optional parameters: search_param (a word or more to search), end_date."
                                     " To clean the console, use the 'clear' command"
                                     " Example query with operator '><':"
                                     " --start_date '2022-02-03 01:05:40.459'"
                                     " --operator '><' --end_date '2022-02-03 01:06:46.490'"
                                     " --path_to_file ...your path to file.log"
                                     " --search_param 'ERROR'" + Style.RESET_ALL,
    epilog=Fore.LIGHTBLUE_EX + "Read the description carefully before using the program" + Style.RESET_ALL)
# Аргументы которые принимает программа, их описание: краткое имя, полное имя, тип данных.
start_date = parser.add_argument("-S", "--start_date", type=str,
                                 help="Start date for the search (format: yyyy-mm-dd hh:mm:ss.SSS)")
end_date = parser.add_argument("-E", "--end_date", type=str,
                               help="End date for the search (format: yyyy-mm-dd hh:mm:ss.SSS)")
operator = parser.add_argument("-O", "--operator", type=str,
                               help="Comparison operator: '<', '>', '=', '><'")
path_to_file = parser.add_argument("-P", "--path_to_file", type=str,
                                   help="Path to a file or directory containing the file")
search_param = parser.add_argument("-SP", "--search_param", type=str, help="Any words to find rows")
nsp = parser.add_argument("-NSP", "--nsp", type=str, help="No search params (nsp)")
full_log = parser.add_argument("-FL", "--full_log", type=str, help="To show full logs")
args = parser.parse_args()

# Проверка корректности параметров nsp и full_log введенных пользователем в консоли
if args.nsp and args.nsp != 'nsp':
    print(Fore.LIGHTRED_EX + f"Incorrect value for nsp, must be 'nsp', not {args.nsp}" + Style.RESET_ALL)
elif args.full_log and args.full_log != 'fl':
    print(Fore.LIGHTRED_EX + f"Incorrect value for full_log, must be 'fl', not {args.full_log}" + Style.RESET_ALL)
elif args.operator and args.operator not in ['<', '>', '=', '><']:
    print(Fore.LIGHTRED_EX + "Incorrect operator, must be '<', '>', '=', '><'" + Style.RESET_ALL)
else:
    # Функция поиска пути к файлу или папке
    def find_path_to_files(param):  # param может быть путем к файлу или директории
        path_list = []
        if os.path.isdir(param):  # если param дериктория
            """
            Цикл for root, dirs, files in os.walk(param) используется для обхода директорий и файлов в
            указанной директории param и ее поддиректориях.
            root: Это директория, которую мы обрабатываем. Внутри этой директории находятся поддиректории и файлы.
            dirs: Это список поддиректорий в директории root.
            files: Это список файлов в директории root."""
            for root, dirs, files in os.walk(param):  # обход всех файлов в указанной директории
                for file in files:  # для файлов дериктории
                    if file.endswith(".log"):  # если его расширение .log
                        file_path = os.path.join(root, file)
                        """os.path.join(root, file) объединяет root и file в одну строку, представляющую
                         полный путь к файлу. Например,если root равен “C:/Users/user/Desktop”, а file равен
                          “document.txt”, то file_path будет равен “C:/Users/user/Desktop/document.txt”."""
                        path_list.append(file_path)  # то файл добавляем в список path_list
            return path_list
        elif os.path.isfile(param):  # если param путь к файлу, функция возвращает его полный путь.
            return [param]
        else:
            return "File not found"


    def read_log_file():  # Функция чтения данных из файла, читаем логи по одной строке,
        # из файлов найденных функцией find_path_to_files (выше)
        try:
            for file_path in find_path_to_files(args.path_to_file):
                with open(file_path, "r") as data_file:
                    for line in data_file.readlines():
                        yield line
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "ERROR! No such file or directory" + Style.RESET_ALL)

    # Поиск слова и вывод 150 символов до и после слова
    def display_context_around_word(text, word, context_length=151):
        index = text.find(word)  # определение индекса указанного слова
        start_index = max(0, index - context_length)  # вычисляет начальный индекс слова
        end_index = min(len(text), index + len(word) + context_length)  # вычисляет конечный индекс слова
        context = text[start_index:end_index]  # помещаем в переменную 150 символов до -слово- и 150 символов после
        return context


    find_rows_param = []  # список для заполнения данными удовлетворяющими поиску


    def is_search_params():  # Поиск строк по параметрам указанным пользователем (nsp, full_log, search_param)
        if args.search_param and args.nsp:  # если search_param и nsp в запросе и nsp корректен
            if args.search_param not in row and args.full_log:  # и если args.full_log в запросе
                find_rows_param.append([row])
            elif args.search_param not in row:  # если args.full_log нет в запросе но search_param и nsp в зпросе
                find_rows_param.append([row[:301]])
        elif args.search_param:  # если только search_param в зпросе
            if args.search_param in row:
                if args.full_log:  # и если args.full_log в запросе
                    find_rows_param.append([row])
                else:  # и если нет args.full_log в запросе но search_param в запросе
                    context = display_context_around_word(row, args.search_param, context_length=151)
                    find_rows_param.append([context])
        elif args.full_log:  # и если args.full_log в запросе
            find_rows_param.append([row])
        else:  # и если нет args.full_log в запросе
            context = display_context_around_word(row, args.search_param, context_length=151)
            find_rows_param.append([context])


    # Цикл для обработки строк с датами и поиска нужных строк
    for row in read_log_file():
        if row.startswith("20"):
            date_in_row = row[:23]
            date_in_file = datetime.datetime.strptime(date_in_row, '%Y-%m-%d %H:%M:%S.%f')
            user_start_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d %H:%M:%S.%f')
            if args.operator == '><':
                try:
                    user_end_date = datetime.datetime.strptime(args.end_date, '%Y-%m-%d %H:%M:%S.%f')
                    if user_start_date <= date_in_file <= user_end_date:
                        is_search_params()
                except ValueError:
                    print(Fore.LIGHTRED_EX + "ERROR! Time data does not match format '%Y-%m-%d %H:%M:%S.%f,"
                                             "check params: start_date and end_date"
                          + Style.RESET_ALL)
                    break  # останавливаем код при ошибке
            elif args.operator == '=' and date_in_file == user_start_date:
                is_search_params()
            elif args.operator == '>' and date_in_file >= user_start_date:
                is_search_params()
            elif args.operator == '<' and date_in_file <= user_start_date:
                is_search_params()

    # Вывод результатов
    if len(find_rows_param) >= 1:
        print(Fore.LIGHTGREEN_EX + f"Search parameters:\ndate: {args.start_date}\noperator: {args.operator}"
                                   f"\nend_date: {args.end_date}\ncontains words: {args.search_param}\nnsp: {args.nsp}"
                                   f"\nfull_log: {args.full_log}" + Style.RESET_ALL)
    # настрока цветов отображения в консоли
    for elem in find_rows_param:
        date_part = elem[0][:23]  # Зеленый == Fore.LIGHTGREEN_EX
        message_part = elem[0][23:301]
        message_part2 = elem[0][301:]  # серый == Fore.WHITE
        print(Fore.LIGHTGREEN_EX + str(date_part) + Style.RESET_ALL + str(message_part)
              + Fore.WHITE + str(message_part2) + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"Found {len(find_rows_param)} items by search criteria " + Style.RESET_ALL)
