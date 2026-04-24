from db.db import cursor
from models.usuarios import UsuarioModel
from models.libros import LibroModel
from models.prestamos import PrestamoModel
from lib.biblioteca import UsuarioInput, LibroInput

usuarios = [
    UsuarioInput("admin", "admin"),
    UsuarioInput("Diego", "diego123"),
    UsuarioInput('Andres', 'andres123'),
    UsuarioInput('Juan', 'juan123')
]

libros = [
    LibroInput("Cien años de soledad", "Gabriel García Márquez", 1967, "Una novela que narra la historia de la familia Buendía a lo largo de varias generaciones en el pueblo ficticio de Macondo. La obra es conocida por su estilo de realismo mágico, donde lo fantástico se mezcla con lo cotidiano, y aborda temas como el amor, la soledad, el poder y la historia de América Latina."),
    LibroInput("El coronel no tiene quien le escriba", "Gabriel García Márquez", 1961, "La novela sigue la vida de un coronel retirado que espera una pensión que nunca llega. A lo largo de la historia, el coronel enfrenta la pobreza, la soledad y la esperanza de recibir su merecida pensión. La obra es una crítica a la burocracia y a las injusticias sociales, y destaca por su estilo narrativo y su profunda exploración de la condición humana."),
    LibroInput("Hamlet", "Shakespeare", 1603, "Una tragedia que sigue la historia del príncipe Hamlet, quien busca vengar la muerte de su padre a manos de su tío Claudio, quien se ha casado con la madre de Hamlet. La obra explora temas como la traición, la locura, la venganza y la moralidad, y es conocida por sus monólogos profundos y su compleja trama."),
    LibroInput("Metamorfosis", "Franz Kafka", 1915, "La novela sigue la historia de Gregor Samsa, un viajante comercial que se despierta uno día para descubrir que ha sido transformado en un insecto. La obra explora temas como la alienación, la responsabilidad y la condición humana, y es conocida por su estilo narrativo y su profunda exploración de la psique humana."),
    LibroInput("Moby Dick", "Herman Melville", 1851, "Una novela que narra la historia del capitán Ahab y su obsesión por cazar a la ballena blanca Moby Dick. La obra explora temas como la naturaleza, la venganza y la condición humana, y es conocida por su estilo narrativo y su profunda exploración de la psique humana."),
    LibroInput("El principito", "Antoine de Saint-Exupéry", 1943, "Una novela que sigue la historia de un pequeño príncipe que visita diferentes planetas. La obra explora temas como el amor, la amistad, la vida y la muerte, y es conocida por su estilo sencillo y su profunda reflexión sobre la condición humana.")
]

prestamos = [
    (0, 0),
    (1, 1),
    (2, 2)
]

def seeder():
    # Crear/Reiniciar Tablas
    f = open('./tables.sql', 'r')
    script = f.read()
    cursor.executescript(script)
    
    # Crear Usuarios
    for usuario in usuarios:
        UsuarioModel.crear_usuario(usuario)
        
    # Crear Libros
    for libro in libros:
        LibroModel.crear_libro(libro)
        
    # Obtener todos los Usuarios    
    getUsuarios = UsuarioModel.obtener_usuarios()
    assert getUsuarios
    
    for usuario in getUsuarios:
        print(usuario.nombre)
        
    print("".center(30, "-"))
        
    # Obtener todos los Libros   
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro)

    print("".center(30, "-"))
        
    ##### PRUEBAS #####
    """ 
        
    # Obtener Usuario por nombre
    usuario_admin = UsuarioModel.obtener_usuario_por_nombre("admin")
    assert usuario_admin 
    
    print(usuario_admin.nombre)
    print("".center(30, "-"))
    
    usuario_no_existente = UsuarioModel.obtener_usuario_por_nombre("Jaime")
    assert not usuario_no_existente 

    # Editar Libro
        
    primerLibro = getLibros[0]
    primerLibro.libre = False
    
    LibroModel.editar_libro(primerLibro)
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    print("".center(30, "-"))
    
    # Eliminar Libro
    
    LibroModel.eliminar_libro(primerLibro.id)
    
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    print("".center(30, "-"))
    
    # Hacer prestamos
    for (usuario_id, libro_id) in prestamos:
        assert PrestamoModel.prestar_libro(getUsuarios[usuario_id], getLibros[libro_id])
    
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    #Obtener Prestamos
    getPrestamos = PrestamoModel.obtener_prestamos()
    assert getPrestamos
    
    print(getPrestamos) """

if __name__ == "__main__":
    seeder()