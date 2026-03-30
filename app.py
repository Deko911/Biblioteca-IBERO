import customtkinter as ctk
import math

#Vistas
from views.view import View
from views.crear_libro import CrearLibroView 
from views.editar_libro import EditarLibroView 
from views.ver_libros import VerLibrosView
from views.ver_usuarios import VerUsuariosView 
from views.detalles_libro import DetallesLibroView
from views.ingreso import IngresoView
from views.registro import RegistroView

from lib.biblioteca import Biblioteca, Usuario
from lib.config import fuentes   

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self, biblioteca: Biblioteca):
        super().__init__()
        
        self.width = 800
        self.height = 500
        
        self.biblioteca = biblioteca
        self.usuario: Usuario | None = None

        self.title("Biblioteca Ibero")
        self.geometry("800x500")
        self.minsize(width=self.width, height=self.height)
        
        self.bind('<Configure>', lambda e: self.configuracion_ventana(e))
        
        self.frames: dict[type, View] = {}
        
        self.vistas_usuario()
        
    
    def vistas_usuario(self):
        self.limpiar_ui()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
        
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        for F in (IngresoView, RegistroView):
            frame = F(self.container, self, self.biblioteca)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.mostrar_frame(IngresoView)
        

    def vistas_protegidas(self):
        self.limpiar_ui()
        if not self.usuario: return
        
        # Layout principal (2 columnas)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, fg_color='#222222')
        self.sidebar.grid(row=0, column=0, sticky="ns", ipadx=10)

        # Contenedor de vistas
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        for F in (CrearLibroView, EditarLibroView, VerLibrosView, VerUsuariosView, DetallesLibroView):
            frame = F(self.container, self, self.biblioteca)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        ctk.CTkLabel(self.sidebar, text=f"Bienvenido, {self.usuario.nombre}", font=fuentes["normal_font"]).pack(pady=(30, 10), padx=10)

        # Botones del sidebar
        ctk.CTkButton(self.sidebar, text="Ver libros",
                      command=lambda: self.mostrar_frame(VerLibrosView)).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Crear libro",
                      command=lambda: self.mostrar_frame(CrearLibroView)).pack(pady=10)
        
        ctk.CTkButton(self.sidebar, text="Ver usuarios",
                      command=lambda: self.mostrar_frame(VerUsuariosView)).pack(pady=10)
        
        ctk.CTkButton(self.sidebar, text="Cerrar sesión", fg_color="#d32525", hover_color="#b60000",
                      command=lambda: self.cerrar_sesion()).pack(side="bottom", pady=20)

        # Vista inicial
        self.mostrar_frame(VerLibrosView)

    def mostrar_frame(self, cont: type) -> None:
        frame = self.frames[cont]
        frame.tkraise()
    
    def mostrar_frame_str(self, cont: str) -> None:
        for key in self.frames.keys():
            if key.__name__ == cont:
                self.mostrar_frame(key)
                return

        raise Exception(f"No se encontró la vista '{cont}'")
        
    def actualizar_frames(self):
        for view in self.frames.values():
            view.actualizar_frame()
            
    def configuracion_ventana(self, event):
        if event.widget == self:
            [width, height] = [event.width, event.height]
            dif_w = math.fabs(self.width - width)
            dif_h = math.fabs(self.height - height)
            if dif_h > 25 or dif_w > 25:
                self.width = width
                self.height = height
                self.actualizar_frames()
                
    def mostrar_libro(self, libro):
        self.frames[DetallesLibroView].ver_libro(libro) # type: ignore
        self.mostrar_frame(DetallesLibroView)
        
    def editar_libro(self, libro):
        self.frames[EditarLibroView].editar_libro(libro) # type: ignore
        self.mostrar_frame(EditarLibroView)
        
    def pantalla_principal(self):
        self.mostrar_frame(VerLibrosView)
        
    def limpiar_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.frames.clear()
        
    def cerrar_sesion(self):
        self.usuario = None
        self.vistas_usuario()