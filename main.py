def dist_between_two_points(x1, y1, x2, y2):
    """Возвращает расстояние между двумя точками"""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def full_path_calc(routes):
    """ Возвращает таблицу с расстоянием из каждой начальной точки списка
        в каждую конечную точку списка """
    res = 0
    for i in range(len(routes) - 1):
        res += dist_between_two_points(*routes[i], *routes[i + 1])
    return res


def postman_print(routes):
    """Устанавливает формат вывода"""
    res = 0
    distances = []

    for i in range(len(routes) - 1):
        res += dist_between_two_points(*routes[i], *routes[i + 1])
        distances.append(res)
    print(
        f"{routes[0]} -> "
        f"{routes[1]}[{distances[0]}] -> "
        f"{routes[2]}[{distances[1]}] -> "
        f"{routes[3]}[{distances[2]}] -> "
        f"{routes[4]}[{distances[3]}] -> "
        f"{routes[5]}[{distances[4]}] = {distances[4]}")


def postman(start, locations):
    """Рассчитывает минимально возможный маршрут"""
    res_list = []
    res_distance = -1
    for i in range(0, 4):
        j_copy = locations[:i] + locations[i + 1:]
        for j in range(len(j_copy)):
            k_copy = j_copy[:j] + j_copy[j + 1:]
            for k in range(len(k_copy)):
                compare_list = [start, locations[i], j_copy[j], k_copy[k], k_copy[1 - k], start]
                compare_distance = full_path_calc(compare_list)
                if res_distance == -1 or compare_distance < res_distance:
                    res_list = compare_list[:]
                    res_distance = compare_distance
    postman_print(res_list)


postal_office = (0, 2)
elem_1 = (2, 5)
elem_2 = (5, 2)
elem_3 = (6, 6)
elem_4 = (8, 3)

postman(postal_office, [elem_1, elem_2, elem_3, elem_4])
