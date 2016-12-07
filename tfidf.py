# coding: utf-8

def tf(terms, document):
    tf_values = [document.count(term) for term in terms]
    return list(map(lambda x: x/sum(tf_values), tf_values))

def idf(terms, documents):
    import math
    return [math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms]

def tf_idf(terms, documents):
    return [[_tf*_idf for _tf, _idf in zip(tf(terms, document), idf(terms, documents))] for document in documents]

text1 = "政府は、GDPの数値目標を明示して掲げています。その政府ですが、年明け最初の経済財政諮問会議で、景気対策と失業率についての追加の総合経済対策について、民間議員から意見を聞いた模様です。GDP数値目標についても、突っ込んだ意見が出たのかどうかに注目が集まっています。"
text2 = "FRB（米連邦準備制度理事会）は、伝統的な物価上昇率と並び、米国の国内失業率の水準を、金融政策の舵取りを行う上で、主要な参考数値に位置付けている。"
text3 = "失業率、失業率、失業率"
text4 = "景気対策、景気対策"

terms = ["GDP", "景気対策", "失業率"]
documents = [text1, text2, text3, text4]

result = tf_idf(terms, documents)
print(result)
terms = ["apple", "gorilla", "lappa"]
documents = ["appleandapple", "appleandgorilla", "gorillaandlappa"]
print(documents)
print(tf_idf(terms, documents))
