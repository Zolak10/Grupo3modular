from posixpath import abspath
from trie import *
from os import getcwd 
from os.path import abspath,dirname
__all__ = ['wordInArq', 'insereArvore','verificaPrefixo','procuraArv','clear','palavraAleatoria']
dirname = (dirname(abspath(__file__)))

def wordInArq(word,arq):
    path = dirname + '/' + arq
    file = open(path, 'r')
    list = []
    for line in file:
        list.append(line.strip())
    file.close()
    if word in list:
        return True
    return False

def insereArvore(arq):
    path = dirname + '/' + arq
    print("caminho: ", path, "\n")
    file = open(path, 'r')
    for line in file:
        line = line.strip()
        if wordInArq(line,arq):
            insert(line,arq,wordInArq)
    file.close()
    return

def verificaPrefixo(pr):
   if wordsWith(pr) == []:
       return False
   return True

def procuraArv(s):
    return search(s)

def limpaArv():
    clear()
    return

def palavraAleatoria():
    return random()