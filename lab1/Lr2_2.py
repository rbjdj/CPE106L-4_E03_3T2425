import random

def getWords(filename):
    with open(filename, 'r') as file:
        return tuple(line.strip() for line in file)

def generateSentence(articles, nouns, verbs, prepositions):
    return f"{random.choice(articles).capitalize()} {random.choice(nouns)} " \
           f"{random.choice(verbs)} {random.choice(prepositions)} " \
           f"{random.choice(articles)} {random.choice(nouns)}."

def main():
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    prepositions = getWords("prepositions.txt")

    try:
        count = int(input("How many sentences do you want to generate? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nGenerated Sentences:\n")
    for _ in range(count):
        print(generateSentence(articles, nouns, verbs, prepositions))

if __name__ == "__main__":
    main()
