def count_words_per_line(file_path):
    try:
        word_count_dict = {}

        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                word_count = len(line.split())  # Count words by splitting on whitespace
                word_count_dict[line_number] = word_count

        return word_count_dict

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# File path to your text dataclear
editions_file = '/Users/vedant/Desktop/Atgeir/HandsOn/Python/Assignments/AssignmentDay8/employee_data/Editions.txt'

# Call the function to count words per line
editions_word_counts = count_words_per_line(editions_file)

# Print the dictionary containing line numbers and word counts
if editions_word_counts is not None:
    print("Word counts per line:")
    for line_number, word_count in editions_word_counts.items():
        print(f"Line {line_number}: {word_count} words")
else:
    print("Failed to load editions data.")
