 Sistema de Gestión para Bibliotecas

Aplicación de escritorio para administrar una biblioteca: alta de libros, personas, préstamos y devoluciones. Está hecha en Python con wxPython para la interfaz gráfica, y usa archivos JSON como base de datos.

Proyecto desarrollado para la materia Programación Orientada a Objetos (Tecnicatura Superior en Desarrollo Web).


 Funcionalidades


Libros: alta de libros con código autogenerado (LIB0001, LIB0002...) y listado en tabla.
Personas: alta de personas (DNI, nombre, apellido) y listado.
Préstamos: registrar un préstamo eligiendo un libro disponible, una persona y una fecha. El libro pasa a estado Prestado.
Devoluciones: seleccionar un préstamo activo y devolverlo. El préstamo pasa a Devuelto y el libro vuelve a Disponible.
Los datos persisten entre ejecuciones en libros.json, personas.json y prestamos.json.
