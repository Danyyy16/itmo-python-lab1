
RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'

file = open('sequence.txt')
numbers = [float(line) for line in file]
file.close()

more = 0   
less = 0   
for n in numbers:
    if n < 0:
        if n > -5:
            more += 1
        elif n < -5:
            less += 1

total = more + less
more_p = round(more / total * 100)
less_p= round(less / total * 100)

print('больше -5:', RED + '  ' * (more_p // 2) + END, more_p, '%')
print('меньше -5:', BLUE + '  ' * (less_p // 2) + END, less_p, '%')
