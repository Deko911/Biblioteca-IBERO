
class Libro:
    def __init__(self, id: int, nombre: str, autor: str, año: int, descripcion: str, libre: bool):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.descripcion = descripcion
        self.libre = libre
        
    def __str__(self) -> str:
        estado = "Disponible" if self.libre else "Prestado"
        return f"Id: {self.id} - Nombre: {self.nombre} - Autor: {self.autor} - Año: {self.año} - Estado: {estado}"
    
    def actualizar_libro(self, input: LibroInput):
        self.nombre = input.nombre
        self.autor = input.autor
        self.año = input.año
        self.descripcion = input.descripcion
        
class LibroInput:
    def __init__(self, nombre: str, autor: str, año: int, descripcion: str):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.descripcion = descripcion
        
class Usuario:
    def __init__(self, id: int, nombre: str, contraseña: str):
        self.id = id
        self.nombre = nombre
        self._contraseña = contraseña
        self.prestamos: dict[int, Libro] = {}
        
class UsuarioInput:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self._contraseña = contraseña
        self.prestamos: dict[int, Libro] = {}
        
class UsuarioSeguro:
    def __init__(self, usuario: Usuario):
        self.id = usuario.id
        self.nombre = usuario.nombre
        self.prestamos = usuario.prestamos

class Biblioteca:
    def __init__(self):
        self._libros: list[Libro] = []
        self._libros_id: dict[int, Libro] = {}
        self._usuarios: dict[int, Usuario] = {}
        self._contador = 0
        self._contador_usuario = 0
        
    @property
    def usuarios(self): 
        usuarios = [UsuarioSeguro(usuario) for usuario in self._usuarios.values()]
        return usuarios

    @property
    def libros(self):
        return self._libros
        
    def crear_libro(self, input: LibroInput):
        libro = Libro(self._contador, input.nombre, input.autor, input.año, input.descripcion, True)
        self._contador += 1
        return libro
        
    def agregar_libro(self, libro: LibroInput):
        nuevo_libro = self.crear_libro(libro)
        self._libros.append(nuevo_libro)
        self._libros_id[nuevo_libro.id] = nuevo_libro
        
    def obtener_libro(self, id=0):
        return self._libros_id[id]
    
    def editar_libro(self, nuevo_libro: LibroInput, id=0):
        libro = self.obtener_libro(id)
        libro.actualizar_libro(nuevo_libro)
        return libro
    
    def eliminar_libro(self, id=-1):
        if id == -1: return self._libros.pop()
        ids = [libro.id for libro in self._libros]
        idx = ids.index(id)
        libro = self._libros.pop(idx)
        return self._libros_id.pop(libro.id)
    
    def registrar_usuario(self, input: UsuarioInput):
        usuario = Usuario(self._contador_usuario, input.nombre, input._contraseña)
        self._usuarios[self._contador_usuario] = usuario
        self._contador_usuario += 1
        return usuario
        
    def ingresar_usuario(self, nombre: str, contraseña: str):
        usuario = None
        for u in self._usuarios.values():
            if u.nombre == nombre:
                usuario = u
                
        if usuario == None:
            return None
        
        if usuario._contraseña != contraseña:
            return None
        
        return usuario
    
    def prestar_libro(self, libro_id: int, usuario: Usuario):
        libro = self.obtener_libro(libro_id)
        if not libro.libre: return False
        
        libro.libre = False
        usuario.prestamos[libro.id] = libro
        
        return True
    
    def devolver_libro(self, libro_id: int, usuario: Usuario):
        libro = self.buscar_prestamo(usuario, libro_id)
        if libro is None: return False
        
        libro.libre = True
        usuario.prestamos.pop(libro.id)
        
        return True
    
    def buscar_prestamo(self, usuario: Usuario, libro_id: int):
        return usuario.prestamos.get(libro_id)
    
    def __str__(self) -> str:
        return f"Biblioteca Ibero \n Libros: \n {"\n ".join([f"- {libro}" for libro in self._libros])}"
    
def formatear_descripcion(descripcion: str):
    lineas = descripcion.splitlines()
    return '\n'.join([linea.strip() for linea in lineas])