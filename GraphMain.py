"""
Source: Claude
"""




import matplotlib.pyplot as plt


def count_string_occurrences(text, target):
    # Split the text into paragraphs
    paragraphs = text.split('\n')
    # Count occurrences in each paragraph
    counts = [paragraph.lower().count(target.lower()) for paragraph in paragraphs]
    return counts


def create_frequency_graph(counts, search_string):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(counts) + 1), counts, marker='o')
    plt.title(f'Frequency of "{search_string}" throughout the text')
    plt.xlabel('Paragraph Number')
    plt.ylabel('Number of Occurrences')
    plt.grid(True)
    plt.show()


def main():
    # Read the story file
    try:
        with open('Sentences.txt', 'r', encoding='utf-8') as file:
            story_text = file.read()
    except FileNotFoundError:
        print("Error: Story.txt not found!")
        return
   
    # Get search string from user
    search_string = input("Enter the string to search for: ")
   
    # Count occurrences
    occurrences = count_string_occurrences(story_text, search_string)
   
    # Create and display the graph
    create_frequency_graph(occurrences, search_string)
   
    # Print total occurrences
    total = sum(occurrences)
    print(f'\nTotal occurrences of "{search_string}": {total}')


if __name__ == "__main__":
    main()

