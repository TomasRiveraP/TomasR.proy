def palidromo(numero:int) -> bool:
    centena=numero//100
    decena=(numero-centena*100)//100
    unidad=numero-centena*100-decena*10

    if centena == unidad:
        resultado = True
    else:
        resultado = False
    return resultado

def espar(numero:int) -> bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def clasificar_chocolate(codigo:int) -> str:
    if palidromo(codigo):
        if espar(codigo):
            resultado = "sweet"
        else:
            resultado = "bitter"
    else:
        if espar(codigo):
            resultado = "cinnamon"
        else:
            resultado = "light"
    return resultado

print(clasificar_chocolate(123))
print(clasificar_chocolate(222))
print(clasificar_chocolate(111))
print(clasificar_chocolate(505))
print(clasificar_chocolate(576))
