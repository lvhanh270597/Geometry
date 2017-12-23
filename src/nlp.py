
import functions as fc
import knowledge as know
import math
from sklearn.svm import LinearSVC

dictionary = []
sentences = []
templates = []
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

def loadData():
    f = open('../data/data.txt', 'r')
    num = int(f.readline())
    for i in range(num):
    ###############################################################################
        sentence = f.readline()        
        category = f.readline()
        category = category[ : len(category) - 1]
        sentence = sentence[ : len(sentence) - 1] 
    #################################MAKING-DICTIONARY#############################
        v = getVectorOfWords(sentence)
        for u in v:
            if u not in dictionary:
                dictionary.append(u)  
        sentence = ' '.join(v)
    ################################################################################
        sentences.append(sentence)
        y.append(category)
    f.close()    
    ####################################READ CATEGORIES#############################
    f = open('../data/categories.txt', 'r')
    num = int(f.readline())
    for i in range(num):
        category = f.readline()
        category = category[ : len(category) - 1]
        
        if category not in limited_list.keys():
            limited_list[category] = [i]
        else:
            limited_list[category].append(i)
    f.close()
    #####################################MAKING DATA#################################        
    for sentence in sentences:        
        X.append(getVectorOfWeight(sentence))    
    #####################################MAKING TEMPLATEs############################
    f = open('../data/templates.txt', 'r')
    sentences.clear()
    num = int(f.readline())
    for i in range(num):
        sentence = f.readline()
        sentence = sentence[ : len(sentence) - 1]
        templates.append(getVectorOfWeight(sentence))    
        sentences.append(sentence)

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
    return getBigrams(vectorOfWords)
def getVectorOfWeight(sentence):
    vectorOfWords = getVectorOfWords(sentence)    
    w = []
    for d in dictionary:
        if vectorOfWords.count(d) > 0:
            w.append(1)
        else:
            w.append(0)    
    return w

def getTheSame(sentence):    
    w = getVectorOfWeight(sentence)  
    
    if sum(w) == 0: return None

    category = clf.predict([w])[0]    
    ##########################################
    n = len(X)    
    L = [(cosine(w, templates[i]), i) for i in limited_list[category]]
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
    return res

