# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    """
    Elimina los ingredientes duplicados de una receta.

    Args:
        nombre_plato: String con el nombre del plato
        ingredientes: Lista de ingredientes (puede contener duplicados)

    Returns:
        Una tupla (nombre_plato, set_de_ingredientes_sin_duplicados)
    """
    return (str(nombre_plato), set(ingredientes))


def check_drinks(nombre_bebida, ingredientes):
    """
    Clasifica una bebida como "Cocktail" (contiene alcohol) o "Mocktail"
    (no contiene alcohol) basándose en sus ingredientes.

    Los ingredientes alcohólicos válidos están definidos en el set ALCOHOLS.

    Args:
        nombre_bebida: String con el nombre de la bebida
        ingredientes: Lista de ingredientes de la bebida

    Returns:
        String con el nombre de la bebida seguido de "Cocktail" o "Mocktail"
    """
    set_ingredientes = set(ingredientes)
    if set_ingredientes & ALCOHOLS:
        tipo_de_bebida = "Cocktail"
        return str(nombre_bebida) + " " + tipo_de_bebida
    else:
        tipo_de_bebida = "Mocktail"
        return str(nombre_bebida) + " " + tipo_de_bebida


def unique_chars(texto):
    """
    Retorna un set con los caracteres únicos de un string.

    Args:
        texto: Un string

    Returns:
        Un set con los caracteres únicos del texto

    Ejemplo:
        unique_chars("hello") -> {'h', 'e', 'l', 'o'}
    """
    return set(texto)


def sum_set(numeros):
    """
    Recorre un set de números y retorna la suma total.
    Si el set está vacío, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo el set con un for (o while).

    Args:
        numeros: Set de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos del set

    Ejemplo:
        sum_set({1, 2, 3, 4}) -> 10
        sum_set(set()) -> 0
    """
    suma = 0
    for i in numeros:
        suma += i
    return suma


def common_elements(set_a, set_b):
    """
    Retorna un nuevo set con los elementos que aparecen en AMBOS sets.

    No se permite usar el operador & ni el método .intersection().
    Implementar la intersección recorriendo uno de los sets y
    verificando pertenencia en el otro.

    Args:
        set_a: Primer set
        set_b: Segundo set

    Returns:
        Set con los elementos presentes en ambos

    Ejemplo:
        common_elements({1, 2, 3}, {2, 3, 4}) -> {2, 3}
        common_elements({1, 2}, {3, 4}) -> set()
    """
    elementos_comunes = []
    for i in set_a:
        for h in set_b:
            if i == h:
                elementos_comunes.append(i)
    return set(elementos_comunes)