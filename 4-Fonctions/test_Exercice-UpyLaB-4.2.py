# Test case 1: Sunrise and sunset are different, current time is between them
assert soleil_leve(6, 18, 10) == True

# Test case 2: Sunrise and sunset are different, current time is not between them
assert soleil_leve(15, 8, 12) == False

# Test case 3: Sunrise and sunset are the same, both are not 12 or 0
assert soleil_leve(12, 12, 10) == False

# Test case 4: Sunrise and sunset are the same, both are 0
assert soleil_leve(0, 0, 22) == True