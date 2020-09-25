import re

if __name__ == '__main__':
    file = open('regex_sum_746562.txt', 'r')
    lines = file.read()
    numbers = re.findall('[0-9]+', lines)
    result = 0
    for number in numbers:
        result = result + int(number)
    print(result)
