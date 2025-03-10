# 1
# Представьте, что вы работаете с данными, содержащими информацию о клиентах интернет-магазина.
# Ваша задача — составить список уникальных клиентов, исключив повторяющиеся записи.
# Дан список customers, содержащий имена клиентов (с возможными повторениями).
# Необходимо создать и вывести новый список unique_customers,
# в котором каждое имя будет встречаться только один раз.
# customers = ["Иван", "Мария", "Иван", "Алексей", "Мария", "Елена"]

# 2
# Вы работаете в компании, занимающейся продажей книг.
# У вас есть три базы данных, содержащие списки книг, доступных в разных филиалах.
# Ваша задача — найти книги, которые есть во всех трёх филиалах.
# Даны три множества branch1, branch2 и branch3, содержащие названия книг в разных филиалах.
# Найдите и выведите множество книг, которые есть во всех трёх филиалах.
# branch1 = {"Война и мир", "Преступление и наказание", "Мастер и Маргарита"}
# branch2 = {"Война и мир", "Анна Каренина", "Мастер и Маргарита"}
# branch3 = {"Война и мир", "Мастер и Маргарита", "Идиот"}

# 3
# Вы работаете редактором, и вам нужно определить, насколько разнообразен словарный запас автора в его тексте.
# Для этого необходимо подсчитать количество уникальных слов в предоставленном фрагменте текста.
# Вводится одна строка, состоящая из слов, разделённых пробелами.
# Найдите и выведите количество уникальных слов.

# 4
# Вы работаете криптографом, и вам необходимо проанализировать текст на частоту появления каждого символа.
# Это поможет вам в дальнейшем построить шифр или провести анализ взлома.
# Ваша задача — составить таблицу частотности символов, чтобы узнать, какие символы встречаются чаще всего.
# Вводится строка. Подсчитайте, сколько раз встречается каждый символ в этом тексте,
# и выведите результат в виде списка пар "{символ}: {количество}" в порядке убывания.
# Каждую пару нужно вывести в отдельной строке


# 5
# Ваша задача — разработать систему для шифрования текстов.
# Один из простейших методов шифрования — это запись слов наоборот.
# Таким образом, слова остаются читаемыми, но их смысл становится менее очевидным.
# Вводится строка, состоящая из нескольких слов, разделённых пробелами.
# Переставьте все символы в каждом слове наоборот, сохранив порядок слов.
# text = "Привет мир"
# Ожидаемый результат: "тевирП рим"

# 6
# Вы разрабатываете текстовый анализатор, который должен находить самое длинное слово в тексте.
# Это полезно, например, для оценки сложности текста или для поиска потенциальных опечаток (слишком длинных слов).
# Вводится строка, состоящая из нескольких слов, разделённых пробелами.
# Найдите и выведите самое длинное слово в тексте. Если таких слов несколько, выведите первое из них.
# text = "Задачи на программирование развивают аналитическое мышление."
# Ожидаемый результат: "аналитическое"

# 7
# Вы работаете над задачей анализа текстов для определения их оригинальности.
# Одним из показателей является количество уникальных слов в тексте.
# Вводится строка, состоящая из нескольких слов, разделённых пробелами.
# Кроме того, в конце слова может стоять знак препинания - точка или запятая.
# Подсчитайте, сколько уникальных слов встречается в тексте, не учитывая регистр и знаки препинания.
# (то есть "Программирование" и "программирование." считаются одним и тем же словом).
# text = "Программирование — это искусство. Искусство требует времени и усилий."
# Ожидаемый результат: 8 (слова: "Программирование", "—", "это", "искусство", "требует", "времени", "и", "усилий")


# 8
# Вы разрабатываете программу для поиска анаграмм — слов,
# которые состоят из одних и тех же букв, но в разном порядке.
# Например, слова "лист" и "стил" являются анаграммами.
# Вводятся две строки. Проверьте, являются ли они анаграммами друг друга. Не учитывайте регистр и пробелы.
# word1 = "листо"
# word2 = "стило"
# Ожидаемый результат: True

# 9
# Вы разрабатываете систему, которая должна автоматически генерировать аббревиатуры
# из названий организаций или длинных фраз.
# Вводится строка, состоящая из нескольких слов, разделённых пробелами.
# Сгенерируйте аббревиатуру, взяв первые буквы каждого слова и
# составив из них новое слово (все буквы должны быть заглавными).
# text = "Федеральная служба безопасности"
# Ожидаемый результат: "ФСБ"


def make_filter(threshold):
    def filter_func(value):
        return value > threshold

    return filter_func


filter_above_10 = make_filter(10)
data = [5, 10, 15, 20]
filtered_data = list(filter(filter_above_10, data))
print(filtered_data)
