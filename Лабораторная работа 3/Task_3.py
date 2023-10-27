def count_letters(text):
    letter_dictionary = {}

    for char in text:
        char = char.lower()

        if char.isalpha():

            if char in letter_dictionary:
                letter_dictionary[char] += 1
            else:
                letter_dictionary[char] = 1

    return letter_dictionary


def calculate_frequency(letter_dictionary):
    total_letters = sum(letter_dictionary.values())

    letter_frequencies_dic = {}

    for letter, count in letter_dictionary.items():
        frequency = count / total_letters
        letter_frequencies_dic[letter] = frequency

    return letter_frequencies_dic


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


letter_dictionary = count_letters(main_str)
letter_frequencies_dic = calculate_frequency(letter_dictionary)


for letter, frequency in letter_frequencies_dic.items():
    print(f"{letter}: {frequency: .2f}")

