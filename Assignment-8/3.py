class SubsetGenerator:
    def unique_subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

generator = SubsetGenerator()
nums = [4, 5, 6]
print(generator.unique_subsets(nums))
