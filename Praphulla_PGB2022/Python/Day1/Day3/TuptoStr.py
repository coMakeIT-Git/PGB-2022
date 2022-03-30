def conversion(lst):
    result = list(map(' '.join, lst))
    return result
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("\n List of colors:")
print(colors)
print("\n Converting List of Tuples into a List of Strings:")
print(conversion(colors))
