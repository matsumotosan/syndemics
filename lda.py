from pathlib import Path

import gensim
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

text_dir = "./parsed"


def main():
    # Get parsed text files
    path_text = Path(text_dir)
    files = [f for f in path_text.iterdir() if f.is_file()]

    docs = []
    for file in files:
        with open(file, "r") as f:
            docs.append(f.read())

    # Split the documents into tokens.
    tokenizer = RegexpTokenizer(r"\w+")
    for idx in range(len(docs)):
        docs[idx] = docs[idx].lower()  # Convert to lowercase.
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

    # Remove numbers, but not words that contain numbers.
    docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

    # Remove words that are only one character.
    docs = [[token for token in doc if len(token) > 1] for doc in docs]


if __name__ == "__main__":
    main()
