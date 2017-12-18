

##################################################################
##################################################################
# co the giai quyet duoc cac cai de nhu sau:
# cho tam giac ABC co duong cao AH, duong phan giac, trung tuyen
# duong thang d song song voi BC cat AB va AC lan luot tai M, N

import nlp

defaultShap = ''

def process(sentence):

    global defaultShap
    
    names = nlp.extractName(sentence)

    for name in names:
        if len(defaultShap) < len(name):
            defaultShap = name

    (index, template) = nlp.getTemplate(sentence)
    fc = nlp.functions[index]
    # neu so luong tham so it hon, nghia la minh can hieu la o tam giac
    if len(names) < fc[1]:
        names.append(defaultShap)
    fc[0](names)

def main():
    
    nlp.readKeywords('../data/keywords.txt')
    nlp.readTemplates('../data/template.txt')

    while True:
        sentence = input()        
        process(sentence)        

main()











