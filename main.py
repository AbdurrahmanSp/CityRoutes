def route(list):
    realRoute = []
    lenList = len(list)
    lenItem0 = len(list[0])
    for i in range(lenList):
        for j in range(lenItem0):
            if list[i][j] not in realRoute:
                realRoute.append(list[i][j])
    for i in realRoute:
        print(i + "-", end='')

cities = [
["Sarajevo", "Mostar"],
["Tuzla", "Zenica"],
["Mostar", "Konjic"],
["Zenica", "Banja Luka"],
["Konjic", "Tuzla"],
["Zavidovici", "Sarajevo"]
]

route(cities)
