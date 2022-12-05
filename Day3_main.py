################################################################################################################
# Dag 3 del 1
################################################################################################################

# 1. Dela upp i två halvor
# 2. Hitta gemensamma bokstaven
# 3. Hämta poängtalet för bokstaven
# 4. Addera till totaltsumman
# 5. Printa ut totalsumman

class Row_analyser():

    def __init__(self, text):
        '''Skapar ett object med två strängar, en för varje compartment.'''
        clean_text = text.strip()
        length = int(len(clean_text) / 2)
        self.first_half = clean_text[:length]
        self.second_half = clean_text[length:]

    def return_common(self):
        '''Hittar gemensam bokstab och returnerar denna.'''
        for character in self.first_half:
            if character in self.second_half:
                return character

    def point_calculator(self, character):
        '''Input är ett tecken, output är dess poängtal'''
        alphabet = '0 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
        alphabet_list = alphabet.split(' ')
        return alphabet_list.index(character)

    def return_points(self):
        '''Hittar gemensam bokstav, beräknar poängtal och returnerar.'''
        return self.point_calculator(self.return_common())


with open('Day3_input.txt') as file:
    total_score = 0
    for line in file:
        temp_object = Row_analyser(line)
        total_score += temp_object.return_points()
    print(total_score)

################################################################################################################
# Dag 3 del 2
################################################################################################################
# 1. Skapa gruppobjekt
# 2. Läs in tre rader
# 3. Hitta gemensam nämnare
# 4. Hitta poängtalet och addera till totalen
# 5. Rensa raderna
# 6. returnera totalsumman

class Elf_group(Row_analyser):
    def __init__(self, list_with_lines):
        '''Skapar tre strings, en för varje elf.'''
        self.elf1 = list_with_lines[0]
        self.elf2 = list_with_lines[1]
        self.elf3 = list_with_lines[2]

    def find_common_badge(self):
        '''Hittar bokstaven som är gemensam i alla tre texter och returnerar den.'''
        list_of_shared_between_first_two = []
        for character in self.elf1:
            if character in self.elf2:
                list_of_shared_between_first_two.append(character)
        for character in list_of_shared_between_first_two:
            if character in self.elf3:
                return character

    def return_badge_score(self):
        '''Hittar bokstaven som är gemensam och returnerar dess poängsumma. Dvs returnerar elf gruppens badges poäng.'''
        return self.point_calculator(self.find_common_badge())


with open('Day3_input.txt') as file:
    total_score = 0
    counter = 0 # Används för att hålla koll på när vi samlat en hel grupp.
    list_of_elfitems = []   # Lista med alla rader av text, dvs innehållet i elfs ryggsäckar.
    for line in file:

        clean_line = line.strip()
        list_of_elfitems.append(clean_line)
        counter += 1

        if counter == 3:    # När vi samlat en hel elfgrupp kommer vi hit.
            temp_elfgroup = Elf_group(list_of_elfitems) # Skapar ett objekt för elfgruppen som gör alla beräkningar.
            total_score += temp_elfgroup.return_badge_score()
            counter = 0 # Nollställer räknare inför nästa grupp av elfs.
            list_of_elfitems = []


    print(total_score)


