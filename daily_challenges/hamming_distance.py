import math
def hammingDistance(x: int, y: int) -> int:
    digits = x if x > y else y
    digits = math.ceil(math.log(digits,2)) + 1
    format_string = "0:0{}b".format(digits)
    format_string = "{" + format_string + "}"
    x_str = format_string.format(x)
    y_str = format_string.format(y)
    print(x_str, y_str)
    distance = 0
    for i in range(len(x_str)):
        if x_str[i] != y_str[i]:
            distance = distance + 1
    return distance

def hammingDistance(x: int, y: int) -> int:
    if x == 0 and y == 0: return 0
    digits = math.ceil(math.log(max(x,y),2)) + 1
    format_string = "{{0:0{}b}}".format(digits)
    x_str, y_str = format_string.format(x), format_string.format(y)
    return len([(x,y) for x, y in zip(x_str, y_str) if x != y])


def hammingDistance(x: int, y: int) -> int:
    return len([b for b in bin(x^y) if b == '1'])

# my_nums = [1,2,3,4,5,6]
# x = sum(d+i for i in my_nums if i%2==0)
# print(x)

print(hammingDistance(13,111145))
print(hammingDistance(4,2))
print(hammingDistance(14,0))
print(hammingDistance(0,1))
print(hammingDistance(0,0))