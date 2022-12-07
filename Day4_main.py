# Dag 4 program

# Läs in varje rad
# Kolla om första mindre än andra, isåfall kolla om andra mindre än första.
class Method_3():
    def __init__(self, string):
        self.ranges = string.split(',')
        self.range1 = self.ranges[0].split('-')
        self.range2 = self.ranges[1].split('-')
        self.range = self.range1 + self.range2
        self.range[3] = self.range[3].strip()   # Tar bort radslutet
        for index in range(len(self.range)):
            self.range[index] = int(self.range[index])

    def score_counter(self):
        if self.range[0] >= self.range[2] and self.range[1] <= self.range[3]:
            return 1

        elif self.range[0] <= self.range[2] and self.range[1] >= self.range[3]:
            return 1

        else:
            return 0

with open('Day4_input.txt') as file:
    total_score = 0
    for line in file:
        temp_object = Method_3(line)
        total_score += temp_object.score_counter()
    print(total_score)



### Part 2

class Method_3():
    def __init__(self, string):
        self.ranges = string.split(',')
        self.range1 = self.ranges[0].split('-')
        self.range2 = self.ranges[1].split('-')
        self.range = self.range1 + self.range2
        self.range[3] = self.range[3].strip()   # Tar bort radslutet
        for index in range(len(self.range)):
            self.range[index] = int(self.range[index])

    def score_counter(self):
        if self.range[0] >= self.range[2] and self.range[1] <= self.range[3]:
            return 1

        elif self.range[0] <= self.range[2] and self.range[1] >= self.range[3]:
            return 1

        elif self.range[0] >= self.range[2] and self.range[0] <= self.range[3]:  # Runt 0
            return 1

        elif self.range[0] <= self.range[2] and self.range[1] >= self.range[2]:  # runt 2
            return 1

        elif self.range[1] >= self.range[2] and self.range[1] <= self.range[3]:  # runt 1
            return 1

        elif self.range[0] <= self.range[3] and self.range[1] >= self.range[3]:  # runt 3
            return 1

        else:
            return 0

with open('Day4_input.txt') as file:
    total_score = 0
    for line in file:
        temp_object = Method_3(line)
        total_score += temp_object.score_counter()
    print(total_score)






exit()



#### Allt nedanför är skit..... varför????









class Method_2():
    def __init__(self, string):
        self.ranges = string.split(',')
        self.range1 = self.ranges[0].split('-')
        self.range2 = self.ranges[1].split('-')
        self.range = self.range1 + self.range2
        self.range[3] = self.range[3].strip()   # Tar bort radslutet

    def score_counter(self):
        if self.range[0] >= self.range[2] and self.range[1] <= self.range[3]:
            return 1

        elif self.range[0] <= self.range[2] and self.range[1] >= self.range[3]:
            return 1

        else:
            return 0

master_list = []
with open('Day4_input.txt') as file:
    total_score = 0
    for line in file:
        temp_object = Method_2(line)
        total_score += temp_object.score_counter()
        master_list.append(temp_object.score_counter())
    print(total_score)


class Line_checker():

    def __init__(self, string):
        self.ranges = string.split(',')
        self.range1 = self.ranges[0].split('-')
        self.range2 = self.ranges[1].split('-')

    def compare_method(self):

        if int(self.range1[0]) <= int(self.range2[0]):  # Om range 1 har mindre start och större slut omsluter den range 2
            if int(self.range1[1]) >= int(self.range2[1]):
                return 1
            else:
                return 0

        if int(self.range1[0]) >= int(self.range2[0]):  # Om range 2 har mindre start och större slut omsluter den range 1
            if int(self.range1[1]) <= int(self.range2[1]):
                return 1
            else:
                return 0

        else:
            return 0






class Line_checker():

    def __init__(self, string):
        self.ranges = string.split(',')
        self.range1 = self.ranges[0].split('-')
        self.range2 = self.ranges[1].split('-')

    def compare_method(self):


        if int(self.range1[0]) <= int(self.range2[0]):  # Om range 1 har mindre start och större slut omsluter den range 2
            if int(self.range1[1]) >= int(self.range2[1]):
                return 1
            else:
                return 0

        if int(self.range1[0]) >= int(self.range2[0]):  # Om range 2 har mindre start och större slut omsluter den range 1
            if int(self.range1[1]) <= int(self.range2[1]):
                return 1
            else:
                return 0

        else:
            return 0
truth = []
with open('Day4_input.txt') as file:
    total_score = 0
    counter = 0
    for line in file:
        temp_object = Line_checker(line)
        total_score += temp_object.compare_method()
        counter += 1
    print(total_score)







