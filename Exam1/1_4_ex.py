# 두개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하는 프로그램을 작성하시오.
for i in range(1, 7):
    for j in range(1, 7):

        tot = i + j

        if tot == 6:
            print('첫번째 주사위 : %d, 두번째 주사위 : %d' %(i, j))