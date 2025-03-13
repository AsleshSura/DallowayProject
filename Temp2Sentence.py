Temp = open("Temp.txt", "r", encoding='utf-8')
Sentences = open("Sentences.txt", "w", encoding='utf-8')

temp = Temp.read()

lines = temp.splitlines()
filtered = [
    line
    for line in lines
    if line.strip()
]
Sentences.write('\n'.join(filtered))

Temp.close()
Sentences.close() 