# Biblioteca - Proyecto de Estructuras de Datos

## Descripción General

Este proyecto es una aplicación de gestión de biblioteca desarrollada como parte de la asignatura de Estructuras de Datos en la Fundación Universitaria Iberoamericana, carrera de Ingeniería de Software. El objetivo principal es aplicar conceptos de estructuras de datos lineales, específicamente arreglos, para la administración de libros y usuarios.

## Integrantes del Grupo
- **Andrés Camilo Pérez Valderrama**
- **Diego Mauricio Ortiz Sánchez**
- **Juan Pablo Carrillo Chavez**

## Características Principales
- Registro y autenticación de usuarios.
- Visualización, creación, edición y eliminación de libros.
- Gestión de usuarios y libros mediante arreglos.
- Interfaz gráfica para interacción amigable.
- Datos de prueba incluidos para usuarios y libros.

## Estructura de Archivos

```
├── app.py                  # Archivo principal de la aplicación, coordina las vistas
├── main.py                 # Punto de entrada principal del sistema
├── requirements.txt        # Dependencias del proyecto
├── assets/                 # Recursos estáticos (imágenes, íconos, etc.)
├── lib/
│   ├── biblioteca.py       # Lógica principal de la biblioteca (gestión de libros y usuarios)
│   ├── config.py           # Configuración general del sistema
│   └── imagenes.py         # Gestión de imágenes
├── views/
│   ├── crear_libro.py      # Vista para crear libros
│   ├── detalles_libro.py   # Vista de detalles de un libro
│   ├── dialogs.py          # Diálogos y ventanas emergentes
│   ├── editar_libro.py     # Vista para editar libros
│   ├── ingreso.py          # Vista de inicio de sesión
│   ├── registro.py         # Vista de registro de usuarios
│   ├── ver_libros.py       # Vista para listar libros
│   ├── ver_usuarios.py     # Vista para listar usuarios
│   └── view.py             # Clase base para todas las vistas
```

## Instalación y Ejecución

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Biblioteca-Ibero
   ```
2. **Crear y activar un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   source .venv/bin/activate  # En Linux/Mac
   ```
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

## Datos de Prueba

### Usuarios de Prueba
- **admin** / **admin** (Administrador)
- **Diego** / **diego123**
- **Andres** / **andres123**
- **Juan** / **juan123**

### Libros de Prueba
- "Cien años de soledad" - Gabriel García Márquez
- "El coronel no tiene quien le escriba" - Gabriel García Márquez
- "Hamlet" - Shakespeare
- "Metamorfosis" - Franz Kafka
- "Moby Dick" - Herman Melville
- "El principito" - Antoine de Saint-Exupéry

Estos usuarios y libros están precargados para facilitar las pruebas y la exploración de la aplicación.

## Notas Técnicas
- El proyecto utiliza **arreglos** como estructura de datos principal para almacenar y gestionar la información de usuarios y libros.
- No se utiliza una base de datos externa; toda la información se mantiene en memoria durante la ejecución.
- El código está organizado en módulos para separar la lógica, la configuración y las vistas.

## Licencia
Fundación Universitaria Iberoamericana - Ingeniería de Software
