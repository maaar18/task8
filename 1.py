def main():
    number = input("Введите число:")
    try:
       number = int(number)
    except ValueError:
       print("Ошибка")
       exit()    
    base = input("Введите систему счисления:")
    try:
       base = int(base)
    except ValueError:
       print("Ошибка")
       exit()    
    
    print(to_base(number, base))
    
    
def to_base(number, base):
    if number < base:
        return str(number)
    
    converted = []
    
    while number >= base:
        converted.append(str(number % base))
        number = number // base
        
    converted.append(str(number))
    
    return ''.join(converted[::-1])


if __name__ == '__main__':
    main()