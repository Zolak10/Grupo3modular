import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import arv

def test_wordInarq():
    assert arv.wordInArq('frutas.txt','banana')


