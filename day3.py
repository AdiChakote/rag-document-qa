from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

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

embeddings = model.encode(sentences)

queries = [
    "How do lenders decide who gets a loan?",
    "What is a good hot drink?",
    "Weather today",
]

for query in queries:
    query_embedding = model.encode(query)
    scores = util.cos_sim(query_embedding, embeddings)[0]
    ranked = sorted(zip(scores.tolist(), sentences), reverse=True)
    print("QUERY:", query)
    for score, sentence in ranked[:3]:
        print("  ", round(score, 3), sentence)
    print()