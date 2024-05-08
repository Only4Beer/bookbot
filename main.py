def main ():
    
    with open("books/frankenstein.txt", "r") as f:
        contents = f.read()

        words = contents.split()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")

        contents_lower = contents.lower()

        character_counts = {}
        for character in contents_lower:
            if character.isalpha() == False:
                continue
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
        character_counts = dict(sorted(character_counts.items()))
        for character, count in character_counts.items():
            print(f"The \'{character}\' character was found {count} times")
        print("\n--- End report of books/frankenstein.txt ---\n")

    

if __name__ == "__main__":
    main()