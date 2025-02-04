from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

import nltk
from gensim.corpora import Dictionary
from gensim.models import HdpModel, Phrases
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

def preprocess(docs):
    # Split the documents into tokens.
    tokenizer = RegexpTokenizer(r"\w+")
    for idx in range(len(docs)):
        docs[idx] = docs[idx].lower()  # Convert to lowercase.
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

    # Remove numbers, but not words that contain numbers.
    docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

    # Remove words that are only one character.
    docs = [[token for token in doc if len(token) > 1] for doc in docs]

    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

    # Add bigrams and trigrams to docs (only ones that appear 20 times or more).
    bigram = Phrases(docs, min_count=20)
    for idx in range(len(docs)):
        for token in bigram[docs[idx]]:
            if "_" in token:
                # Token is a bigram, add to document.
                docs[idx].append(token)

    # Create a dictionary representation of the documents.
    dictionary = Dictionary(docs)

    # Filter out words that occur less than 20 documents, or more than 50% of the documents.
    dictionary.filter_extremes(no_below=20, no_above=0.5)

    return docs, dictionary

def main(args):
    # Download corpora
    nltk.download("wordnet")

    # Get parsed text files
    path_text = Path(args.text_dir)
    files = [f for f in path_text.iterdir() if f.is_file()]

    docs = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            docs.append(f.read())

    docs, dictionary = preprocess(docs)

    # Bag-of-words representation of the documents.
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    _ = dictionary[0]
    id2word = dictionary.id2token

    # Basic statistics
    print(f"Number of documents: {len(corpus)}")
    print(f"Number of unique tokens: {len(dictionary)}")

    # Train the HDP model
    model = HdpModel(corpus=corpus, id2word=id2word)

    topics = model.show_topics()
    print("\n----- MOST SIGNIFICANT TOPICS -----")
    pprint(topics)

    # Get the number of topics inferred by HDP
    num_topics_learned = len(model.show_topics())
    print(f"Number of topics learned: {num_topics_learned}")

    # Extract top topics with their word distributions
    top_topics = model.show_topics(num_topics=num_topics_learned, formatted=False)

    print(f"\n----- MOST SIGNIFICANT TOPICS WITH WEIGHTS (n={num_topics_learned}) -----")
    for topic_id, topic_words in top_topics:
        print(f"\nTopic {topic_id}:")
        pprint([(word, round(weight, 4)) for word, weight in topic_words])

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--text_dir", type=str, default="./parsed")
    args = parser.parse_args()
    main(args)
