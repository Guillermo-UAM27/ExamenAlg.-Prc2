class Paciente:
    def _init_(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo
        self.recetas = Pila()  # Pila para el historial de recetas del paciente

class Pila:
    def _init_(self):
        self.elementos = []
    #Funcion para guardar elementos en la cima de la pila
    def apilar(self, elemento):
        self.elementos.append(elemento)
    #Funcion para quitar los elementos del tope de la pila
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    #Funcion que comprueba si la pila esta vacia para evitar errores
    def esta_vacia(self):
        return len(self.elementos) == 0
    #el nombre de la funcion lo delata se usa para ver el tope
    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None
    
    def obtener_todos(self):
        return self.elementos[::-1]  # Devuelve en orden cronológico

class Cola:
    def _init_(self):
        self.elementos = []
    #Se usa para agregar elementos a la cola
    def encolar(self, elemento):
        self.elementos.append(elemento)
    #Esta funcion quita el primer elemento anadido primero en entrar primero en salir
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    #Funcion que comprueba si la cola esta vacia para evitar errores
    def esta_vacia(self):
        return len(self.elementos) == 0
    #El nombre de la funcion lo delata
    def obtener_todos(self):
        return self.elementos
