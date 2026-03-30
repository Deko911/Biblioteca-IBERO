import customtkinter as ctk

from lib.biblioteca import Biblioteca

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class View(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca) -> None:
        super().__init__(parent)
    
    def generar_ui(self):
        pass
    
    def actualizar_frame(self):
        self.generar_ui()
    
    