def normalize_coordinates(coords):
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    shift_x = -min_x if min_x < 0 else 0
    shift_y = -min_y if min_y < 0 else 0
    return [(x + shift_x, y + shift_y) for x, y in coords]

coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
print(normalize_coordinates(coords))
