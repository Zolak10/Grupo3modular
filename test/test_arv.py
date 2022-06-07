import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import arv

def test_wordInarq():
    assert arv.wordInArq('frutas.txt','banana')
    assert main.add(3.5, 4) == 7
    assert main.add(3.9, 4) == 7
    assert main.add(3.9, 4.1) == 8

