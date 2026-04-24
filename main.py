import customtkinter as ctk

from lib.biblioteca import Biblioteca, UsuarioInput
from lib.biblioteca import LibroInput
from app import App

biblioteca = Biblioteca()

admin = UsuarioInput("admin", "admin")
biblioteca.registrar_usuario(admin)  

usuario1 = UsuarioInput("Diego", "diego123")
biblioteca.registrar_usuario(usuario1)

usuario2 = UsuarioInput('Andres', 'andres123')
biblioteca.registrar_usuario(usuario2)

usuario3 = UsuarioInput('Juan', 'juan123')
biblioteca.registrar_usuario(usuario3)

libro1 = LibroInput("Cien años de soledad", "Gabriel García Márquez", 1967, "Una novela que narra la historia de la familia Buendía a lo largo de varias generaciones en el pueblo ficticio de Macondo. La obra es conocida por su estilo de realismo mágico, donde lo fantástico se mezcla con lo cotidiano, y aborda temas como el amor, la soledad, el poder y la historia de América Latina.")
libro2 = LibroInput("El coronel no tiene quien le escriba", "Gabriel García Márquez", 1961, "La novela sigue la vida de un coronel retirado que espera una pensión que nunca llega. A lo largo de la historia, el coronel enfrenta la pobreza, la soledad y la esperanza de recibir su merecida pensión. La obra es una crítica a la burocracia y a las injusticias sociales, y destaca por su estilo narrativo y su profunda exploración de la condición humana.")
libro3 = LibroInput("Hamlet", "Shakespeare", 1603, "Una tragedia que sigue la historia del príncipe Hamlet, quien busca vengar la muerte de su padre a manos de su tío Claudio, quien se ha casado con la madre de Hamlet. La obra explora temas como la traición, la locura, la venganza y la moralidad, y es conocida por sus monólogos profundos y su compleja trama.")
libro4 = LibroInput("Metamorfosis", "Franz Kafka", 1915, "La novela sigue la historia de Gregor Samsa, un viajante comercial que se despierta uno día para descubrir que ha sido transformado en un insecto. La obra explora temas como la alienación, la responsabilidad y la condición humana, y es conocida por su estilo narrativo y su profunda exploración de la psique humana.")
libro5 = LibroInput("Moby Dick", "Herman Melville", 1851, "Una novela que narra la historia del capitán Ahab y su obsesión por cazar a la ballena blanca Moby Dick. La obra explora temas como la naturaleza, la venganza y la condición humana, y es conocida por su estilo narrativo y su profunda exploración de la psique humana.")
libro6 = LibroInput("El principito", "Antoine de Saint-Exupéry", 1943, "Una novela que sigue la historia de un pequeño príncipe que visita diferentes planetas. La obra explora temas como el amor, la amistad, la vida y la muerte, y es conocida por su estilo sencillo y su profunda reflexión sobre la condición humana.")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)
biblioteca.agregar_libro(libro6)

app = App(biblioteca)

app.mainloop()