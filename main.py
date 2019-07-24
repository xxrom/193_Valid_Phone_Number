import re

file = open("file.txt", "r")

text = file.read()
lines = text.split('\n')

# print(lines)

ans = []

for line in lines:
    found = re.search('^(\(\d{3}\) \d{4}-\d{4}$|\d{3}-\d{4}-\d{4})$', line)
    if found is not None:
        ans.append(line)
    # print(found)
# print('ans', ans)

fullLine = ''
for line in ans:
    fullLine += line + '\n'
print(fullLine)
# re.search('^(\d+)', log[1])

# file.write("This is our new text file")
# file.write("and this is another line.")
# file.write("Why? Because we can.")

file.close()
