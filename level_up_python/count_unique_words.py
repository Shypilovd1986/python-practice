"""Module helps to find top words in text"""

import collections


def count_unique_words(path_file, count_words):
    """ takes two arguments path to file and counts finding top words"""
    with open(path_file, "r", encoding="UTF=8") as file:
        text = file.read()
        list_of_all_words = text.split()
        list_of_all_words = [word.upper() for word in list_of_all_words]

        print(f"Total words in file : {len(list_of_all_words)}")

        words_counts = collections.Counter(list_of_all_words)
        print("Top 20 words: ")
        for word in words_counts.most_common(count_words):
            print(f"{word[0]}\t {word[1]}")


if __name__ == "__main__":
    count_unique_words("good_day.txt", 5)
