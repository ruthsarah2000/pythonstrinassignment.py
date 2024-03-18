'''
1. Product Review Analysis
Task 1: Keyword Highlighter
Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", 
"poor", and "average". Print out each review with the keywords in uppercase so they stand out.

Task 2: Sentiment Tally
Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and 
negative words to check against. The function should return the count of positive and negative words for each review.

Task 3: Review Summary
Implement a script that takes the first 50 characters of a review and appends "…" to create a summary. Ensure that the summary does 
not cut off in the middle of a word.
'''
#Task 1#
import re
paragraph = ['Excellent product', 'Average results', 'Poor quality', 'Good outcome, would buy again', 'Bad product, do not buy']
key_words = ["Excellent", "Average", "Poor", "Good", "Bad"]
for review in paragraph:
    for word in key_words:
        matches = re.findall(word,review)
        if matches:
            print(review.upper())
            break


#Task 2#

positive_words = ["good", "excellent", "awesome", "great"]
negative_words = ["bad", "poor", "terrible", "awful"]

def tally_sentiment(review):
    positive_count = 0
    negative_count = 0
    
    
    words = review.split()
    
    for word in words:
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1
    return positive_count, negative_count

reviews = [
    "Excellent product.",
    "Average results.",
    "Poor quality.",
    "Good outcome, would buy again.",
    "Bad product, do not buy"

]

for idx, review in enumerate(reviews, start=1):
    positive_count, negative_count = tally_sentiment(review)
    print(f"Review {idx}: Positive words: {positive_count}, Negative words: {negative_count}")

#Task 3#
    
review = ["My experience with Rx Medical Billing was excellent! The staff was exceptional and they got my claims paid in less that 10 days. I would recommend their services."]

review[0] = review[0][:52]

print(review)

