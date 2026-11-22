# Day 1 Notes: Calling an LLM from Python

## Question 1

Prompt: Explain what an LLM is in 2 sentences.
Model said: An AI trained on lots of text that learns patterns and can answer questions, write content and chat.
What I noticed: It kept to 2 sentences. The wording changed a little each time I ran it.

## Question 2

Prompt: Explain photosynthesis in one sentence.
Model said: Plants use sunlight, water and carbon dioxide to make oxygen and sugar.
What I noticed: It kept to exactly one sentence.

## Question 3

Prompt: Explain photosynthesis like I'm 5.
Model said: It used a story about plants as tiny chefs, with a list of 3 ingredients.
What I noticed: Same topic as question 2, but the style and length changed a lot.

## Errors I hit

- 404 model not found: the model name was out of date, so I copied the new name from the error message.
- 503 high demand: a Google-side problem. try/except with a 20 second wait handled it.

## What I learned

- The wording of a prompt changes the style and length of the answer.
- LLM calls can fail for reasons that are not my code, so I need error handling.
- I added time.sleep(20) so that when the model is busy, the script waits 20 seconds and then tries the same question again (up to 3 times).
- try/except catches an error, prints a message and lets the script continue instead of crashing.

## Day 2: temperature test

Model that worked: gemini-3.5-flash (gemini-3.8-flash and 3.7-flash were busy with 503 errors)
Temperature 0.0: three different slogans (not identical as I expected)
Temperature 1.5: two identical slogans and one different
What I learned: temperature does not always give the clear pattern the videos show. Outputs can vary even at 0.0, and 3 samples is too few to conclude much.
Other lessons: a timeout that is too short causes 504 errors, and busy models cause 503 errors, so retries and model fallback are needed.

## Day 2: system instruction test

No system instruction: very long answer with headings and lists
Strict teacher instruction: one sentence, as asked
Pirate instruction: two sentences in a pirate style, as asked
What I learned: a system instruction changes length, tone and format. It is how my RAG assistant will be told to answer only from the documents and cite the page.
Also noticed: the model listed older model names as examples, so its built-in knowledge can be out of date.

## Day 2: 10-prompt test (temperature 0.0, model gemini-3.5-flash)

1 Math (37 x 48): correct
2 Made-up 2050 World Cup: no invented winner, said it has not happened yet
3 Fake research paper: said it seems not to exist, but claimed "no records in databases" which it cannot actually search, then added a long unverified section
4 Capital of Australia: correct
5 Haiku: fine
6 Overfitting in one sentence: correct and one sentence
7 Prompt ideas: fine
8 JSON extraction: correct, wrapped in code fences that I would need to strip in code
9 Breakfast question: honestly said it cannot know
10 Pathri population with "say I don't know" instruction: said I don't know, but my prompt told it to, so this is not a clean test
What I learned: this model resisted hallucination here, but it still cannot know my private documents, which is why I am building RAG. Confident wording is not the same as verified facts.
