

"""
Created on Sun Jan  9 16:04:27 2022

@author: Alfredo Diaz

"""
def evaluador(seleccion1='', seleccion2='', seleccion3='', seleccion4='', seleccion5='',
              seleccion6='', seleccion7='', seleccion8='', seleccion9='', seleccion10='',
              seleccion11='', seleccion13='', seleccion14='', seleccion15='',
              seleccion17='', seleccion18='', seleccion19=''):
    
    nota = 0  # Inicializar la nota
    
    print("RESULTADO DEL EXAMEN\n")
    print("**********************")

    # Evaluar las selecciones y asignar puntos
    correct_answers = {
        'seleccion1': 'Mejorar la convergencia del algoritmo',
        'seleccion2': 'Ajustar la escala de las características',
        'seleccion3': 'One-hot encoding',
        'seleccion4': 'Todas las anteriores son correctas',
        'seleccion5': 'La clasificación predice etiquetas categóricas, mientras que la regresión predice valores continuos',
        'seleccion6': 'Cuando se tiene un conjunto de datos etiquetado y se desea predecir etiquetas',
        'seleccion7': 'Aumentar la representatividad de la clase minoritaria',
        'seleccion8': 'Predecir la venta futura de un producto',
        'seleccion9': 'Un clasificador predice etiquetas, un regresor predice valores continuos',
        'seleccion10': 'Usando el coeficiente de correlación',
        'seleccion11': '1002',
        'seleccion13': '14',
        'seleccion14': '1',
        'seleccion15': '11',
        'seleccion17': '38.65',
        'seleccion18': 'No',
        'seleccion19': 'Puedo balancear usando oversampling'
    }

    selections = {
        'seleccion1': seleccion1,
        'seleccion2': seleccion2,
        'seleccion3': seleccion3,
        'seleccion4': seleccion4,
        'seleccion5': seleccion5,
        'seleccion6': seleccion6,
        'seleccion7': seleccion7,
        'seleccion8': seleccion8,
        'seleccion9': seleccion9,
        'seleccion10': seleccion10,
        'seleccion11': seleccion11,
        'seleccion13': seleccion13,
        'seleccion14': seleccion14,
        'seleccion15': seleccion15,
        'seleccion17': seleccion17,
        'seleccion18': seleccion18,
        'seleccion19': seleccion19
    }

    # Evaluar respuestas
    for key in correct_answers:
        if selections[key] == correct_answers[key]:
            nota += 1
            print(f"{key}: Respuesta enviada: '{selections[key]}'. Respuesta correcta.")
        else:
            print(f"{key}: Respuesta enviada: '{selections[key]}'. Respuesta incorrecta. Debe ser '{correct_answers[key]}'.")
    
    # Asignar puntos a las selecciones numéricas
    try:
        if int(seleccion11) == '1002':
            nota += 1
        if int(seleccion13) == '14':
            nota += 1
        if int(seleccion14) == '1':
            nota += 1
        if int(seleccion15) == '11':
            nota += 1
        if float(seleccion17) == '38.65':
            nota += 1
    except ValueError:
        print("Respuestas numéricas inválidas. Asegúrate de ingresar números correctos.")

    # Evaluar la selección de balanceo
    if seleccion18 == 'No':
        nota -= 1
        print("seleccion18: Respuesta incorrecta. Se espera una respuesta afirmativa sobre el balanceo.")
    if seleccion19 == 'Puedo balancear usando oversampling':
        nota += 1

    # Calcular nota final
    nota = (nota * 5) / 17

    # Determinar el resultado basado en la nota
    if nota < 3:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/rechazado.JPG"
    elif nota < 3.9:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/restriccion.JPG"
    else:
        resultado = "https://raw.githubusercontent.com/adiacla/examen2026/main/aprobado.JPG"

    return nota, resultado
