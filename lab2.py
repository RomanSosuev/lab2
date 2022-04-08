"""
Программа, которая читая текст из файла, выводит на экран предложения, начинающиеся с однобуквенных слов.
Входной поток моделируется конечным файлом произвольной длины. Длина файла определяется доступной памятью на диске.
Чтение посимвольно. Максимальный размер рабочего буфера для обработки - 1000. Вывод результата работы программы осуществляется на экран.

"""
import os
import time

max_buf_len = 1000        # максимальный размер рабочего буфера
read_buf_len = 1          # размер буфера чтения
work_buf = ""             # рабочий буфер

try:
    start = time.time()         # Начало отсчета времени работы программы
    with open("text.txt", "r", encoding='utf-8') as file:      # открываем файл              
        print("\n-----Результат работы программы-----\n")
        buf = file.read(read_buf_len)        # читаем первый блок
        
        if not buf:                          # если файл пустой                
            print ("\nФайл text.txt пустой.\n")
        while buf:                           # пока файл не пустой   
            work_buf += buf                  # обработка текущего блока   
            if buf.find(".") >= 0 or buf.find("!") >= 0 or buf.find("?") >= 0:    
                work_buf = work_buf.strip()
                if len(work_buf) > 1 and (work_buf[1] == " " or work_buf[1] == "." or work_buf[1] == "!" or work_buf[1] == "?"):
                    print(work_buf)
                work_buf = ""
            buf = file.read(read_buf_len)    # читаем следующий символ   
            if len(work_buf) >= max_buf_len and buf.find(".") < 0 and buf.find("!") < 0 and buf.find("?") < 0:    # Если буфер переполнен и нет окончания предложения
                print ("\nФайл text.txt не содержит знаков окончания предложения и максимальный размер буфера превышен.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                work_buf = ""
                break
        if len(work_buf) > 0:    # Если буфер переполнен и нет окончания предложения
                print ("\nХвост файла text.txt не содержит знаков окончания предложения \nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")

        finish = time.time()
        result = finish - start
        print("Program time: " + str(result) + " seconds.")     # Вывод времени работы программы
        
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")             

    
