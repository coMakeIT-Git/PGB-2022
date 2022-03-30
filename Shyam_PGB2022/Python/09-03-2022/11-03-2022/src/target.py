class target:
    def targetpair(nums, targex):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == targex:
                    print('Pair found', (nums[i], nums[j]))
                    return
        print('No pair found')

nums = [10, 20, 10, 40, 50, 60, 70]
targex = 50
target.targetpair(nums, targex)
