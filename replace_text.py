words = ["donkey", "bad", "gnda"]

with open("file.txt", "r") as f:
    content = f.read()
for word in words:
    contentNew = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(contentNew)
