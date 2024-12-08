import wikipedia
import random

# List of allowed languages
allowed_languages = [
    "ru",
    "uk",
    "be",
    "bg",
    "sr",
    "mk",
    "ky",
    "tg",
    "mn",
    "kk"
]

# Get random text/lang
random_language = allowed_languages[random.randint(0, len(allowed_languages) - 1)]
wikipedia.set_lang(str(random_language))
random_title = wikipedia.random()
    
# Function to get sentences from a random Wikipedia article
def get_random_sentences():
    # Fetch the content of the article
    try:
        page = wikipedia.page(title=random_title)
    except wikipedia.DisambiguationError as e:
        # Handle disambiguation pages by choosing the first option
        page = wikipedia.page(title=e.options[0])

    # Split the content into sentences
    sentences = page.content.split('. ')
    
    # Ensure we have at least x sentences
    if len(sentences) >= 5:
        return sentences[:5]
    else:
        return None

def main():
    # Get random sentences
    sentences = get_random_sentences()
    
    if sentences:
        print("List of available languages:\nRussian (ru)\nUkrainian (uk)\nBelarusian (be)\nBulgarian (bg)\nSerbian (sr)\nMacedonian(mk)\nKyrgyz (kz)\nTajik (tg)\nMongolian (mn)\nKazakh(kk)\n")
        # Display the sentences to the user
        for sentence in sentences:
            print(f"- {sentence.strip()}.")
        
        # Ask the user to guess the language
        guess = input("Guess the language: ").strip().lower()

        # Check if the guess is correct
        if guess == random_language:
            print("Your guess is correct! The article was " + random_language + ".wikipedia.org/wiki/" + random_title + ".")
        else:
            print("Sorry, your guess is incorrect. It was actually " + random_language + ", and the article was " + random_language + ".wikipedia.org/wiki/" + random_title + ".")
    else:
        print("Couldn't fetch sentences. Please try again.")

if __name__ == "__main__":
    main()
