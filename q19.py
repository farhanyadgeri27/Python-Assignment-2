# Q19 - Text Analysis Functions

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def count_words(text):
    words = text.split()
    return len(words)


def reverse_text(text):
    return text[::-1]


def longest_word(text):
    words = text.split()
    if len(words) == 0:
        return ""
    return max(words, key=len)


def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for word in words:
        # remove punctuation like commas or dots
        word = word.strip(".,!?")

        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def text_analysis():
    text = input("Enter a sentence: ")

    print("\n----- TEXT ANALYSIS RESULT -----")
    print("Total Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed Text:", reverse_text(text))
    print("Longest Word:", longest_word(text))

    print("\nWord Frequency:")
    freq = word_frequency(text)
    for word, count in freq.items():
        print(word, ":", count)


# Call main function
text_analysis()