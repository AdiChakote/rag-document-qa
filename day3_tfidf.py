from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "I love drinking hot masala chai in the morning.",
    "The bank approved my home loan application.",
    "It is raining heavily in the city today.",
    "My credit score affects the interest rate I get.",
    "She makes delicious tea with ginger and cardamom.",
    "The monsoon clouds covered the sky.",
    "Banks check your repayment history before lending money.",
    "Football is the most popular sport in the world.",
    "He scored two goals in the final match.",
    "Python is a popular programming language for data science.",
]

queries = [
    "How do lenders decide who gets a loan?",
    "What is a good hot drink?",
    "Weather today",
]

vectorizer = TfidfVectorizer()
doc_matrix = vectorizer.fit_transform(sentences)

for query in queries:
    q = vectorizer.transform([query])
    scores = cosine_similarity(q, doc_matrix)[0]
    ranked = sorted(zip(scores, sentences), reverse=True)
    print("QUERY:", query)
    for score, sentence in ranked[:3]:
        print("  ", round(float(score), 3), sentence)
    print()