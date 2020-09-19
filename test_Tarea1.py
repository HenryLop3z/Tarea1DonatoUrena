
# Henry Ureña Lopez
# 13/9/2020
# Tarea 1 test

# Para el funcionamiento del test se deben descargar
# ambos archivos y mantenerlos en un mismo directorio
# luego abrir el terminal y ejecudar el comando:
# cd C:\Users\USUARIO\Downloads>
# esto por ejemplo si se encuentran en la carpeta de descargas
# y posterior a eso ejecutar el comando: pytest


from main import operaciones
# importa la clase del archivo main.py


class TestClass:  # define la clase para prueba
    def test_1(self):
        # define la prueba 1
        obj = operaciones()
        # llama a obj como la clase operaciones
        assert obj.basic_ops(1, 2, 1) == 3
        # llama a basic_ops con los parámetros 1,2,1
        # y espera que la respuesta sea 3

    def test_2(self):
        obj = operaciones()
        assert obj.basic_ops(1, 3, 2) == -2

    def test_3(self):
        obj = operaciones()
        assert obj.basic_ops(3, 1, 3) == 1

    def test_4(self):
        obj = operaciones()
        assert obj.basic_ops(4, 1, 4) == 5

    def test_5(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 3], [4, 5, 6], 1) == [5, 7, 9]

    def test_6(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 3], [4, 5, 6], 1) == [5, 7, 9]

    def test_7(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 3], [4, 5, 6], 1) == [5, 7, 9]

    def test_8(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 3], [4, 5, 6], 1) == [5, 7, 9]

    def test_9(self):
        obj = operaciones()
        assert obj.basic_ops(4, 5.5, 1) == "EINVAL: Ingrese números enteros"

    def test_10(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 3], [4, 'j', 6], 1) \
               == "EINVAL: Ingrese números enteros"

    def test_11(self):
        obj = operaciones()
        assert obj.basic_ops(1, 130, 1) \
               == "EDQUOT: Ingresar un número entre -127 y 127"

    def test_12(self):
        obj = operaciones()
        assert obj.array_ops([1, 2, 129], [4, 3, 6], 1) \
               == "EDQUOT: Ingresar un número entre -127 y 127"

    def test_13(self):
        obj = operaciones()
        assert obj.basic_ops(1, 3, 7) \
               == "ENOSYS: Ingrese un valor válido (1-4)"
