# Ejercicios de diccionarios: sistema de inventario

def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    inventario = {}
    cantidad_item = 0
    for item in items:
        if item in inventario:
            cantidad_item += 1
            inventario[item] = cantidad_item
        else:
            cantidad_item = 0
            cantidad_item += 1
            inventario[item] = cantidad_item

    return inventario

def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1
    
    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    for item in items:
        if inventario.get(item, 0) > 0: # Devuelve 0 si el ítem no existe
            inventario[item] -= 1
        
    return inventario

def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    if inventario.get(item):
        inventario.pop(item)
        return inventario
    else:
        return inventario

def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    lista_de_tuplas = []
    claves_a_eliminar = []
    for i in inventario:
        if inventario[i] <= 0:
            claves_a_eliminar.append(i) # Guardo las claves a eliminar en una lista porque no se puede modificar el tamaño de un diccionario mientras se itera
    for i in claves_a_eliminar:
        inventario.pop(i)
    for clave in inventario:
        # No uso "tupla = inventario.items()" --> Esto devuelve "dict_items([('iron', 1), ('diamond', 4), ('gold', 0)])"
        tupla = (clave, inventario[clave])
        lista_de_tuplas.append(tupla)
    return lista_de_tuplas


def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".

    Args:
        diccionario: Diccionario {nombre: puntaje}

    Returns:
        String con la clave de mayor valor, o "" si el dict está vacío

    Ejemplo:
        find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}) -> 'Emma'
    """
    valores = []
    if diccionario:
        for clave in diccionario:
            valor = diccionario[clave]
            valores.append(valor) # [1,0,4]
        valor_mas_alto = max(valores)
        for i in diccionario:
            if diccionario[i] == valor_mas_alto:
                return i
    else:
        return ""
    
    # return max(diccionario, key=diccionario.get) if diccionario else "" --> Oneliner


def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido

    Ejemplo:
        reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        -> {1: 'a', 2: 'be', 3: 'cd'}
    """
    mi_dict_reverso = {}
    for clave, valor in diccionario.items():
        mi_dict_reverso[valor] = mi_dict_reverso.get(valor, "") + clave
    
    return mi_dict_reverso


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    diccionario = {}
    if palabras:
        for elemento in palabras:
            diccionario[elemento] = diccionario.get(elemento, 0)+1
        return diccionario
    else:
        return {}


def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    promedios = []
    if gastos:
        for lista in gastos.values():
            suma_de_valores = 0
            for valor in lista:
                suma_de_valores += valor
            promedio = suma_de_valores/len(lista)
            promedios.append(promedio)
        indice = promedios.index(max(promedios))
        return list(gastos)[indice]
    else:
        return ""


def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    diccionario = {}
    for clave, lista in gastos.items():
        suma_de_valores = 0
        for valor in lista:
            suma_de_valores += valor
        diccionario[clave] = suma_de_valores
    return diccionario

def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    diccionario = {}
    lista_general = []
    for lista in gastos.values():
        for tupla in lista:
            lista_general.append(tupla)
    
    for tupla in lista_general:
        tipo = tupla[0] # Se accede al índice de una tupla con [], no con ().
        monto = tupla[1]
        diccionario[tipo] = diccionario.get(tipo, 0) + monto # Cuando se usa get() no es necesario usar ni un if ni un else, ya que la función devuelve el valor predeterminado de forma segura si la clave no existe / No es necesario usar un "if valor not in diccionario" para crear un ítem en un diccionario, ya que se puede crear o actualizar un ítem directamente sin necesidad de comprobar antes si la clave ya existía.

    return diccionario