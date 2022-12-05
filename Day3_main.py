
# 1. Dela upp i två halvor
# 2. Hitta gemensamma bokstaven
# 3. Hämta poängtalet för bokstaven
# 4. Addera till totaltsumman
# 5. Printa ut totalsumman

class Row_analyser():
    def __init__(self, text):
        clean_text = text.strip()
        length = int(len(clean_text) / 2)
        self.first_half = clean_text[:length]
        self.second_half = clean_text[length:]

    def return_common(self):
        for character in self.first_half:
            if character in self.second_half:
                return character

    def point_calculator(self, character):
        alphabet = '0 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        alphabet_list = alphabet.split(' ')
        return alphabet_list.index(character)

    def return_points(self):
        return self.point_calculator(self.return_common())


with open('Day3_input.txt') as file:
    total_score = 0
    for line in file:
        temp_object = Row_analyser(line)
        total_score += temp_object.return_points()
    print(total_score)