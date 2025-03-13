SentenceNumber = input("Enter the sentence number: ")
SentenceNumber = int(SentenceNumber)

with open("Sentences.txt", encoding="utf-8") as fp:
    for i, line in enumerate(fp):
        if i == SentenceNumber:
            print(line)
            break
