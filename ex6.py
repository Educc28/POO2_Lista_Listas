import statistics

lst = []
students = 0

studentsNumber = 3

for i in range(0, studentsNumber):
    for j in range(0, 4):
        grade = int(input("Insira uma nota: "))
        lst.append(grade)
    
    if statistics.mean(lst) >= 7:
        students = students + 1
    lst = []



print(students)