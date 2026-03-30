from PIL import Image
from pathlib import Path
    
BASE_DIR = Path(__file__).resolve().parent.parent

imagenes = {
    'libro_icono_light': Image.open(BASE_DIR / 'assets' / 'libro_icono_light.webp'),
    'libro_icono_dark': Image.open(BASE_DIR / 'assets' / 'libro_icono_dark.webp'),
    'usuario_icono_light': Image.open(BASE_DIR / 'assets' / 'usuario_icono_light.png'),
    'usuario_icono_dark': Image.open(BASE_DIR / 'assets' / 'usuario_icono_dark.png'),
}