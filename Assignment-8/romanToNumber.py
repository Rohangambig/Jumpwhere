def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in s[::-1]:
        curr = roman[c]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

s = input("Enter a Roman numeral: ")
print(roman_to_int(s))
