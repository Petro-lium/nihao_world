#Практикум яндекс
#Готовим завтрак. Можно приготовить хлопья с молоком (молоко, хлопья), можно яичницу (яйца), 
#а можно омлет (молоко и яйца). Есть и более бюджетные варианты.

milk = False
cereals = True
eggs = not False

if milk or cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'

print('Сегодня на завтрак', breakfast)