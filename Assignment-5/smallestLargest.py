def smallestLargest(string):
    arr = string.split(' ')

    min = float('inf')
    max = float('-inf')

    for words in arr:
        if len(words) > max: max = len(words)
        if len(words) < min: min = len(words)

    return {min,max}

print(smallestLargest('jumpwhere is an it company'))