edad = int(input("proporciona tu edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "la infancia es increible"
elif 10 <= edad < 20:
    mensaje = "muchos cambios, mucho estudio"
elif 20 <= edad < 30:
    mensaje = "amor y comienza el trabajo"
else:
    mensaje = "etapa de voda no reconocida"
print(f"tu edad es: {edad}, {mensaje}")
