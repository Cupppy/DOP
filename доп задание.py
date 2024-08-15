a = int(input('сколько учеников у вас есть?'))
grades=[]
students=[]
summ=0
for i in range(a):
    students.append(input('введите имя ученика'))
    g=input('введите его оценки через запятую, без пробелов')
    d=g.split(',')
    grades.append(d)
for i in range(a):
    for h in range(len(grades[i])):
        u=int(grades[i][h])
        summ+=u
    print(students[i],'средний балл-',summ/len(grades[i]))


