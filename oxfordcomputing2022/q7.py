string = input()

out = ''

i = 1
last_char = string[0]
num_of = 1
while i < len(string):
    if string[i] == last_char:
        num_of += 1
    else:
        out += last_char + str(num_of)
        num_of = 1
        last_char = string[i]
    i += 1

print(out + last_char + str(num_of))
