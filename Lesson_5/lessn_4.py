"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

new_lst = ["Один", "Два", "Три", "Четыре"]
count = 0
with open("text_lessn_4.txt", "rt", encoding="UTF-8") as file:
    for i in file.readlines():
        s = i.split()
        s[0] = new_lst[count]
        count += 1
        with open("text_lesson_4.txt", "a", encoding="UTF-8") as file_w:
            file_w.write(f'{" ".join(s)}\n')
