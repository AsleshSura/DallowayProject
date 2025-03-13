import re


Story = open("Story.txt", "r", encoding='utf-8')
Sentences = open("Sentences.txt", "w", encoding='utf-8')


story = Story.read()


for line in story:
    i = 0
    while i < len(line):
        if len(line)-i >=4:
            if (line[i] == "M") and (line[i+1] == "r") and (line[i+2] == "."):
                Sentences.write(line[i] + line[i+1] + line[i+2])
                i += 3
            elif (line[i] == "M") and (line[i+1] == "r") and (line[i+2] == "s") and (line[i+3] == "."):
                Sentences.write(line[i] + line[i+1] + line[i+2] + line[i+3])
                i += 4
            elif (line[i] == "M") and (line[i+1] == "s") and (line[i+2] == "."):
                Sentences.write(line[i] + line[i+1] + line[i+2])
                i += 3
            elif (line[i] == "D") and (line[i+1] == "r") and (line[i+2] == "."):
                Sentences.write(line[i] + line[i+1] + line[i+2])
                i += 3
            elif line[i] in ['.', '?', '!']:
                Sentences.write(line[i] + '\n')
                i += 1
            else:
                Sentences.write(line[i])
                i += 1

           
        elif line[i] in ['.', '?', '!']:
            Sentences.write(line[i] + '\n')
            i += 1
        else:
            Sentences.write(line[i])
            i += 1


Story.close()
Sentences.close()

