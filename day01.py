file = open("input", "r")
data = file.read()
file.close()

result = []
for block in data.split("\n\n"):
    result.append(sum(list(map(lambda x: int(x.strip()), block.split("\n")))))
print(sum(sorted(result, reverse=True)[0:3]))