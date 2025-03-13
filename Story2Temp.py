import re


Story = open("Story.txt", "r", encoding='utf-8')
Temp = open("temp.txt", "w", encoding='utf-8')


story = Story.read()


# for line in story:
#     i = 0
#     while i < len(line):
#         a = (i + 3) < len(line);
#         if a and line[i:i+3] in ['Mr.', 'Ms.', 'Dr.', '...']:
#             Temp.write(line[i:i+3])
#             i += 3
#         elif ((i+4)<len(line)) and line[i:i+4] in ['Mrs.']:
#             Temp.write(line[i:i+4])
#             i += 4
#         elif line[i] == '\"':
#             Temp.write(line[i])
#             i+=1

#         elif line[i] in ['.', '?', '!']:
#             Temp.write(line[i] + '\n')
#             i += 1
#         else:
#             Temp.write(line[i])
#             i += 1

i = 0
j = 0
while j < 2:
    while i < len(story):
        if (i + 3) < len(story) and story[i:i+3] in ['Mr.', 'Ms.', 'Dr.', '...']:
            Temp.write(story[i:i+3])
            i += 3
        elif (i + 4) < len(story) and story[i:i+4] in ['Mrs.']:
            Temp.write(story[i:i+4])
            i += 4
        elif (i + 1) < len(story) and story[i:i+2] == "\n\n":
            Temp.write("\n")
            i += 2
        elif story[i] == '\"':
            Temp.write(story[i])
            i += 1
        elif story[i] in ['.', '?', '!']:
            Temp.write(story[i] + '\n')
            i += 1
        else:
            Temp.write(story[i])
            i += 1
    j += 1


Story.close()
Temp.close()

