import string

punc = string.punctuation #pull in pre-made punctuation list

text = "The cat sat. The cat ran!" #source list
#text_target = ['the', 'cat', 'sat', 'the', 'cat', 'ran']

# 1. lowercase
text = text.lower()

# 2. split each word separately
words = text.split()

# 2.5 synthetic edge case
ec = "a - b"
ec = ec.lower().split()

# 3. loop through each word & each punctuation and remove if true
stripped = [w.strip(punc) for w in ec]
new_words = [w for w in stripped if w]

print(f"Start: {text}")
print(f"End: {new_words}")