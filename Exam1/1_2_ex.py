#1 ~ 10 까지의 정수에서 2의 배수와 3의 배수 정수의 합을 구하시오.
sum = 0

for k in range(1, 11):
    if k % 2 == 0 or k % 3 ==0:
        sum += k

print('2와 3 배수의 정수의 합 :', sum)
