import os

WHITE = '\u001b[47m'
RED = '\u001b[41m'
BLACK = '\u001b[40m'
END = '\u001b[0m'

os.system('cls')

h = 12
w = 6

picture = ''
for y in range(h, -1, -1):
    for col in range(w + 1):
        x = col - 1
        if col == 0 or y == 0:
            picture += BLACK + '  '
        elif 3 * x <= y < 3 * (x + 1):
            picture += RED + '  '
        else:
            picture += WHITE + '  '
    picture += END + '\n'

print(picture)
