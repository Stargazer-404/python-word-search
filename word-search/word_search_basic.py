def wordSearch(sentences):
    """
    Search for user-provided word(s) in a list of sentences.
    Sentences are matched only if ALL search words are present.
    Results are sorted by number of occurrences (highest first).
    """

    # Take input from user and convert to lowercase
    user_input = input("Enter the words to be searched: ").lower()

     # Split input into individual words
    user_words = user_input.split()

    # Handle empty input
    if not user_words:
        print("\nNo Match Found")
        return


    results = []
    for sentence in sentences:
        # Convert sentence into list of words (lowercase)
        sentence_word = sentence.lower().strip().split()
        
        # Check if ALL user words are present in the sentence
        if all(word in sentence_word for word in user_words):
            # Count total occurrences of search words in sentence
            total_occ = sum(sentence_word.count(word) for word in user_words)
            results.append((total_occ,sentence))
        
    if results:
        print(f"{len(results)} matched found\n ")
         # Sort results by number of occurrences (descending order)
        results.sort(key=lambda x:x[0],reverse=True)
        for occ,res in results:
            print(f"- {res}")# Display matched sentence

    pass

def main():
    # Sample sentences to search from
    sentences = ["this is good", "python is good", "python is not python snake"]
    wordSearch(sentences)

if __name__ == "__main__":
    main()
