# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        return Solution().Map(nums, target)
    def End2mid(self, nums, target):
        numList = []
        for n in range(len(nums)):
            numList.append( Num(n, nums[n]))
        sortedNums = sorted( numList, key=lambda num: num.value)
        start = 0
        end = len(nums) - 1
        while( start != end):
            if sortedNums[start].value + sortedNums[end].value == target:
                return sorted([sortedNums[start].index, sortedNums[end].index])
            elif sortedNums[start].value + sortedNums[end].value > target:
                end = end - 1
            else:
                start = start + 1
        return []
    def Map(self, nums, target):
        numMap = {}
        for n in range(len(nums)):
            if numMap.get(nums[n]) is not None:
                numMap[nums[n]] = [numMap[nums[n]], n + 1]
            else:
                numMap[nums[n]] = n + 1
        #print numMap
        for k in numMap.keys():
            if numMap.get(target - k) is not None:
                if numMap[k] == numMap[target - k]:
                    return sorted( numMap[k][:2])
                return sorted([numMap[k], numMap[target - k]])

class Num:
    def __init__(self, index, value):
        self.index = index + 1
        self.value = value
    def __repr__(self):
        return repr((self.index, self.value))

if __name__ == '__main__':
    nums = [1 , 2, 7, 11, 15, 1]
    target = 2
    print Solution().twoSum( nums, target)
