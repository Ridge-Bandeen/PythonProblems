import math


def nearest_polygonal_number(n, s):
    print(f'{n},{s}')
    exact = polygonal_number_i(n, s)
    lower_i = int(exact)
    lower = polygonal_number_at(s, lower_i)
    higher = polygonal_number_at(s, lower_i + 1)
    if higher - n < n - lower:
        return int(higher)
    return int(lower)


def polygonal_number_at(s, i):
    return (((s - 2) * (i ** 2)) - ((s - 4) * i)) // 2


def polygonal_number_i(n, s):
    return (math.sqrt((8 * n * (s - 2)) + ((s - 4) ** 2)) + s - 4) // (2 * (s - 2))


print(
    nearest_polygonal_number(
        188046518173444382120161023625158793197957154742584610447294908911002300690879870653574957 /
        73515104317349940728858535952141108476552063402512609301164235512, 100)
)
