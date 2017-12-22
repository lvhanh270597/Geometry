
import functions as fc
import knowledge as know
import math

dictionary = []
data_train = []


def getBigrams(v):
    '''n = len(v)
    res = []
    for i in range(n - 1):
        res.append((v[i], v[i + 1]))'''
    return v

def loadData(fpath):
    global dictionary
    f = open(fpath)
    num = int(f.readline())
    sentences = []
    for i in range(num):
        ###################################################
        sentence = ''
        n_des = int(f.readline())        
        for j in range(n_des):
            s = f.readline()
            sentence += s[ : len(s) - 1] + ' ____ '
        ###################################################     
        for j in range(n_des):
            s = f.readline()
            sentence += s[ : len(s) - 1] + ' '                   
        ###### Making dictionary ######
        _v = getBigrams(sentence.split())
        for u in _v:
            if u not in dictionary:
                dictionary.append(u)        
        ###################################################        
        ###############################
        sentences.append(sentence)

    ################## Making data ####################
    for sentence in sentences:        
        data_train.append(getVectorOfWeight(sentence))

    #print(dictionary)


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
    # khong tim thay
    if sum(w) == 0: return None  
    ##############
    n = len(data_train)
    #print(data_train)
    L = [(cosine(w, data_train[i]), i) for i in range(n)]
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

