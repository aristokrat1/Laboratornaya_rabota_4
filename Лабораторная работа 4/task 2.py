def get_count_char(str_):
    list_of_words = str_.lower() # TODO посчитать количество каждой буквы в строке в аргументе str_
    list_of_words = list_of_words.split(" ")
    list_of_words = "".join(list_of_words)
    letters = list(list_of_words)
    dictionary = {}
    for letter in letters:
        if letter.isalpha() == True:
            dictionary[letter] = list_of_words.count(letter)
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
