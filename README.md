# Curso de Django Rest Framework




Activamos el ambiente virtual

Instalamos django y restframework


## Vistas de Django Rest Framework

Tenemos 2 maneras de mostrar la información de nuestros modelos en el API

1. API VIEW 
    * Más control sobre lógica
    * Buenos para lógica compleja
    * Llamar otras APIS
    * Trabajar con archivos locales

2. ViewSet

### ¿Cuándo usar Api Views?

* Si necesitas control de lógica
* Procesos de archivos y renderizar respuesta asincrona
* Llamado a otros APIS/servicios
* Acceso a archivos locales o datos

### ¿Qué son los ViewSets?

Usa funciones de operadores de los modelos

* list() # Enlistar objetos
* create() # Crea objetos
* retrieve() # Obtiene objetos específicos 
* update() # Actualiza un objeto
* partial_update() # Hace una actualización parcial
* destroy() # Destruye un objeto

Se encargan de la lógica común
Son buenas para las operaciones estándar de las bases de datos
Forma más rápida de hacer una interfaz con la bade de datos

## ¿Cuándo usamos ViewSets?

* Hacer operacione simples, como borrar, leer o crear
* Usamos cuando queremos hacer una APi simple
* Permite poca personalización de lógica
* Trabaja con estructura de datos normales

## Api para perfil de usuario

¿Qué debemos hacer?

1. Crear Nuevo Perfil
    * Maneja registro nuevos usuarios
    * Valida datos de perfil

2. Enlistar perfiles existentes
    * Buscar perfiles
    * Email y Nombre

3. Ver perfil especifico
    * ID de perfil

4. Actualiza perfil de usuarios logeados

1:04:00
