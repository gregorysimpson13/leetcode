def myAtoi(s: str) -> int:
    #s = str
    start_int = 0
    sign = 1
    result = 0
    int_max, int_min = (2**31) - 1, -2**31
    for i in range(len(s)):
        if s[i] == '-':
            sign = -1
            start_int = i+1
            break
        if s[i] == '+':
            start_int = i+1
            break
        if s[i].isnumeric():
            start_int = i
            break
        if s[i] == " ":
            continue
        return 0
    for i in range(start_int, len(s)):
        if not s[i].isnumeric():
            break
        result = result * 10
        result = result + int(s[i])
    result = result * sign
    print(result > int_max)
    if result > int_max:
        return int_max
    if result < int_min:
        return int_min
    return result




print(myAtoi("   -42"),-42)
print(myAtoi("42"),42)
print(myAtoi("4193 with words"),4193)
print(myAtoi("words 4193"),0)
print(myAtoi("23002489025232947249249"),2147483647)



