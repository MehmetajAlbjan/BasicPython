def conver_base(number: str, from_base: int, to_base: int):
    digit = "0123456789ABCDEFGHJKLMNOPQRSTUVWXYZ"
    decimal = 0
    if (from_base <= 1 or from_base > 36 or to_base <= 1 or to_base > 36):
        return "ERROR"
    for char in number:
        if digit.index(char.upper()) >= from_base:
            return "ERROR"
        decimal = decimal * from_base + digit.index(char.upper())
    if decimal == 0:
        return "0"

    result = ""
    while decimal > 0:
        result = digit[decimal % to_base] + result
        decimal = decimal // to_base
    return result


print(conver_base("10", 10, 2))
print(conver_base("F", 4, 2))
print(conver_base("F", 16, 2))
print(conver_base("F",2,16))
