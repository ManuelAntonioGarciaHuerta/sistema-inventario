class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar(self):
        texto = (f"Código: {self.codigo} | Nombre: {self.nombre} | "
                 f"Precio: {self.precio} | Existencia: {self.existencia}")
        print(texto)
        return texto