# Dag 1 del 1

'''file = open("Day1_input.txt", 'r')
highest_calorie = 0 # Håller kolla på maxvärdet
current_calorie = 0 # Håller koll på nuvarande elfs kalorimängd

for row in file:
    if row == "\n": # Hit kommer vi när vi byter elf, dvs vid tom rad

        if current_calorie > highest_calorie:   # Om det är nytt rekord mmärker vi det som nytt highest
            highest_calorie = current_calorie
            current_calorie = 0 # Nollställer

        else:
            current_calorie = 0 # Nollställer nuvarande elf räkningen

    else:   # När vi inte har kommit till en ny elf adderar vi fortsatt alla kalorier
        row.strip()
        current_calorie += int(row) # Adderar till listan

print(highest_calorie)
file.close()
'''
################################################################################################################
# Dag 1 del 2
################################################################################################################

# Skapar en klass som håller koll på de tre högsta värden
class ELf_list():

    # Skapas med tre värden, kommer alltid att ha tre värden.
    def __init__(self):
        self.list = [0, 0, 0]

    # Funktion som hittar det minsta talet. OBS att minsta talet måste vara mindre än 1 miljon.
    def return_smallest_number(self):
        smallest_number = 1000000
        for item in self.list:
            if item < smallest_number:
                smallest_number = item
        return smallest_number

    # Input är ett värde som ska ersätta minsta talet. Ersätter minsta talet med detta. Kollar INTE att värdet är mindre.
    # Detta måste man göra utanför programmet. Denna kommer bara ersätta minsta talet i listan med value.
    def substitute_smallest_number(self, value):
        smallest_value = self.return_smallest_number()
        for index in range(len(self.list)):
            if self.list[index] == smallest_value:
                self.list[index] = value
                break

    # Printar summan av de tre värdena.
    def print_sum(self):
        print (self.list[0] + self.list[1] + self.list[2])


file = open("Day1_input.txt", 'r')
high_calorie_elfs = ELf_list()  # Skapar ett objekt
current_calorie = 0 # Håller koll på nuvarande elfs kalorimängd


for row in file:
    if row == "\n": # Hit kommer vi när vi byter elf, dvs vid tom rad

        if current_calorie > high_calorie_elfs.return_smallest_number():   # Kollar om värdet är större än tredjehögsta
            high_calorie_elfs.substitute_smallest_number(current_calorie)   # Ersätter med lägsta värdet
            current_calorie = 0 # Nollställer vad nuvarande elf har

        else:
            current_calorie = 0 # Nollställer nuvarande elf räkningen

    else:   # När vi inte har kommit till en ny elf adderar vi fortsatt alla kalorier
        row.strip()
        current_calorie += int(row) # Adderar värdet till den nuvarande elfens totala kaloriintag

high_calorie_elfs.print_sum()
file.close()
