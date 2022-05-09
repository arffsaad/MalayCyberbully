#importing malaya
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import malaya
from os import system
import loadingBar

#initialize models for predictions
loadingBar.printProgressBar(0, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
alxlnet = malaya.zero_shot.classification.transformer(model = 'alxlnet')

loadingBar.printProgressBar(1, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
albert = malaya.zero_shot.classification.transformer(model = 'albert')

loadingBar.printProgressBar(2, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
tiny_bert = malaya.zero_shot.classification.transformer(model = 'tiny-bert')

loadingBar.printProgressBar(3, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
labels = ['buli', 'mesra', 'gaduh', 'kawan', 'tak setuju']
txc = malaya.toxicity.transformer(model = 'alxlnet')

loadingBar.printProgressBar(4, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
txc1 = malaya.toxicity.transformer(model = 'albert')

loadingBar.printProgressBar(5, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
txc2 = malaya.toxicity.transformer(model = 'tiny-bert')

loadingBar.printProgressBar(6, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
malaya.stack.predict_stack([alxlnet, albert, tiny_bert], ['Aku harap benda ni menjadi'], labels = labels) #init string


loadingBar.printProgressBar(7, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
malaya.stack.predict_stack([txc,txc1,txc2], ["bodoh"])


loadingBar.printProgressBar(8, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
#normalization model
corrector = malaya.spell.probability()
normalizer = malaya.normalize.normalizer(corrector)
loadingBar.printProgressBar(9, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
normalizer.normalize('aq hrp bnde ni jdi la') #init string


#toxicity model
toxic = malaya.toxicity.transformer(model = 'alxlnet')

loadingBar.printProgressBar(10, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
toxic.predict(['Aku harap benda ni menjadi'])
loadingBar.printProgressBar(11, 11, prefix = 'Initializing:', suffix = 'Complete', length = 35)
print("Tool Initialized.")

# define function
def cyb(text):
    global alxlnet, albert, tiny_bert, normalizer, corrector , labels
    norm_text = normalizer.normalize(text[0])
    string = [str(norm_text['normalize'])]
    print(string)
    res = []
    for x in range(5):
        res.append(malaya.stack.predict_stack([alxlnet, albert, tiny_bert], string, labels = labels))
    
    #define avg vars
    avg_buli = 0
    avg_mesra = 0
    avg_gaduh = 0
    avg_kawan = 0
    avg_disagree = 0

    for x in range(5):
        avg_buli = avg_buli + res[x][0]['buli']
        avg_gaduh = avg_gaduh + res[x][0]['gaduh']
        avg_mesra = avg_mesra + res[x][0]['mesra']
        avg_kawan = avg_kawan + res[x][0]['kawan']
        avg_disagree = avg_disagree + res[x][0]['tak setuju']
    
    #divide for avg
    avg_buli = avg_buli / 5
    avg_gaduh = avg_gaduh / 5
    avg_mesra = avg_mesra / 5
    avg_kawan = avg_kawan / 5
    avg_disagree = avg_disagree / 5


    final = {'buli' : avg_buli, 'gaduh' : avg_gaduh, 'mesra' : avg_mesra, 'kawan' : avg_kawan, 'tak setuju' : avg_disagree}
    verdict = max(final, key=final.get)
    print(final, "\n", verdict)
    if (verdict == 'tak setuju'):
        tox = toxic.predict(string)
        if (len(tox[0]) >= 1):
            return('gaduh')
        else:
            return(verdict)
    else:
        return(verdict)


def cen(text):
    global txc, txc1, txc2, normalizer, corrector
    norm_text = normalizer.normalize(text[0])
    splstr = str(text[0]).split()
    print ("Original split: ", splstr)
    string = str(norm_text['normalize'])
    print(string)
    stro = str(string)
    split = stro.split()
    print(split)
    split = list(filter((',').__ne__, split))
    split = list(filter(('?').__ne__, split))
    split = list(filter(('!').__ne__, split))
    split = list(filter(('.').__ne__, split))
    isneg = []
    for x in split:
        res=malaya.stack.predict_stack([txc,txc1,txc2], [x])
        proba = res[0][max(res[0], key=res[0].get)]
        if (proba > 0.4):
            isneg.append(1)
        else:
            isneg.append(0)
    finished = ""
    for x in range(len(split)):
        if (isneg[x] == 1):
            finished = finished + '<span class="censor">' + str(splstr[x]) + '</span> '
        else:
            finished = finished +  str(splstr[x]) + ' '
    print(isneg)
    return finished
