class Power:
    def my_pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

power = Power()
x = float(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))
print(power.my_pow(x, n))
