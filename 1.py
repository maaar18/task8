def main():
    number = int(input("Введите число:"))
    base = int(input("Введите систему счисления:"))
    
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