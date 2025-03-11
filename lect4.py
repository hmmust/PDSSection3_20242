output = []
get_names = ("Ahmad"*i for i in range(1,6))
"""for n in get_names:
    output.append(n)
print(output)"""

print(list(get_names))
print([*get_names])
"""get_names2 = ["Ahmad"*i for i in range(1,6)]
print(get_names2)"""