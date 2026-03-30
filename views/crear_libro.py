import customtkinter as ctk

from lib.config import fuentes
from lib.biblioteca import Biblioteca, LibroInput, formatear_descripcion

from views.view import View
from views.dialogs import enviar_popup

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class CrearLibroView(View): 
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        self.app = controller
    
        self.biblioteca = biblioteca
        
        self.nombre_input = None
        
        self.autor_input = None
        
        self.año_input = None
        
        self.descripcion_input = None
        
        self.generar_ui()
        
    def generar_ui(self):
        title = ctk.CTkLabel(self, text="Crear Libro", font=fuentes["title_font"])
        title.pack(pady=20)
        
        scrollable_frame = ctk.CTkScrollableFrame(self)
        scrollable_frame.pack(fill="both", expand=True, padx=0, pady=0)
        scrollable_frame.grid_columnconfigure(0, weight=1)
        
        nombre_label = ctk.CTkLabel(scrollable_frame, text="Nombre del libro", font=fuentes["normal_font"])
        nombre_label.pack(pady=5, padx=40, anchor="w")
        self.nombre_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el nombre", font=fuentes["input_font"])
        self.nombre_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.nombre_input.bind('<Return>', self.manejar_enter)
        
        autor_label = ctk.CTkLabel(scrollable_frame, text="Nombre del Autor", font=fuentes["normal_font"])
        autor_label.pack(pady=5, padx=40, anchor="w")
        self.autor_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el autor", font=fuentes["input_font"])
        self.autor_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.autor_input.bind('<Return>', self.manejar_enter)
        
        año_label = ctk.CTkLabel(scrollable_frame, text="Año de publicación", font=fuentes["normal_font"])
        año_label.pack(pady=5, padx=40, anchor="w")
        self.año_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el año de publicación", font=fuentes["input_font"])
        self.año_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.año_input.bind('<Return>', self.manejar_enter)
        
        descripcion_label = ctk.CTkLabel(scrollable_frame, text="Descripcion del libro", font=fuentes["normal_font"])
        descripcion_label.pack(pady=5, padx=40, anchor="w")
        self.descripcion_input = ctk.CTkTextbox(scrollable_frame, font=fuentes["input_font"])
        self.descripcion_input.insert("0.0", "Ingrese la descripción del libro")
        self.descripcion_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.descripcion_input.bind('<Return>', self.manejar_enter)
        
        crear_boton = ctk.CTkButton(scrollable_frame, text="Crear Libro", font=fuentes["button_font"], command=self.crear_libro)
        crear_boton.pack(pady=20)
        
    def manejar_enter(self, event):
        if event.state & 0x0001:  # Shift está activo
            return
        self.crear_libro()
        
    def crear_libro(self):
    
        if not self.nombre_input or not self.autor_input or not self.año_input or not self.descripcion_input:
            raise Exception("campos de entrada no inicializados.")
        
        nombre = self.nombre_input.get()
        autor = self.autor_input.get()
        año_input = self.año_input.get()
        descripcion = self.descripcion_input.get("0.0", 'end').strip()
        descripcion = formatear_descripcion(descripcion)
        
        if nombre == "":
            enviar_popup(self.app, "Por favor ingrese el nombre del libro.", True)
            return
        if autor == "":
            enviar_popup(self.app, "Por favor ingrese el nombre del autor del libro.", True)
            return
        try:
            año = int(año_input)
            if año <= 0: raise Exception("Año invalido")
        except:
            enviar_popup(self.app, "Año inválido. Por favor ingrese un año válido.", True)
            return
        if descripcion == "" or descripcion == "Ingrese la descripción del libro":
            enviar_popup(self.app, "Por favor ingrese la descripción del libro.", True)
            return
        
        libro_input = LibroInput(nombre, autor, año, descripcion)

        self.biblioteca.agregar_libro(libro_input)
        enviar_popup(self.app, "Libro añadido exitosamente", False)
        
        self.nombre_input.delete(0, 'end')
        self.autor_input.delete(0, 'end')
        self.año_input.delete(0, 'end')
        self.descripcion_input.delete('0.0', 'end')
        self.descripcion_input.insert("0.0", "Ingrese la descripción del libro")
         
        self.nombre_input.focus()
        
        self.app.actualizar_frames()
        
    def actualizar_frame(self):
        pass
            
    
        
        