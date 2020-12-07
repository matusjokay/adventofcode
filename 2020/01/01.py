nums = [int(line) for line in open('input.txt')]
s = 0
for i in range(0,len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(f'{nums[i]*nums[j]}')
        for k in range(j+i, len(nums)):
            if nums[i]+nums[j]+nums[k] == 2020:
                print(f'{nums[i]*nums[j]*nums[k]}')
    
