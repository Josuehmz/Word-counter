def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    question = "What are you thinking about?\n"
    user_input = input(question).strip()
    num_words = count_words(user_input)
    print(f"Great, you've shown me your thoughts in {num_words} words!")

if __name__ == "__main__":
    main()