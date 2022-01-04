numCount = int(input())
stringNums = input().split(' ')
nums = [int(num) for num in stringNums]
first_2_same = False
evenness = False
sum_of_first_2 = nums[0] + nums[1]
sum_of_first_3 = sum_of_first_2 + nums[2] 
if (sum_of_first_2 % 2 == 0):
    if (nums[0] % 2 == 0):
        evenness = True
else:
    if (sum_of_first_3 % 2 == 1):
       evenness = True 
if evenness:
    offsett = 1
else:
    offsett = 0
for index in range(numCount):
    if (nums[index] % 2 == offsett):
        print(index + 1)
