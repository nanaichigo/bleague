a=[0,2,4,4,4,4,2,4,4,4,4,2,4,4,4,2]
b=[2,0,2,4,2,4,4,4,4,4,4,4,2,4,4,4]
c=[4,2,0,4,2,4,4,2,2,4,4,4,4,4,4,4]
d=[4,4,4,0,4,4,4,4,2,2,4,2,4,2,4,4]
e=[4,2,2,4,0,4,4,2,2,4,4,4,4,4,4,4]
f=[4,4,4,4,4,0,2,4,4,2,2,4,4,4,2,4]
g=[2,4,4,4,4,2,0,2,4,4,4,4,4,4,4,2]
h=[4,4,2,4,2,4,2,0,4,4,2,4,4,4,4,4]
i=[4,4,2,2,2,4,4,4,0,4,2,4,4,4,4,4]
j=[4,4,4,2,4,2,4,4,4,0,4,2,4,4,2,4]
k=[4,4,4,4,4,2,4,2,2,4,0,4,2,4,4,4]
l=[2,4,4,2,4,4,4,4,4,2,4,0,2,4,4,4]
m=[4,2,4,4,4,4,4,4,4,4,2,2,0,2,4,4]
n=[4,4,4,2,4,4,4,4,4,4,4,4,2,0,2,2]
o=[4,4,4,4,4,2,4,4,4,2,4,4,4,2,0,2]
p=[2,4,4,4,4,4,2,4,4,4,4,4,4,2,2,0]

import itertools
import statistics

all = itertools.combinations('abcdefghijklmnop', 8)

answer = 52
for x in all:
    x_games = []
    for t_i in range(8):
        tmp = eval(x[t_i])
        sum_tmp = 0
        for t_j in range(8):
            if t_i == t_j:
                continue

            match x[t_j]:
                case 'a':
                    sum_tmp += tmp[0]
                case 'b':
                    sum_tmp += tmp[1]
                case 'c':
                    sum_tmp += tmp[2]
                case 'd':
                    sum_tmp += tmp[3]
                case 'e':
                    sum_tmp += tmp[4]
                case 'f':
                    sum_tmp += tmp[5]
                case 'g':
                    sum_tmp += tmp[6]
                case 'h':
                    sum_tmp += tmp[7]
                case 'i':
                    sum_tmp += tmp[8]
                case 'j':
                    sum_tmp += tmp[9]
                case 'k':
                    sum_tmp += tmp[10]
                case 'l':
                    sum_tmp += tmp[11]
                case 'm':
                    sum_tmp += tmp[12]
                case 'n':
                    sum_tmp += tmp[13]
                case 'o':
                    sum_tmp += tmp[14]
                case 'p':
                    sum_tmp += tmp[15]

        x_games.append(sum_tmp)

    calc_game = statistics.mean(x_games)
    if calc_game <= answer:
        print(x,calc_game,x_games)
        answer = calc_game
            

