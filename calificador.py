import os

def evaluador(df_nps, df_calidad, nps_percentage, respuesta1, total_diferentes, seleccion8,
              Cantidad_soporte, df_final, label, nulos, seleccion12, num_registros_quedan,
              totalnulos, df_final_sinnulo, correlation_matrix, seleccion20A, df_balanced, X_train):
    
    global nota 
    # Inicialización de notas
    nota2 = nota3 = nota3A = nota4 = nota5 = nota6 = nota7 = nota8 = nota9 = 0
    nota10 = nota11 = nota12 = nota13 = nota14 = nota15 = nota16 = nota17 = nota18 = 0
    nota20 = nota20A = nota21 = nota22 = 0

    # INSTRUCCION 2
    try:
        df_nps
        print("INTRUCCION 2: Cargo correctamente los dataframe")
        nota2 = 1
    except NameError:
        print("INTRUCCION 2: No realizó la carga")
        nota2 = 0
    
    # INSTRUCCION 3
    if df_calidad.shape == (1000, 8):
        print("INTRUCCION 3: El DataFrame df_calidad tiene la forma correcta: (1000, 8).")
        nota3 = 1
    else:
        print(f"INTRUCCION 3: El DataFrame df_calidad tiene una forma diferente: {df_calidad.shape}.")
        nota3 = 0
    
    # INSTRUCCION 3A
    try:
        nps_percentage
        print("INSTRUCCION 3A: Se realizó el gráfico correctamente")
        nota3A = 1
    except NameError:
        print("INSTRUCCION 3A: No realizó el gráfico")
        nota3A = 0
    
    # INSTRUCCION 4
    if respuesta1 == "":
        print("INSTRUCCION 4: No analizó el gráfico de conteo de las NPS y está vacía.")
        nota4 = 0
    else:
        print("INSTRUCCION 4: Sí analizó la gráfica de NPS.")
        nota4 = 1
    
    # INSTRUCCION 5
    if total_diferentes != -50:
        print("INSTRUCCION 5: El valor NO corresponde al valor real de diferencia.")
        nota5 = 0
    else:
        print("INSTRUCCION 5: Es correcto el valor de diferencia de tamaños de los dataframe")
        nota5 = 1   
    
    # INSTRUCCION 6
    if seleccion8 == "Que hay nulos":
        print("INSTRUCCION 6: Correcto hay nulos")
        nota6 = 1
    else:
        print('INSTRUCCION 6: La respuesta es incorrecta. Porque si hay nulos')
        nota6 = 0
    
    # INSTRUCCION 7
    try:
        Cantidad_soporte
        print("INSTRUCCION 7: Se realizó el conteo")
        nota7 = 1
    except NameError:
        print("INSTRUCCION 7: No realizó el conteo")
        nota12 = 0
    
    # INSTRUCCION 8
    try:
        df_final
        print("INSTRUCCION 8: Se unió correctamente los dos dataframe")
        nota8 = 1
    except NameError:
        print("INSTRUCCION 8: No realizó la unión")
        nota12 = 0
    
    # INSTRUCCION 9
    try:
        df_final["ValorNPS"]
        print("INSTRUCCION 9: El ValorNPS NO fue borrado")
        nota9 = 0
    except KeyError:
        print("INSTRUCCION 9: Sí fue borrado")
        nota9 = 1

    # INSTRUCCION 10 
    print("pase" 1)
    if not label.empty:
        print("INSTRUCCION 10: Gráfico tipo pie se hizo correctamente")
        nota10 = 1
    else:
        print("INSTRUCCION 10: No realizó la gráfica")
        nota10=0
        print("pase 2")
    # INSTRUCCION 11
    try:
        nulos 
        print("INSTRUCCION 11: Si listó los nulos")
        nota11 = 1
        
    except KeyError:
        print("INSTRUCCION 11: No listó los nulos.")
        nota11 = 0
    print("pase3")
    # INSTRUCCION 12
    if seleccion12 == "Soporte":
        print("INSTRUCCION 12: Fue borrada la columna Soporte")
        nota12 = 1
    else:
        print("INSTRUCCION 12: No fue borrada la columna soporte")
        nota12 = 0
    
    # INSTRUCCION 13
    if num_registros_quedan == 982:
        print("INSTRUCCION 13: Fueron borrados los que tenían más de 2 nulos")
        nota13 = 1
    else:
        print("INSTRUCCION 13: No fueron borrados los que tienen más de dos nulos")
        nota13 = 0
    
    # INSTRUCCION 14
    if totalnulos == 0:
        print("INSTRUCCION 14: Fueron imputados todos los nulos")
        nota14 = 1
    else:
        print("INSTRUCCION 14: No fueron imputados todos los nulos")
        nota14 = 0
    
    # INSTRUCCION 15
    try:
        df_final_sinnulo['NPS']
        print("INSTRUCCION 15: El campo NPS no fue borrado")
        nota15 = 0
    except KeyError:
        print("INSTRUCCION 15: El campo NPS fue borrado")
        nota15 = 1
        
    # INSTRUCCION 16
    try:
        df_final_sinnulo['Tipo_Canal']
        print("INSTRUCCION 16: El campo Tipo Canal no fue borrado")
        nota16 = 0
    except KeyError:
        print("INSTRUCCION 16: El campo tipo canal fue borrado")
        nota16 = 1
        
    # INSTRUCCION 17
    try:
        df_final_sinnulo['ID_Cliente']
        print("INSTRUCCION 17: El campo ID Cliente no fue borrado")
        nota17 = 0
    except KeyError:
        print("INSTRUCCION 17: El campo ID Cliente fue borrado")
        nota17 = 1
         
    # INSTRUCCION 18
    # Verificar si el archivo existe
    archivo = './encoderNPS.joblib'
    if os.path.isfile(archivo):
        print("INSTRUCCION 18: Se guardaron los archivos de los modelos de numerización")
        nota18 = 1
    else:
        print("INSTRUCCION 18: No existen los archivos de los modelos de numerización")
        nota18 = 0
    
    # INSTRUCCION 20
    try:
        correlation_matrix
        print("INSTRUCCION 20: Se realizó la matriz de correlación")
        nota20 = 1
    except NameError:
        print("INSTRUCCION 20: No realizó la matriz de correlación")
        nota20 = 0
            
    # INSTRUCCION 20A
    if seleccion20A == 'Ninguna':
        print("INSTRUCCION 20A: La respuesta está correcta, es Ninguna Columna")
        nota20A = 1
    else:
        print("INSTRUCCION 20A: La respuesta NO está correcta, no es Ninguna Columna")
        nota20A = 0
        
    # INSTRUCCION 21
    try:
        df_balanced
        print("INSTRUCCION 21: Se hizo el balanceo")
        nota21 = 1
    except NameError:
        print("INSTRUCCION 21: No se hizo el balanceo")
        nota21 = 0
        
    # INSTRUCCION 22
    try:
        X_train
        print("INSTRUCCION 22: Se realizó la partición")
        nota22 = 1
    except NameError:
        print("INSTRUCCION 22: No se hizo la partición")
        nota22 = 0
        
    # Calcular nota final
    nota = (nota2 + nota3 + nota3A + nota4 + nota5 + nota6 + nota7 + nota8 +
            nota9 + nota10 + nota11 + nota12 + nota13 + nota14 + nota15 + 
            nota16 + nota17 + nota18 + nota20 + nota20A + nota21 + nota22) / 22.0

    # Determinar el resultado basado en la nota
    if nota < 3:
        resultado = "https://github.com/adiacla/examen2026/blob/main/rechazado.JPG"
    elif nota < 3.9:
        resultado = "https://github.com/adiacla/examen2026/blob/main/restriccion.JPG"
    else:
        resultado = "https://github.com/adiacla/examen2026/blob/main/aprobado.JPG"   

    return nota, resultado
