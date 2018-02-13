def reverse(x):
    sign = 1
    l = str(x)
    int_value_type = type(1)
    if l[0] == '-':
        sign = -1
        l = l[1:]

    string = "".join([x for x in reversed(l)])
    integer = int(string)
    
    return sign * integer if integer < 2147483647 else 0

print(reverse(1534236469))