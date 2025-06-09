import requests

print("Welcome to the Dictionary App!")
print("Type 'exit' to close the app.\n")

while True:
    word = input("Enter a word: ")

    if word.lower() == 'exit':
        print("Goodbye! 👋")
        break

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meanings = data[0]['meanings']

        print(f"\nMeanings of '{word}':")
        for i, meaning in enumerate(meanings):
            definition = meaning['definitions'][0]['definition']
            print(f"{i+1}. {definition}")

            synonyms = meaning['definitions'][0].get('synonyms', [])
            if synonyms:
                print("   Synonyms:", ", ".join(synonyms))
        print()
    else:
        print("Word not found. Please try again.\n")