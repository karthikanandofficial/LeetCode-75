class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pos = 0

        for read_pos in range(len(nums)):
            if nums[read_pos] != 0:
                nums[write_pos], nums[read_pos] = nums[read_pos], nums[write_pos]
                write_pos += 1
