import customtkinter as ctk

import customtkinter as ctk

class ConfirmDialog(ctk.CTkToplevel):
    def __init__(self, master, message="¿Estás seguro?"):
        super().__init__(master)

        self.title("Confirmación")
        self.geometry("300x150")
        self.resizable(False, False)

        self.result = None

        label = ctk.CTkLabel(self, text=message)
        label.pack(pady=20)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        btn_yes = ctk.CTkButton(frame, text="Sí", command=self.yes)
        btn_yes.grid(row=0, column=0, padx=10)

        btn_no = ctk.CTkButton(frame, text="No", command=self.no)
        btn_no.grid(row=0, column=1, padx=10)

        self.grab_set()  # Bloquea la ventana principal

    def yes(self):
        self.result = True
        self.destroy()

    def no(self):
        self.result = False
        self.destroy()
        
import customtkinter as ctk

class PopUpDialog(ctk.CTkToplevel):
    def __init__(self, master, message="Error", is_error=True):
        super().__init__(master)

        self.title("Error" if is_error else "Info")
        self.geometry("300x150")
        self.resizable(False, False)

        self.result = None

        label = ctk.CTkLabel(self, text=message)
        label.pack(pady=20)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)

        btn = ctk.CTkButton(frame, text="Aceptar", command=self.destroy)
        btn.pack(ipadx=10)

        self.grab_set()  # Bloquea la ventana principal

def enviar_confirmacion(app: ctk.CTk, msg: str):
    dialog = ConfirmDialog(app, msg)
    app.wait_window(dialog)
    return dialog.result 

def enviar_popup(app: ctk.CTk, msg: str, is_error=True):
    dialog = PopUpDialog(app, msg, is_error)
    dialog.bind('<Return>', lambda e: dialog.destroy())
    app.wait_window(dialog)    
