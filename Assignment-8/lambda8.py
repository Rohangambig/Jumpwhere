validate = lambda s: "valid string" if any(c.islower() for c in s) and any(c.isupper() for c in s) and any(c.isdigit() for c in s) and len(s) >= 10 else "invalid string"

print(validate("PaceWisd0m"))
