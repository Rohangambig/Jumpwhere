class PairFinder:
    def find_pair(self, numbers, target):
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return seen[diff], i
            seen[num] = i

finder = PairFinder()
numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50
print(finder.find_pair(numbers, target))
