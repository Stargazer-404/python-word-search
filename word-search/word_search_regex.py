import re

def wordSearch(sentences):
    user_input = input("Enter the word to be searched ").lower()
    user_words = user_input.split()

    if not user_words:
        print("No matched found")
    
    results = []
    for sentence in sentences:
        sentence_lower = sentence.lower()

        if all(re.search(rf"{re.escape(word)}",sentence_lower) for word in user_words):
            total_occ = sum(len(re.findall(rf"{re.escape(word)}",sentence_lower))for word in user_words)
            results.append((total_occ,sentence))
    
    if results:
        print(f"{len(results)} matched found")
        results.sort(key=lambda x:x[0],reverse=True)
        for occ,res in results:
            print(f"- {res}")
    else:
        print("No matched Found")
    

def main():
    # Sample sentences to search from
    sentences = ["this is good", "python is good", "python is not python snake"]
    wordSearch(sentences)

if __name__ == "__main__":
    main()