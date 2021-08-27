def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) ->str:

        
    notas = (nota1, nota2, nota3, nota4, nota5)
    
    min = max = notas[0]
    for nota in notas:
        if nota < min:
            min = nota
        elif nota > max:
            max = nota
    


    notas = sum(notas)
    notas = notas - min
    
    promedio = notas/ 4
    promedio = round(promedio, 2)
    promedio = promedio*5.0/100
    res = (str("El promedio ajustado del estudiante " +codigo+ " es: " + str(promedio)))
    return res
    
r=nota_quices('a3', 100, 100, 100, 100, 100)
print(r)


