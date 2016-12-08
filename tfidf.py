document1 = "I have a pen"
document2 = "I have an apple"
document3 = "Applepen!"
document4 = "I have a pen"
document5 = "I have apple and apple"

term1 = "pen"
term2 = "apple"

documents = [document1, document2, document3, document4, document5]

def sliceBySpace(document):
    return document.split(" ")

splitted_doc1 = sliceBySpace(document1)
splitted_doc2 = sliceBySpace(document2)
splitted_doc3 = sliceBySpace(document3)
splitted_doc4 = sliceBySpace(document4)
splitted_doc5 = sliceBySpace(document5)

documents = [splitted_doc1, splitted_doc2, splitted_doc3, splitted_doc4, splitted_doc5]

def tf(term, document):
    tf_values = 0
    for word in document:
        if word == term:
            tf_values += 1
    return tf_values

print(tf(term2, splitted_doc5))

def idf(term, documents):
    import math
    df = 0
    for document in documents:
        df += document.count(term)
idf(term1, documents)


# def tf(terms, document):
#     tf_values = [document.count(term) for term in terms]
#     return list(map(lambda x: x/sum(tf_values), tf_values))
#
# def idf(terms, documents):
#     import math
#     return [math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms]
#
# def tf_idf(terms, documents):
#     return [[_tf*_idf for _tf, _idf in zip(tf(terms, document), idf(terms, documents))] for document in documents]
