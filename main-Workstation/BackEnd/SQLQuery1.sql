create database workstation

use workstation

create table usuarios (
id int  not null,
nombre varchar (35) not null,
apellido varchar (35) not null,
dni varchar (8) null,
telefono varchar (30) null,
mail varchar (70) null,
fecha_nacimiento date null,
clave_acceso varchar (30) not null,
token int null, 
primary key (id),
)

