#1
# f = open('file.txt', 'r', encoding='utf-8')
# lines1 = set(f.read().split())
# f.close()
# f = open('file2.txt', 'r', encoding='utf-8')
# lines2 = set(f.read().split())
# f.close()
#
# print('Первое множество:', lines1)
# print('Второе множество:', lines2)
#
# intersection = lines1.intersection(lines2)
#
# if len(intersection) > 0:
#     print('Совпадения найдены:', intersection)
# else:
#     print('Совпадения не найдены')
#
#
#3

# fr = open('file_r.txt')
# fw = open('file_w.txt', 'w')
#
# frl = fr.readlines()
# frll = frl[:-1]
#
# for line in frll:
#     fw.write(line)
#
# fr.close()
# fw.close()

#4


# f = open('file_r.txt')
# text = f.read()
# f.close()
# lines = text.split('\n')
# max_line = lines[0]
# index = 0
# for i in range(len(lines)):
#     if len(max_line) < len(lines[i]):
#         max_line = lines[i]
#
# print(max_line)

#5


# word = input("Введите слово ")
# count = 0
# with open("file5.txt", 'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             if(i==word):
#                 count=count+1
# print("Заданных слов",word, ":", count)


#6

search_text = input("Введите слово которое хотите найти ")
replace_text = input("Введите на, что заменить ")
with open(r'file5.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
with open(r'file5.txt', 'w') as file:
    file.write(data)
print("Текст изменен")