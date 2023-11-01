import sqlite3


conexion = sqlite3.connect('base.db')

miCursor = conexion.cursor()

conexion.execute("create table usuarios (id int, nombre varchar (35), apellido varchar (35), dni varchar (8), telefono varchar (30), mail varchar (70), fecha_nacimiento date, clave_acceso varchar (30), token int null )")
