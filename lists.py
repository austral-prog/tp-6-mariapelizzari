# Replace the "ANSWER HERE" with your answer
def remove_elements(list_to_remove_elements):
    remove = list_to_remove_elements[:]
    if len(remove) > 5:
        del remove[5]
    if len(remove) > 4:
        del remove[4]
    if len(remove) > 0:
        del remove[0]
    return remove


def add_elements(list_to_add_elements):
    add = list_to_add_elements[:]
    add.append("Yellow")
    add.insert(0,"Pink")
    return add


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    lista_1 = list_to_compare1[:]
    lista_2 = list_to_compare2[:]
    if len(lista_1) >= 3 and len(lista_2) >= 3:
        if lista_1[2] == lista_2[2]:
            return True
        else: 
            return False
    else: 
        return False 

def list_of_lists(list_of_lists_to_modify):
    listaconjunto = list_of_lists_to_modify[:]
    listaconjunto[0] = listaconjunto[0][ :2]
    listaconjunto[1] = listaconjunto[1][1:4]
    listaconjunto[2] = listaconjunto[2][-2:]
    return listaconjunto
