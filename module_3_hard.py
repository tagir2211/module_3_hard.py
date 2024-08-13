sum = 0


def calculate_structure_sum(list_):
    global sum
    for i in list_:
        if isinstance(i, int) or isinstance(i, float):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set) :
            calculate_structure_sum(i)  
        elif isinstance(i, dict):
            calculate_structure_sum(list(i.values())) + calculate_structure_sum(list(i.keys()))
    return sum


data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}), "Hello", ((),
[{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))