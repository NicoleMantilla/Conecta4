#PRESENCIA INSTANCIA BUSCA LA AGUJA
# Funciones para:
# 1. Detectaremos la presencia de UNA instancia del elemento dentro de una lista, en cualquier posición.
# 2. Detectaremos la presencia de N instancias dentro de una lista, en cualquier posición
# 3. Detectaremos la presencia de N elementos SEGUIDOS dentro de una lista.

def find_one(list, needle):
    """
    Devuelve True si encuentra a needle en la lista en alguna posición
    Sino, devuelve False
    """
    return find_n(list, needle, 1)

def find_n(list, needle, n):

    if n > 0:
        # inicializo el contador de veces que lo he encontrado
        # inicializo el indice del elemento actual
        index = 0
        count = 0
        # mientras no haya encontrado n veces y no haya terminado la lista
        while count < n and index < len(list):
            # si la encuento, actualizo el contador 
            if needle == list[index]:
                count = count + 1

            #pase lo que pase, actualizo el contador
            index = index + 1
        
        # devuelvo el resultado de comparar n con el contador
        return count >= n
    else:
        # pregunta idiota
        return False

def find_streak(list, element, size):
    """
    Devuelve True si en list hay size o más elementos SEGUIDOS  
    False en caso contrario y también si size <= 0
    """
    if size > 0:
        # Inicializo el indice, el contador, y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya ecnontrado a size elements seguidos y la lista no se haya terminado
        while count < size and index < len(list):
            
            if list[index] == element:
                # si lo encuentro, activo el indicador de rachas y incremento el contador
                streak = True
                count = count + 1
            else:
                # si no lo encuentro, desactivo indicador de rachas y pongo contador a cero
                streak = False
                count = 0
            
            # avanzo al siguiente elemento (incremento indice)
            index = index + 1
        
        # devolvemos el resultado de comparar el contador con size, 
        # SIEMPRE Y CUANDO ESTEMOS EN RACHA
        if streak == True:
            return count >= size
        else:
            return False
           
    else:
        return False

# buscar una racha de 4s de longitud 3: 4,4,4
# find_streak([0, 7, 7], 7, 3)


def first_elements(list_of_lists):
    """"
    Receibe una matriz (lista de listas) y devuelve una lista
    con los primeros elementos de cada una de las listas de la
    matriz
    """
    return nth_elements(list_of_lists, 0)

def nth_elements(list_of_lists,n):
    """"
    Receibe una matriz (lista de listas) y devuelve una lista
    con los enésimos elementos de cada una de las listas de la
    matriz
    """
    result = []
    for sub_list in list_of_lists:
        result.append(sub_list[n])
    return result

def transpose(list_of_lists):
    """
    Recibe una matriz y devuelve su transpuesta
    """
    # creo una matriz vacía, en la que iré acumulando
    transp = []
    # desde cero al último indice de list_of_lists
    for index in range(len(list_of_lists)):
        # extraigo sus valores enésimos y se lso encasqueto a la acumualda
        transp.append(nth_elements(list_of_lists, index))
    # devuelvo la acumulada
    return transp