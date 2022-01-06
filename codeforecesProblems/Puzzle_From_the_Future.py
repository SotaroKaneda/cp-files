test_num = int(input())
while test_num:
    test_num -= 1
    n = int(input())
    a = ['0'] * n
    b = input()
    last_digit = 0
    for i in range(n):
        #if the sum is odd and last digit is non-zero
        if (int(b[i]) + last_digit) % 2 == 1 and last_digit != 0:
            a[i] = '0'
        else:
            a[i] = '1'
        last_digit = int(b[i]) + int(a[i])
    print(''.join(a))
