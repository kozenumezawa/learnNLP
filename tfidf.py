def tf(terms, document):
    tf_values = [document.count(term) for term in terms]
    return list(map(lambda x: x/sum(tf_values), tf_values))

def idf(terms, documents):
    import math
    return [math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms]

def tf_idf(terms, documents):
    return [[_tf*_idf for _tf, _idf in zip(tf(terms, document), idf(terms, documents))] for document in documents]

text1 = "I have a pen"
text2 = "I have an Apple"
text3 = "Applepen!"
text4 = "I have a pen"
text5 = "I have apple and apple"

terms = ["apple", "apple"]

documents = [text1, text2, text3, text4, text5]

# テスト
print(text1.count("pen"))
print(text5.count("apple"))
