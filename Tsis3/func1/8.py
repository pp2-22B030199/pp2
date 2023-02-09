def spy_game(nums):
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] == 0:
                    for x in range(j + 1, len(nums)):
                        if (nums[x] == 7):
                            return True


nums = input().split()

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

if spy_game(nums) == True:
    print("True")
else:
    print("False")