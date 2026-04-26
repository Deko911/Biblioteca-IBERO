from lib.tipos import Libro
from typing import Tuple

class LibroArbol:
    def __init__(self):
        self.ramas: dict[str, LibroArbol] = {}
        self.libro: Libro | None = None
        
    def _insertar_libro(self, libro: Libro, nombre: str):
        # Si el nombre quedó vacio, el libro se guarda en la rama actual y termina la función
        if nombre == "":
            self.libro = libro
            return
        
        # Buscamos la rama del caracter o la creamos en caso de no existir
        caracter = "" if nombre == "" else nombre[0].lower()
        rama = self.ramas.get(caracter)
        if rama is None:
            rama = LibroArbol()
            self.ramas[caracter] = rama
            
        # Insertamos el resto del nombre a la rama para continuar con la recursión
        rama._insertar_libro(libro, nombre[1:])
        
    
    def insertar_libro(self, libro: Libro):
        self._insertar_libro(libro, libro.nombre)
    
    def buscar_interseccion(self, nombre: str, ultima = None, ultimo_caracter='') -> Tuple[LibroArbol, str] | None:
        if ultima is None:
            ultima = self
            ultimo_caracter = nombre[0]
        # Buscamos la rama del caracter, devolvemos None en caso de no existir
        caracter = "" if nombre == "" else nombre[0]
        rama = self.ramas.get(caracter)
        if rama is None:
            return None
        
        resto = nombre[1:]
        
        # Si la rama tiene mas de un subarbol, se asigna como ultima rama
        if len(rama.ramas) > 1:
            ultima = rama
            ultimo_caracter = '' if resto == "" else resto[0]
        
        # Si la rama contiene el libro a buscar y tiene algun subarbol, se asigna como ultima rama
        if not rama.libro is None and len(rama.ramas) > 0:
            ultima = rama
            ultimo_caracter = '' if resto == "" else resto[0]

        # Si no quedan caracteres, se devuelve lo encontrado
        if resto == "":        
            return (ultima, ultimo_caracter)
        
        # Seguimos buscando el resto en la rama
        return rama.buscar_interseccion(resto, ultima, ultimo_caracter)
    
    def buscar_rama(self, nombre: str) -> LibroArbol | None:
        # Buscamos la rama del caracter, devolvemos None en caso de no existir
        caracter = "" if nombre == "" else nombre[0].lower()
        rama = self.ramas.get(caracter)
        if rama is None:
            return None
        
        # Si la rama contiene un libro y el resto esta vacio, devolvemos dicha rama
        resto = nombre[1:]
        if not rama.libro is None and resto == "":
            return rama
        
        # Seguimos buscando el resto en la rama
        return rama.buscar_rama(resto)
    
    def buscar_libro(self, nombre: str) -> Libro | None:
        # Buscamos la rama del caracter, devolvemos None en caso de no existir
        caracter = "" if nombre == "" else nombre[0].lower()
        rama = self.ramas.get(caracter)
        if rama is None:
            return None
        
        # Si la rama contiene un libro y el resto esta vacio, devolvemos dicho libro
        resto = nombre[1:]
        if not rama.libro is None and resto == "":
            return rama.libro
        
        # Seguimos buscando el resto en la rama
        return rama.buscar_libro(resto)
    
    def _buscar_libro_por_sufijo(self, sufijo: str, resultado=[]) -> list[Libro]:
        # Si nos hemos quedado sin más caracteres, buscaremos en todas las ramas y adjuntaremos todos los libros que encuentre al resultado
        if sufijo == "":
            if not self.libro is None:
                resultado.append(self.libro)
            for rama in self.ramas.values():
                resultado = rama._buscar_libro_por_sufijo(sufijo[1:], resultado)
            return resultado
        
        # Buscamos la rama del caracter, devolvemos un array vacio en caso de no existir
        caracter = sufijo[0]
        rama = self.ramas.get(caracter)
        if rama is None:
            return []
        
        return rama._buscar_libro_por_sufijo(sufijo[1:], resultado)
    
    def buscar_libro_por_sufijo(self, sufijo: str):
        return self._buscar_libro_por_sufijo(sufijo.lower(), [])

    def eliminar_libro(self, libro: Libro):        
        # Buscamos la ultima interseccion
        inter = self.buscar_interseccion(libro.nombre.lower(), None)
        if inter is None:
            return
        
        inter, idx = inter
        # Si el indice esta vacio, eliminamos el libro de la rama
        if idx == "":
            inter.libro = None
            return
        
        # De lo contrario, eliminamos todo el subarbol de la rama
        inter.ramas.pop(idx)
        
    def editar_libro(self, anterior_libro: Libro, libro: Libro):
        self.eliminar_libro(anterior_libro)
        self.insertar_libro(libro)

    def __str__(self) -> str:
        return f"[{", ".join([f"{rama} {not self.ramas[rama].libro is None}, {str(self.ramas[rama])}" for rama in self.ramas])}]"
