import math

def pythogor(katet, hypotenuse):
    return math.sqrt(hypotenuse**2 - katet**2)


def tour(friends, friend_towns, home_to_town_distances):

    dict_friend_towns = dict(friend_towns)
    friends_copy = friends.copy()

    for town in dict_friend_towns.copy():
        if town not in friends:
            del dict_friend_towns[town]

    for friend in friends:
        if friend not in dict_friend_towns:
            friends_copy.remove(friend)

    result = home_to_town_distances[dict_friend_towns[friends_copy[0]]]

    for i in range(len(friends_copy)-1):
        katet = home_to_town_distances[dict_friend_towns[friends_copy[i]]]
        hypotenuse = home_to_town_distances[dict_friend_towns[friends_copy[i+1]]]
        result += pythogor(katet, hypotenuse)

    result += home_to_town_distances[dict_friend_towns[friends_copy[-1]]]

    return math.floor(result)


friends8 = ["B1", "B2", "B5", "B6"]
fTowns8 = [["B1", "Y1"], ["B2", "Y2"], ["B3", "Y3"], ["B4", "Y4"], ["B5", "Y5"]]
distTable8 =  {"Y1": 60.0, "Y2": 80.0, "Y3": 100.0, "Y4": 110.0, "Y5": 150.0}


x = tour(friends8, fTowns8, distTable8)
print(x)