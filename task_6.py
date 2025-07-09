types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
def match(dict1,dict2):
    tickets_by_type = {}
    for value1, value2 in zip(dict1.values(),dict2.values()):
        tickets_by_type[value1]=value2
    return tickets_by_type

def remove_duplicates(dict2):
    lst1 = [] # Новый пустой список для добавления value
    for key, value in dict2.items():
        lst2 = []  # Новый пустой список для value без дубликатов
        for i in value:
            if i not in lst1:
                lst1.append(i)  # Добавляем в список lst1
                lst2.append(i)  # Добавляем в список без дубликатов
        dict2[key] = lst2  # Обновляем словарь
    return dict2

def test(dict1,dict2):
    tickets_without_duplicates = remove_duplicates(dict2)
    tickets_by_type = match(dict1,tickets_without_duplicates)
    print(tickets_by_type)

test(types,tickets)