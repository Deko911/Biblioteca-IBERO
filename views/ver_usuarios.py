import customtkinter as ctk

from lib.biblioteca import Biblioteca, Libro
from lib.imagenes import imagenes
from lib.config import fuentes

from views.view import View

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class VerUsuariosView(View): 

    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        
        self.usuario_icono = ctk.CTkImage(imagenes['usuario_icono_light'], imagenes['usuario_icono_dark'], (100, 100))
        
        self.generar_ui()
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        label = ctk.CTkLabel(self.frame, text="Ver Usuarios", font=fuentes["title_font"])
        label.pack(pady=20)
        
        usuarios_frame = ctk.CTkScrollableFrame(self.frame)
        usuarios_frame.pack(pady=5, fill='both', expand=True)
            
        
        for usuario in self.biblioteca.usuarios:
            usuario_grid = ctk.CTkFrame(usuarios_frame, fg_color='#333333')
            usuario_grid.pack(pady=10, padx=5, fill='x')
            
            usuario_grid.grid_columnconfigure(0, weight=0)
            usuario_grid.grid_columnconfigure(1, weight=1)
            
            icono_usuario = ctk.CTkLabel(usuario_grid, image=self.usuario_icono, text='')
            icono_usuario.grid(row=0, column=0, padx=20, pady=10)
            
            info_usuario = ctk.CTkFrame(usuario_grid, fg_color='transparent')
            info_usuario.grid(row=0, column=1, sticky='w')
            
            ctk.CTkLabel(info_usuario, text=f"Nombre: {usuario.nombre}", font=fuentes["title_font"]).pack(anchor='w', pady=(10, 0))
            
            ctk.CTkLabel(info_usuario, text=f"Prestamos:", font=fuentes["normal_font"]).pack(anchor='w', pady=(10, 0))
            
            if len(usuario.prestamos) == 0:
                ctk.CTkLabel(info_usuario, text="No tiene libros prestados", font=fuentes["details_font"]).pack(anchor='w', padx=20)
            
            libros = ', '.join([libro.nombre for libro in usuario.prestamos.values()])
            libros_label = ctk.CTkLabel(info_usuario, text=libros, font=fuentes["details_font"], justify='left')
            libros_label.pack(anchor='w', padx=20)
            libros_label.configure(wraplength=self.app.width - 400)

            self.detectar_hover(usuario_grid)
            
    def detectar_hover(self, frame: ctk.CTkBaseClass, widget=None):
        if widget is None: widget = frame
        widget.bind("<Enter>", lambda _: hover_usuario(frame))
        widget.bind("<Leave>", lambda _: unhover_usuario(frame))
        for w in widget.winfo_children():
            if isinstance(w, ctk.CTkBaseClass):
                self.detectar_hover(frame, w)

def hover_usuario(frame):
    frame.configure(fg_color='#222222')
    
def unhover_usuario(frame):
    frame.configure(fg_color='#333333')
        