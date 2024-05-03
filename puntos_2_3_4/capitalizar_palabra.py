def capitalizar_palabra(str1):
    #Justificacion debido a que valido el tipo cambie el nombre del argumento a  str1(string1)
    # # Validaciones
    if type(str1) != str:  # noqa: E721
        raise TypeError("El parametro recibido no es una cadena")
    
    if len(str1) == 0:
        raise ValueError("El parametro recibido es una cadena vacia")
    if str1!= str1.lower():
        raise ValueError("El parametro recibido debe ser una cadena que contenga solo minusculas")   

    try:
        #se retorna el string con el metodo capitilize que hace que la priemra letra sea mayuscula
        return str1.capitalize()
    except Exception as e:
        return e

print(capitalizar_palabra("python"))
print(capitalizar_palabra("dalto"))
print(capitalizar_palabra("gojira"))
print(capitalizar_palabra("rodan09"))
print(capitalizar_palabra("laios"))
