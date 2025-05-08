from textblob import TextBlob

# Ask for user input
text = input("Enter a sentence: ")

# Create a TextBlob object
blob = TextBlob(text)

# Analyze sentiment
polarity = blob.sentiment.polarity

# Print sentiment result
if polarity > 0:
    print("The sentiment is positive.")
elif polarity < 0:
    print("The sentiment is negative.")
else:
    print("The sentiment is neutral.")

# Also show the polarity score
print("Polarity score:", polarity)