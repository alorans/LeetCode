class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Use indicies dictionary (hash table) to store numbers to indicies
        indicies = {}

        # Iterate through nums list
        for i, num in enumerate(nums):
            # Get other necessary addend
            difference = target - num

            # If we already have the indice of difference, return
            if difference in indicies:
                return [i, indicies[difference]]
            
            # Otherwise, append the current number's indice to the dictionary
            else:
                indicies[num] = i
        