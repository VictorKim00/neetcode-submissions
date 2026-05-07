class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i in range(len(nums)):
            current = nums[i]
            need = target - current
            if need in prev_map:
                return [prev_map[need], i]
            prev_map[current] = i