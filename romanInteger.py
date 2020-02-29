# Symbol       Value
# I             1
# I             2
#  - IV            4
# V             5
# IX            9
# X             10
# XII           12
# XXII          22
# XXVII         27
#  - XL         40
# L             50
# XC            90
# C             100
# CD            400
# D             500
# CM            900
# M             1000

def romanToInteger (s):
    romanChars = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    
    sequence = []
    result = 0
    
    for i in range(len(s) - 1):
        current = s[i] #roman char
        if current in romanChars: # exists in map
            if romanChars[current] < romanChars[ s[i+1] ]: # 뒷글자와 비교
                print('in map', romanChars[current])
                result -= romanChars[current]
            else:
                result += romanChars[current]
    result += romanChars[ s[len(s) - 1 ] ]
    return result

# romanToInteger("III")
romanToInteger("LVIII")

    