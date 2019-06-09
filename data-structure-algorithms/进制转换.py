# coding=utf-8
# switch between binary ,hex,oct
def switch(num, source, target):
    if source == 10 and target == 2:
        return bin(num)
    elif source == 2 and bin == 10:
        return int(num, 2)
    elif source == 10 and target == 16:
        return hex(num)
    elif source == 16 and target == 10:
        return int(num, 16)
    elif source == 16 and target == 2:
        return bin(num)
    elif source == 10 and target == 8:
        return oct(num)
    if source == 2 and target == 16:
        return hex(num)


if __name__ == '__main__':
    hextobin = switch(0x18af7,16,2)
    bintohex = switch(0b010111101,2,16)
    print(hextobin)
    print(bintohex)