data="""....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

lines = data.splitlines()

rows = [list(char) for char in lines]



pattern = "XMAS"
backwards_pattern = "SAMX"

pattern_match = 0

def horrizontal_check(dataset):
    matches = 0
    for i in dataset:
        for j in range(len(i) - 3):
            result = ''.join(i[j:j+4])
            if result == pattern:
                matches += 1
 
        for j in range(len(i) - 1, 2, -1):
            result_backwards = ''.join(i[j-3:j+1])
            print(result_backwards)
            if result_backwards == backwards_pattern:
                matches += 1
    
    return matches
pattern_match = horrizontal_check(rows)


print(pattern_match)