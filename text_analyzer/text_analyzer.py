def analyze_text(text):

    words_list = text.split()
    words = len(words_list)
    total_chars = 0
    sentences = 0
    vowels = 0
    consonants = 0

    for ch in text:
        
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            total_chars += 1
            if ch in 'aeiouAEIOU':
                vowels += 1
            else:
                consonants += 1
        elif ch in '.!?':
            sentences += 1

    
    print("\n=== Text Analysis Result ===")
    print("Total words in text:", words)
    print("Total characters in text:", total_chars)
    print("Total sentences in text:", sentences)
    print("Total vowels in text:", vowels)
    print("Total consonants in text:", consonants)

    
    search_word = input("\nEnter a word to find: ").strip()

    count = 0
    positions = []

    for i in range(len(words_list)):
        if words_list[i].strip(".,!?").lower() == search_word.lower():
            count += 1
            positions.append(i + 1)  

    
    print("\n=== Word Search Result ===")
    if count == 0:
        print(f"'{search_word}' not found in text.")
    else:
        print(f"'{search_word}' found {count} time(s) at position(s): {positions}")


if __name__ == "__main__":
    text = input("Enter text: ")
    analyze_text(text)
