test_cases = input()
nums_list = test_cases.split(r'\n')
for nums in nums_list:
    separated = nums.split(' ')
    if len(separated) == 2:
        first, second = separated
        res = int(first) ** int(second)
        print(f"{len(str(res))}")