import random
import sys

def create_tree(n, file):
    teams = [[]]
    for i in range(1, n + 1):
        teams[0].append("Team" + str(i))

    i = 1
    while len(teams[-1]) > 1:
        teams.append([])
        for j in range(0, len(teams[i - 1]), 2):
            teams[i].append(teams[i - 1][j] if random.choice([True, False]) else teams[i - 1][j + 1])
        i += 1

    mapped = []
    for i in range(len(teams)):
        mapped.append([])
        for team in teams[i]:
            mapped[i].append((i, team))

    for i in range(len(mapped) - 1, 0, -1):
        j = 1
        for k in mapped[i]:
            mapped[i - 1].insert(j, k)
            j += 2

    if file is not None:
        with open(file, "w") as fout:
            for item in mapped[0]:
                if item[0] == 0:
                    fout.write(" " * 20 * item[0] + item[1] + (3 - (len(item[1]) - 5)) * "-" + "|\n")
                elif item[0] == 1:
                    fout.write(" " * 8 * item[0] + "|--->" + item[1] + (11 - len(item[1])) * "-" + "|\n")
                else:
                    fout.write(" " * ((16 * item[0]) - 8) + "|--->" + item[1] + (11 - len(item[1])) * "-" + "|\n")
    else:
        for item in mapped[0]:
            if item[0] == 0:
                print(" " * 20 * item[0] + item[1], end="")
                print((3 - (len(item[1]) - 5)) * "-" + "|")
            elif item[0] == 1:
                print(" " * 8 * item[0] + "|--->" + item[1], end="")
                print((11 - len(item[1])) * "-" + "|")
            else:
                print(" " * ((16 * item[0]) - 8) + "|--->" + item[1], end="")
                print((11 - len(item[1])) * "-" + "|")


create_tree(int(sys.argv[1]),sys.argv[2])