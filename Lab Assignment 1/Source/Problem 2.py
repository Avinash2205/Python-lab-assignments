# Python code to Reverse each word
# of a Sentence individually

# This is a predefined function which is used to Reverse words
def reverseWordSentence(Sentence):
    # Dividing the Sentence into list of words.
    words = Sentence.split(" ")

    # Reversing each word enabling a new group of words
    nWords = [word[::-1] for word in words]

    # Combining the new words for the creation of a sentence
    nSentence = " ".join(nWords)

    return nSentence
# It is a predefined statement which is used to define the longest word in teh sentence.
# pool is the Python package index for the key and reverse.
def Biggestword(Sentence):
    pool = Sentence.split()
    pool.sort(key=len, reverse=True)
    return pool[0]
# It is used to define the middle word of the sentence with the operation involved in iut
def Middleword(Sentence):
    a =Sentence.split(" ")
    print(a)
    if len(a) % 2 == 0:
        return a[int(len(a) / 2)], a[int(len(a) / 2 - 1)]
    else:
        return a[int(len(a) // 2)]

# input the sentence as per the wish of the customer
Sentence = input("Enter the sentence: ")
print("Biggest Word of the sentence is:",Biggestword(Sentence))
print("Middle Word of the sentence is:",Middleword(Sentence))
print("Reverse of the Sentence is :",reverseWordSentence(Sentence))