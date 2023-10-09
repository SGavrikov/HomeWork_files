import os
dir_path = "Files/Sorted/"
files = os.listdir(dir_path)   # создание списка файлов внутри каталога Sorted
files_list = []
for file_name in files:
    path = os.path.join(dir_path, file_name)
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            files_list.append([len(f.readlines()), file_name])     # создание списка [количество строк, имя файла]
files_list.sort()
with open('result.txt', 'w') as f:          # очистка файла (если ранее был создан)
    f.write('')
for elem in files_list:
    path = os.path.join(dir_path, elem[1])
    with open(path, 'r', encoding='utf-8') as source_file, open('result.txt', 'a') as f:
        f.write(f'{elem[1]}\n')
        f.write(f'{elem[0]}\n')
        for line in source_file:
            f.write(line)
            if "\n" not in line:            # переход на новую строку, если в исходном файле нет
                f.write("\n")
