SentenceNumber = input("Enter the sentence number: ")
SentenceNumber = int(SentenceNumber)

with open("Sentences") as fp:
    for i, line in enumerate(fp):
        if i == SentenceNumber:
            print(line)
            break
