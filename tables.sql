DROP TABLE IF EXISTS Prestamo;
DROP TABLE IF EXISTS Libro;
DROP TABLE IF EXISTS Usuario;

CREATE TABLE Usuario(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
);

CREATE TABLE Libro(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    autor TEXT NOT NULL,
    anio INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    libre BOOLEAN NOT NULL CHECK (libre IN (0, 1))
);

CREATE TABLE Prestamo(
    usuario_id INTEGER,
    libro_id INTEGER,
    PRIMARY KEY(usuario_id, libro_id),
    FOREIGN KEY(usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY(libro_id) REFERENCES Libro(id)
);
