import math

def pythogor(katet, hypotenuse): # Функция высчитывающая 2-ой катет треугольника
    return math.sqrt(hypotenuse**2 - katet**2)


def tour(friends, friend_towns, home_to_town_distances):

    dict_friend_towns = dict(friend_towns)  # Создание копий входных данных
    friends_copy = friends.copy()

    for town in dict_friend_towns.copy(): # Удоление лишних городов
        if town not in friends:
            del dict_friend_towns[town]

    for friend in friends: # Удоление лишних друзей
        if friend not in dict_friend_towns:
            friends_copy.remove(friend)

    # Записываем в результат расстояния от дома до 1-го друга
    result = home_to_town_distances[dict_friend_towns[friends_copy[0]]]

    for i in range(len(friends_copy)-1): # Проходим по друзья
        katet = home_to_town_distances[dict_friend_towns[friends_copy[i]]]
        hypotenuse = home_to_town_distances[dict_friend_towns[friends_copy[i+1]]]
        result += pythogor(katet, hypotenuse)

    # Добовляем к результату расстояния от последнего друга до дома
    result += home_to_town_distances[dict_friend_towns[friends_copy[-1]]]

    return math.floor(result)

if __name__ == "main":

    friends8 = ["B1", "B2", "B5", "B6"]
    fTowns8 = [["B1", "Y1"], ["B2", "Y2"], ["B3", "Y3"], ["B4", "Y4"], ["B5", "Y5"]]
    distTable8 =  {"Y1": 60.0, "Y2": 80.0, "Y3": 100.0, "Y4": 110.0, "Y5": 150.0}

    test = tour(friends8, fTowns8, distTable8)
    print(test)
