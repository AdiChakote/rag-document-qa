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
