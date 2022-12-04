# Dag 2 del 1

# Algoritm
# 1. läs in varje rad och strippa
# 2. Baserat på första bokstaven adderas poäng
# 3. Baserat på kombinationen av bokstäver adderas ytterligare en summa
# 4. Printa ut totalen

#file = open('Day2_input.txt', 'r')

#Vinnst

class Game_round():

    # Skapar en lista med de två bokstäverna
    def __init__(self, text):
        self.letter_list = text.split(' ')

    def score_returner(self):
        score = 0
        if self.letter_list[0] == 'A':  # De gör sten

            if self.letter_list[1] == 'X':  # Du sten
                score+= 4
            if self.letter_list[1] == 'Y':  # Du påse
                score+= 8
            if self.letter_list[1] == 'Z':  # Du sax
                score+= 3

        if self.letter_list[0] == 'B': # De drar påse

            if self.letter_list[1] == 'X':  # Du sten
                score+= 1
            if self.letter_list[1] == 'Y':  # Du påse
                score+= 5
            if self.letter_list[1] == 'Z':  # Du sax
                score+= 9

        if self.letter_list[0] == 'C':  # De gör sax

            if self.letter_list[1] == 'X':  # Du sten
                score+= 7
            if self.letter_list[1] == 'Y':  # Du påse
                score+= 2
            if self.letter_list[1] == 'Z':  # Du sax
                score+= 6

        return score



with open('Day2_input.txt') as file:
    total_score = 0
    counter = 0
    for line in file:
        text = line.strip()
        temp_score_counter_object = Game_round(text)
        total_score += temp_score_counter_object.score_returner()

print(total_score)
###################################################################################################################
# Dag 2 del 2
###################################################################################################################

class Game_round_part2(Game_round):


    def score_returner(self):
        score = 0
        if self.letter_list[0] == 'A':  # De gör sten

            if self.letter_list[1] == 'X':  # Förlora. Sax.
                score+= 0 + 3
            if self.letter_list[1] == 'Y':  # Oavgjort. Sten.
                score+= 3 + 1
            if self.letter_list[1] == 'Z':  # VInna. Påse.
                score+= 6 + 2

        if self.letter_list[0] == 'B': # De drar påse

            if self.letter_list[1] == 'X':  # Förlora, sten.
                score+= 0 + 1
            if self.letter_list[1] == 'Y':  # Oavgjort, påse.
                score+= 3 + 2
            if self.letter_list[1] == 'Z':  # Vinna, sax.
                score+= 6 + 3

        if self.letter_list[0] == 'C':  # De gör sax

            if self.letter_list[1] == 'X':  # Förlora, påse
                score+= 0 + 2
            if self.letter_list[1] == 'Y':  # Oavjort, sax
                score+= 3 + 3
            if self.letter_list[1] == 'Z':  # VInna, sten
                score+= 6 + 1

        return score

with open('Day2_input.txt') as file:
    total_score_2 = 0
    counter = 0
    for line in file:
        text = line.strip()
        temp_score_counter_object = Game_round_part2(text)
        total_score_2 += temp_score_counter_object.score_returner()
print(total_score_2)
