import random

#количество бросков
rollCount = int(10)

# виртуальный бросок кубика
def diceRoll():
    return random.randint(0, 5)


#количество побед
def winCount(player, you):
    global rollCount
    win = int(0)
    for i in range(rollCount):
        if player[i] < you[i]:
            win+=1
    return win

#виртуальные кубики с числами на гранях
с1 = [3, 3, 3, 3, 3, 3]
c2 = [0, 0, 4, 4, 4, 4]
c3 = [1, 1, 1, 5, 5, 5]
c4 = [2, 2, 2, 2, 6, 6]
cubeOptions = ['кубик с тройками', 'кубик с нолями и четвёрками', 'кубик с единицами и пятёрками', 'кубик с двойками и шестёрками']
result = [[0 for i in range(rollCount)] for j in range(4)]

#перебераем по очереди все 4 кубика
for i in range(rollCount):
    result[0][i] = с1[diceRoll()]
    result[1][i] = c2[diceRoll()]
    result[2][i] = c3[diceRoll()]
    result[3][i] = c4[diceRoll()]

#виртуальная таблица побед
winResult = [[0 for i in range(4)] for j in range(4)]
winResult = [[winCount(result[i], result[j]) for i in range(4)] for j in range(4) if i != j]

selected = int(input('Какой кубик выбрал соперник: \n\n3 — ' + cubeOptions[0] + ' \n\n4 — ' + cubeOptions[1] + '\n\n5 — ' + cubeOptions[2] + '\n\n6 — ' + cubeOptions[3] + '\n\n'))
if selected != 3 and selected != 4 and selected != 5 and selected != 6:
    # если ввели не то, что нам нужно, — выводим сообщение
    print('Вы выбрали кубик, которого нет в условии')
maximum = int(0)
choose = int(0)
print(winResult)
for i in range(4):
    if winResult[selected - 3][i] > maximum:
        # то делаем это максимальным результатом
        max = winResult[selected - 3][i];
        # и запоминаем номер кубика, который показал наибольший результат
        choose = i;
print('Вам нужно выбрать ' + cubeOptions[choose]);



    
    




