# Example 1:
#  - Input: 123
#  - Output: 321

# Example 2:
#  - Input: -123
#  - Output: -321

# Example 3:
#  - Input: 120
#  - Output: 21

def reverse(x):
    reversed = 0
    if x > 0:
        reversed = int(str(x)[::-1])
    if x < 0:
        reversed = int(str(x*-1)[::-1]) * -1
    
    if reversed >= 2**31-1 or reversed <= -2**31:
        return 0
    else:
        return reversed

print('max', 2**31-1)
print('min', -2**31)
reverse(123)
reverse(-123)
reverse(120)
reverse(1534236469)