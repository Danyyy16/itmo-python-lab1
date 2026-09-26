
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

s = 4
w = 4 * s + 1
h = 2 * s + 1

for y in range(h):
    for x in range(w):
        dx = x % (2 * s) - s
        dy = y - s
        if abs(dx) + abs(dy) == s:
            print(BLUE + '  ', end='')
        else:
            print(WHITE + '  ', end='')
    print(END)
