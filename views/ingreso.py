import customtkinter as ctk

from lib.biblioteca import Biblioteca, Usuario
from lib.config import fuentes

from views.view import View
from views.dialogs import enviar_popup

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class IngresoView(View): 
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        
        self.generar_ui()
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        title = ctk.CTkLabel(self.frame, text="Ingresar Usuario", font=fuentes["title_font"])
        title.pack(pady=20)
        
        ctk.CTkLabel(self.frame, text="Nombre de usuario", font=fuentes["normal_font"]).pack(pady=5, padx=40, anchor="w")
        self.nombre_input = ctk.CTkEntry(self.frame, placeholder_text="Ingrese su nombre", font=fuentes["input_font"])
        self.nombre_input.pack(pady=10, padx=40, anchor="w", fill="x")
        self.nombre_input.bind('<Return>', self.manejar_enter)
        
        ctk.CTkLabel(self.frame, text="Contraseña", font=fuentes["normal_font"]).pack(pady=5, padx=40, anchor="w")
        self.contraseña_input = ctk.CTkEntry(self.frame, placeholder_text="Ingrese su contraseña", font=fuentes["input_font"], show="*")
        self.contraseña_input.pack(pady=10, padx=40, anchor="w", fill="x")
        self.contraseña_input.bind('<Return>', self.manejar_enter)  
        
        registrar_button = ctk.CTkButton(self.frame, text="¿No tiene un usuario?", font=fuentes["button_font"], command=lambda: self.app.mostrar_frame_str('RegistroView'), fg_color="transparent")
        registrar_button.pack(pady=10, padx=40, anchor="w")
        
        ingresar_button = ctk.CTkButton(self.frame, text="Ingresar", font=fuentes["button_font"], command=self.ingresar_usuario)
        ingresar_button.pack(pady=10, padx=40, anchor="w", fill="x")
        
    def actualizar_frame(self):
        pass
    
    def ingresar_usuario(self):
        nombre = self.nombre_input.get()
        contraseña = self.contraseña_input.get()
        
        if not nombre or not contraseña:
            enviar_popup(self.app, "Por favor complete todos los campos.")
            return
        
        resultado = self.biblioteca.ingresar_usuario(nombre, contraseña)
        
        if resultado is None:
            enviar_popup(self.app, "Usuario o contraseña incorrectos.")
            return
        
        self.app.usuario = resultado
        
        enviar_popup(self.app, f"Usuario '{nombre}' ingresado exitosamente.", False)
        self.app.vistas_protegidas()
        self.app.pantalla_principal()
    
    def manejar_enter(self, event):
        self.ingresar_usuario()
        
        