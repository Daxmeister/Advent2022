# Dag 1

file = open("Day1_input.txt", 'r')
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