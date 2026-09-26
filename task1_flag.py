
WHITE = '\u001b[47m'
RED = '\u001b[41m'
END = '\u001b[0m'

width = 30
height = 20
cx = 14.5
cy = 9.5
r = 6

for y in range(height):
    for x in range(width):
        if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
            print(RED + '  ', end='')
        else:
            print(WHITE + '  ', end='')
    print(END)
