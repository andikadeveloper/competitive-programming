# Input
s = "III"

# Process
data = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

output = 0
count = 0

while count < len(s):
    current_roman = s[count]
    next_roman = s[count + 1] if count < len(s) - 1 else current_roman
    
    if data[current_roman] >= data[next_roman]:
        output += data[current_roman]
        count += 1
    else:
        diff = data[next_roman] - data[current_roman]
        output += diff
        count += 2
        
# Output
print(output)