
'''
Henry Ureña Lopez
18/9/2020
Tarea 1
'''


class operaciones:  # Define la clase operaciones
    '''
    Método basic ops:
    los parámetros de entrada son dos números
    a y b enteros y un número n de selección
    verifica que los números sean válido
    y dependiendo del numero n realiza una operación
    '''
    def basic_ops(self, a, b, n):  # define el método basic_ops
        if isinstance(a, int) and isinstance(b, int) and isinstance(n, int):
            # pregunta si a b y n son números enteros
            if a in range(-127, 128) and b in range(-127, 128):
                # pregunta si a y b están en el rango de -127 a 127
                if n == 1:  # si n es la opción 1
                    # si se selecciona la suma esta es su salida
                    return int(a) + int(b)
                elif n == 2:  # si n es la opción 2
                    # si se selecciona la resta esta es su salida
                    return int(a) - int(b)
                elif n == 3:  # si n es la opción 3
                    # si se selecciona la AND esta es su salida
                    return int(a) & int(b)
                elif n == 4:  # si n es la opción 4
                    # si se selecciona la OR esta es su salida
                    return int(a) | int(b)
                else:  # si n no es una de las opciones de 1 a 4
                    # presenta un error
                    return "ENOSYS: Ingrese un valor válido (1-4)"
            else:  # si a y b no está en el rango de -127 a 127
                # presenta un error diferente
                return "EDQUOT: Ingresar un número entre -127 y 127"
        else:  # si las entradas no son números enteros
            # presenta un error diferente
            return "EINVAL: Ingrese números enteros"

    def array_ops(self, a, b, n):  # define el método array_ops
        L3 = []  # crea una lista vacía para la respuesta de salida
        ext = operaciones()  # parámetros de los métodos
        for i, w in enumerate(a):
            # hace un recorrido a la lista del tamaño de la lista a
            L3.append(ext.basic_ops(a[i], b[i], n))
            # agrega a la lista el resultado de la operación
            # segun el parámetro n y
            # llama al método basic_ops con los parámetros
            # de cada elemento de la lista
            if isinstance(L3[i], str):
                # pregunta si ubo un error con las variables
                return ext.basic_ops(a[i], b[i], n)
                # si existe error lo retorna y acaba el ciclo
        return L3  # al finalizar el ciclo muestra el resultado de la lista
