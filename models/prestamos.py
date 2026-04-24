from typing import Tuple

from db.db import cursor
from lib.biblioteca import Usuario, Libro
from models.libros import LibroModel

class PrestamoModel:
    
    @staticmethod
    def prestar_libro(usuario: Usuario, libro: Libro) -> bool:
        if LibroModel.obtener_libro_por_id(libro.id) == None:
            return False
        sql = "INSERT INTO Prestamo (usuario_id, libro_id) VALUES (?, ?)"
        try:
            usuario.prestamos[libro.id] = libro
            libro.libre = False
            cursor.execute(sql, (usuario.id, libro.id))
            LibroModel.editar_libro(libro)
            return True
        except:
            if not usuario.prestamos.get(libro.id) is None:
                usuario.prestamos.pop(libro.id)
            libro.libre = True
            return False
    
    @staticmethod
    def obtener_prestamos() -> list[Tuple[int, int]] | None:
        sql = "SELECT * FROM Prestamo"
        prestamos = []
        try:
            filas = cursor.execute(sql)
            for fila in filas:
                prestamos.append((fila[0], fila[1]))
            return prestamos
        except:
            return None
    