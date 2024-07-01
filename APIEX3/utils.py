# imports

import json , beaupy

# JSON

def loadJSONFile(filename):
    try:
        with open(filename , 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("\nErro: ficheiro não encontrado!\n")
        return []
    except:
        print("\nErro !!!!!!!\n")
        return []
    else:
        return data
    
def saveJSONFile(filename, list):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list, f, indent=4)
    except FileNotFoundError:
        print("\nErro: não foi possível gravar o ficheiro!\n")
    except:
        print("\nUps, deu erro!")

# FUNCTIONS

def nextID(list):
    ids = [ele['id'] for ele in list]
    if ids:
        return max(ids)+1
    else:
        return 1

def getItemID(list):
    op = int(beaupy.select(list, cursor="->", cursor_style='green', return_index=True))
    return list[op]['id']