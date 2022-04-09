#importing malaya
import malaya
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

#initialize models for predictions
print("Initializing... [0/5]")
alxlnet = malaya.zero_shot.classification.transformer(model = 'alxlnet')
os.system('clear')
print("Initializing... [1/5]")
albert = malaya.zero_shot.classification.transformer(model = 'albert')
os.system('clear')
print("Initializing... [2/5]")
tiny_bert = malaya.zero_shot.classification.transformer(model = 'tiny-bert')
os.system('clear')
print("Initializing... [3/5]")
labels = ['buli', 'mesra', 'gaduh', 'kawan']

malaya.stack.predict_stack([alxlnet, albert, tiny_bert], ['Aku harap benda ni menjadi'], labels = labels) #init string
os.system('clear')
print("Initializing... [4/5]")

#normalization model
corrector = malaya.spell.probability()
normalizer = malaya.normalize.normalizer(corrector)

normalizer.normalize('aq hrp bnde ni jdi la') #init string
os.system('clear')
print("Initializing... [5/5]")
print("Tool Initialized.")

# define function
def cyb(text):
    if (len(text[0]) == 0):
        return('empty')
    else:
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

        for x in range(5):
            avg_buli = avg_buli + res[x][0]['buli']
            avg_gaduh = avg_gaduh + res[x][0]['gaduh']
            avg_mesra = avg_mesra + res[x][0]['mesra']
            avg_kawan = avg_kawan + res[x][0]['kawan']
        
        #divide for avg
        avg_buli = avg_buli / 5
        avg_gaduh = avg_gaduh / 5
        avg_mesra = avg_mesra / 5
        avg_kawan = avg_kawan / 5


        final = {'buli' : avg_buli, 'gaduh' : avg_gaduh, 'mesra' : avg_mesra, 'kawan' : avg_kawan}
        print(final)
        return(max(final, key=final.get))

# testing code, comment in production env
# text = []
# text.append(input("Enter Text for emotion analysis "))
# print(cyb(text))
