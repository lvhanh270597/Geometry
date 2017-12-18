
import functions as fc

keywords = []
templates = []
functions = [(fc.TamGiac, 1), 
             (fc.Doan, 1),
             (fc.Duong, 1),
             (fc.DuongCaoTamGiac2, 3),
             (fc.DuongCaoTamGiac, 2),
             (fc.DoanPhanGiac, 2),
             (fc.TrungTuyen, 2),
             (fc.DuongCaoTamGiac, 2),
             (fc.DoanPhanGiac, 2)
             ]

def bigrams(v):
    n = len(v)
    res = []
    for i in range(n - 1):
        res.append((v[i], v[i + 1]))
    return res

class Template(object):
    def __init__(self, ListOfWords, numberOfArgument):
        self.L = ListOfWords
        self.n = numberOfArgument
    def __str__(self):
        return str(self.L) + " with " + str(self.n) + " args"

def readKeywords(fpath):
    f = open(fpath, 'r')
    for line in f:
        mtp = line[: len(line) - 1]
        keywords.append(tuple(mtp.split()))
    f.close()

def readTemplates(fpath):
    f = open(fpath, 'r')
    
    for line in f:
        mtp = line[: len(line) - 1]
        v = mtp.split(',')

        n = int(v[-1])
        
        v = v[ : len(v) - 1]
        
        L = []        
        for u in v: L.append(tuple(u.split()))

        templates.append(Template(L, n))
        
    f.close()

def extractKeywords(sentence):
    words = sentence.split()
    bigs = bigrams(words)
    res = [big for big in bigs if big in keywords]
    return res

def extractName(sentence):
    words = sentence.split()
    res = [word for word in words \
           if (word.startswith('d') and len(word) == 2)\
           or word.isupper()]
    return res

def getTemplate(sentence):
    KeysOfSentence = extractKeywords(sentence)
    ListOfNames = extractName(sentence)
    numberOfName = len(ListOfNames)
    for i in range(len(templates)):
        temp = templates[i]
        if (numberOfName == temp.n) and \
           (set(temp.L) == set(KeysOfSentence)):            
            return (i, temp)

    return None








    
