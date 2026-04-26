from lib.biblioteca import Biblioteca
from app import App

biblioteca = Biblioteca()

app = App(biblioteca)

app.mainloop()