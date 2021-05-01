def generate_squares(inter):
    dict = {}
    i = 1
    while i <= inter:
        dict[i] = i ** 2
        i += 1
    return dict

print(generate_squares(5))
