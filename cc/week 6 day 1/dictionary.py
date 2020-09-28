class Dictionary:
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic.keys():
                return [i,dic[target-nums[i]]]
            dic[nums[i]] = i