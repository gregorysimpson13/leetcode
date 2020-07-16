# mapper_function
def mapper_function(row, col):
    return ((row // 3) * 3) + (col // 3)

coords = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
for row, col in coords:
    print(mapper_function(row, col), end='\t')