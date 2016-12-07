def tf(terms, document):
    tf_values = [document.cont(term) for term in terms]
    return list(map(lambda x: x/sum(tf_values), tf_values))

def idf(terms, documents):
    import math
    return [math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms]

def tf_idf(terms, documents):
    return [[_tf*_idf for _tf, _idf in zip(tf(terms, document), idf(terms, documents))] for document in documents]

terms = ["GDP", "景気対策", "失業率"]
