print("Para el registro se solicitan los siguientes datos")
nombre = input("Ingrese nombre")
edad = input("Ingrese edad(debe ser en numero) : ")
altura = input("ingrese su altura(debe ser en numero) : ")
rolAdmin = input("ingrese rol administrador True/False : ")

try:
    edad = int(edad)
    altura = float(altura)
    if rolAdmin == "True" or rolAdmin == "false"
        if rolAdmin == "True" : rolAdmin=True
        elif rolAdmin == "false" : rolAdmin=False
    else: 
        exit()

except:
    print("alguno de los valores ingresados no es correcto")
    print("vuelva a correr la app")
    