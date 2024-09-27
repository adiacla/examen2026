

"""
Created on Sun Jan  9 16:04:27 2022

@author: Alfredo Diaz
"""
def evaluador(seleccion1, seleccion2, seleccion3, seleccion4, seleccion5,
                seleccion6, seleccion7, seleccion8, seleccion9, seleccion10,
                seleccion11, seleccion13, seleccion14, seleccion15,
                seleccion17, seleccion18, seleccion19):
    
    nota = 0  # Inicializar la nota
    
    print("RESULTADO DEL EXAMEN\n")
    print("**********************")

    # Evaluar las selecciones y asignar puntos
    if seleccion1 == 'Mejorar la convergencia del algoritmo':
        nota += 1
        print("seleccion1: Respuesta correcta.")
    else:
        print("seleccion1: Respuesta incorrecta. Debe ser 'Mejorar la convergencia del algoritmo'.")
    
    if seleccion2 == 'Ajustar la escala de las características':
        nota += 1
        print("seleccion2: Respuesta correcta.")
    else:
        print("seleccion2: Respuesta incorrecta. Debe ser 'Ajustar la escala de las características'.")
    
    if seleccion3 == 'One-hot encoding':
        nota += 1
        print("seleccion3: Respuesta correcta.")
    else:
        print("seleccion3: Respuesta incorrecta. Debe ser 'One-hot encoding'.")
    
    if seleccion4 == 'Todas las anteriores son correctas':
        nota += 1
        print("seleccion4: Respuesta correcta.")
    else:
        print("seleccion4: Respuesta incorrecta. Debe ser 'Todas las anteriores son correctas'.")
    
    if seleccion5 == 'La clasificación predice etiquetas categóricas, mientras que la regresión predice valores continuos':
        nota += 1
        print("seleccion5: Respuesta correcta.")
    else:
        print("seleccion5: Respuesta incorrecta. Debe ser 'La clasificación predice etiquetas categóricas, mientras que la regresión predice valores continuos'.")
    
    if seleccion6 == 'Cuando se tiene un conjunto de datos etiquetado y se desea predecir etiquetas':
        nota += 1
        print("seleccion6: Respuesta correcta.")
    else:
        print("seleccion6: Respuesta incorrecta. Debe ser 'Cuando se tiene un conjunto de datos etiquetado y se desea predecir etiquetas'.")
    
    if seleccion7 == 'Aumentar la representatividad de la clase minoritaria':
        nota += 1
        print("seleccion7: Respuesta correcta.")
    else:
        print("seleccion7: Respuesta incorrecta. Debe ser 'Aumentar la representatividad de la clase minoritaria'.")
    
    if seleccion8 == 'Predecir la venta futura de un producto':
        nota += 1
        print("seleccion8: Respuesta correcta.")
    else:
        print("seleccion8: Respuesta incorrecta. Debe ser 'Predecir la venta futura de un producto'.")
    
    if seleccion9 == 'Un clasificador predice etiquetas, un regresor predice valores continuos':
        nota += 1
        print("seleccion9: Respuesta correcta.")
    else:
        print("seleccion9: Respuesta incorrecta. Debe ser 'Un clasificador predice etiquetas, un regresor predice valores continuos'.")
    
    if seleccion10 == 'Usando el coeficiente de correlación':
        nota += 1
        print("seleccion10: Respuesta correcta.")
    else:
        print("seleccion10: Respuesta incorrecta. Debe ser 'Usando el coeficiente de correlación'.")

    # Asignar puntos a las selecciones numéricas (ejemplo simple)
    try:
        if int(seleccion11) =='1002':
            nota += 1
            print("seleccion11: Respuesta correcta.")
        else:
            print("seleccion11: Respuesta incorrecta. Debe ser un número mayor que 1000.")
        
        if int(seleccion13) =='14':
            nota += 1
            print("seleccion13: Respuesta correcta.")
        else:
            print("seleccion13: Respuesta incorrecta. Debe ser un número mayor que 10.")
        
        if int(seleccion14) == '1':
            nota += 1
            print("seleccion14: Respuesta correcta.")
        else:
            print("seleccion14: Respuesta incorrecta. Debe ser 1.")
        
        if int(seleccion15) == '11':
            nota += 1
            print("seleccion15: Respuesta correcta.")
        else:
            print("seleccion15: Respuesta incorrecta. Debe ser un número mayor que 10.")
        
        if float(seleccion17) =='38.65':
            nota += 1
            print("seleccion17: Respuesta correcta.")
        else:
            print("seleccion17: Respuesta incorrecta. Debe ser un número mayor que 30.")
    
    except ValueError:
        print("Respuestas numéricas inválidas. Asegúrate de ingresar números correctos.")

    # Evaluar la selección de balanceo
    if seleccion18 == 'No':
        nota -= 1
        print("seleccion18: Respuesta incorrecta. Se espera una respuesta afirmativa sobre el balanceo.")
    if seleccion19 == 'Puedo balancear usando oversampling':
        nota += 1
        print("seleccion19: Respuesta correcta.")
    else:
        print("seleccion19: Respuesta incorrecta. Debe ser 'Puedo balancear usando oversampling'.")

    nota=(nota*5)/17
        # Determinar el resultado basado en la nota
    if nota < 3:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/rechazado.JPG"
    elif nota < 3.9:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/restriccion.JPG"
    else:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/aprobado.JPG"   
    
    return nota, resultado