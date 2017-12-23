
import functions as fc
import knowledge as know
import math
from sklearn.svm import LinearSVC

dictionary = []
sentences = []
X = []
y = []
limited_list = {}
clf = None


def getBigrams(v):
    '''n = len(v)
    res = []
    for i in range(n - 1):
        res.append((v[i], v[i + 1]))'''
    return v

def loadData(fpath):
    f = open(fpath)
    num = int(f.readline())
    for i in range(num):
        ###################################################
        sentence = f.readline()        
        category = f.readline()
        category = category[ : len(category) - 1]
        sentence = sentence[ : len(sentence) - 1] 
        v = getVectorOfWords(sentence)
        for u in v:
            if u not in dictionary:
                dictionary.append(u)  
        sentence = ' '.join(v)
        ###################################################     
        if category not in limited_list.keys():
            limited_list[category] = [i]
        else:
            limited_list[category].append(i)
        ###############################
        sentences.append(sentence)
        y.append(category)


    ################## Making data ###################    
    dictionary.append('unknown')
    for sentence in sentences:        
        X.append(getVectorOfWeight(sentence))
    print(dictionary)
    print(limited_list)

def learnData():
    global clf
    clf = LinearSVC(random_state=0)
    clf.fit(X, y)

def getVectorOfWords(sentence):
    V = sentence.split()
    vectorOfWords = []
    for v in V:
        Type = know.getType(v)
        if Type != None:
            vectorOfWords += Type.split()
        else:
            vectorOfWords.append(v)
    #print(vectorOfWords)
    #print(getBigrams(vectorOfWords))
    return getBigrams(vectorOfWords)
def getVectorOfWeight(sentence):
    vectorOfWords = getVectorOfWords(sentence)
    w = []
    for d in dictionary:
        if vectorOfWords.count(d) > 0:
            w.append(1)
        else:
            w.append(0)
    #print(w)
    return w

def getTheSame(sentence):    
    w = getVectorOfWeight(sentence)  
    category = clf.predict([w])[0]
    print(category)
    ##########################################
    n = len(X)
    #print(data_train)
    L = [(cosine(w, X[i]), i) for i in limited_list[category]]
    L.sort(reverse=True)
    return L[ : 3]

def size(u):
    return math.sqrt(sum([i for i in u]))

def cosine(u, v):
    size1 = size(u)
    size2 = size(v)
    s = 0
    n = len(u)
    for i in range(n):
        s += u[i] * v[i]    
    return s / (size1 * size2)

def getNames(sentence):
    vectorOfWords = sentence.split()
    res = [v for v in vectorOfWords if know.getType(v) != None]
    #print(res)
    return res

