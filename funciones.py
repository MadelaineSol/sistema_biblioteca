import wx
import json
import os
# import random
# import string


class Libro:
    def cargar_nuevo_libro(self,event):
       

     
     self.dlg = self.formulario_nuevo_libro()
     self.dlg.Show()




    def formulario_nuevo_libro(self):
         

        frame = wx.Frame(None)

        panel = wx.Panel(frame)

        # texto = wx.StaticText(panel, label="ventana de carga")
         

        

        titulo = wx.StaticText(panel, label="Gestión de Libros")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(titulo, 0, wx.ALL, 10)



        sizer.Add(wx.StaticText(panel, label="Título"))
        self.txt_titulo = wx.TextCtrl(panel)
        sizer.Add(self.txt_titulo, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Código"))

        self.txt_codigo = wx.TextCtrl(panel,value=self.generar_codigo_libro(),style=wx.TE_READONLY)

        sizer.Add(self.txt_codigo, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Autor"))
        self.txt_autor = wx.TextCtrl(panel)
        sizer.Add(self.txt_autor, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Genero"))
        self.txt_genero = wx.TextCtrl(panel)
        sizer.Add(self.txt_genero, 0, wx.EXPAND | wx.ALL, 5)


        b = wx.Button(panel, label="Guardar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.Click, b)

        b.SetDefault()
        b.SetSize(b.GetBestSize())


        c = wx.Button(panel, label="Cancelar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.cerrar_ventana, c)

        c.SetDefault()
        c.SetSize(b.GetBestSize())

        sizer.Add(b, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(c, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)#esta linea es clave para q se vean los input, estube renegando mucho para que se vean los inputs que puse y era q me faltaba esta linea




        
        return frame
    


    def Click(self, event):

        titulo = self.txt_titulo.GetValue()
        codigo = self.txt_codigo.GetValue()
        autor = self.txt_autor.GetValue()
        genero = self.txt_genero.GetValue()

        print("Título:", titulo)
        print("Codigo:", codigo)
        print("Autor:", autor)
        print("Genero:", genero)

        self.guardar_libro()


        wx.MessageBox(
        "Libro guardado exitosamente!",
        "Éxito",
        wx.OK | wx.ICON_INFORMATION
    )

        self.dlg.Close()




    def guardar_json(self, libro):
   


        if not os.path.exists("libros.json"):
            with open("libros.json", "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

   
        with open("libros.json", "r", encoding="utf-8") as archivo:
            libros = json.load(archivo)

  
        libros.append(libro)

        with open("libros.json", "w", encoding="utf-8") as archivo:
            json.dump(libros, archivo, indent=4, ensure_ascii=False)





    def guardar_libro(self):

     libro = {
        "titulo": self.txt_titulo.GetValue(),
        "codigo": self.txt_codigo.GetValue(),
        "autor": self.txt_autor.GetValue(),
        "genero": self.txt_genero.GetValue()
    }

     self.guardar_json(libro)





    def generar_codigo_libro(self):

  
        if not os.path.exists("libros.json"):

            with open("libros.json", "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

            return "LIB0001"

    
        with open("libros.json", "r", encoding="utf-8") as archivo:
            libros = json.load(archivo)

        if len(libros) == 0:
            return "LIB0001"

    
        ultimo_numero = len(libros) + 1

        return f"LIB{ultimo_numero:04d}"


    def cerrar_ventana(self, event):
        self.dlg.Close()



    # def cargar_tabla(self):

    #     self.tabla.DeleteAllItems()

    #     if not os.path.exists("libros.json"):
    #         return

    #     with open("libros.json", "r", encoding="utf-8") as archivo:
    #         libros = json.load(archivo)

    #     for libro in libros:

    #         fila = self.tabla.InsertItem(
    #         self.tabla.GetItemCount(),
    #         libro["codigo"]
    #     )

    #     self.tabla.SetItem(fila, 1, libro["titulo"])
    #     self.tabla.SetItem(fila, 2, libro["autor"])
    #     self.tabla.SetItem(fila, 3, libro["genero"])
    #     self.tabla.SetItem(fila, 3, libro["codigo"])




class Personas():


    def cargar_nueva_persona(self,event):
       

     
     self.dlg = self.formulario_nueva_persona()
     self.dlg.Show()




    def formulario_nueva_persona(self):
         

        frame = wx.Frame(None)

        panel = wx.Panel(frame)

        # texto = wx.StaticText(panel, label="ventana de carga")
         

        

        titulo = wx.StaticText(panel, label="Carga de nueva persona")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(titulo, 0, wx.ALL, 10)



        sizer.Add(wx.StaticText(panel, label="Dni"))
        self.txt_dni = wx.TextCtrl(panel)
        sizer.Add(self.txt_dni, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Nombre"))

        self.txt_nombre = wx.TextCtrl(panel)

        sizer.Add(self.txt_nombre, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Apellido"))
        self.txt_apellido = wx.TextCtrl(panel)
        sizer.Add(self.txt_apellido, 0, wx.EXPAND | wx.ALL, 5)

        

        b = wx.Button(panel, label="Guardar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.Click, b)

        b.SetDefault()
        b.SetSize(b.GetBestSize())


        c = wx.Button(panel, label="Cancelar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.cerrar_ventana, c)

        c.SetDefault()
        c.SetSize(b.GetBestSize())

        sizer.Add(b, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(c, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)#esta linea es clave para q se vean los input, estube renegando mucho para que se vean los inputs que puse y era q me faltaba esta linea




        
        return frame
    


    def Click(self, event):

        dni = self.txt_dni.GetValue()
        nombre = self.txt_nombre.GetValue()
        apellido = self.txt_apellido.GetValue()
        

        print("Dni:", dni)
        print("Nombre:", nombre)
        print("Apellido:", apellido)
   

        self.guardar_persona()


        wx.MessageBox(
        "Persona guardado exitosamente!",
        "Éxito",
        wx.OK | wx.ICON_INFORMATION
    )

        self.dlg.Close()




    def guardar_json(self, persona):
   


        if not os.path.exists("personas.json"):
            with open("personas.json", "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

   
        with open("personas.json", "r", encoding="utf-8") as archivo:
            personas = json.load(archivo)

  
        personas.append(persona)

        with open("personas.json", "w", encoding="utf-8") as archivo:
            json.dump(personas, archivo, indent=4, ensure_ascii=False)





    def guardar_persona(self):

     libro = {
        "dni": self.txt_dni.GetValue(),
        "nombre": self.txt_nombre.GetValue(),
        "apellido": self.txt_apellido.GetValue()
        
    }

     self.guardar_json(libro)



    def cerrar_ventana(self, event):
        self.dlg.Close()


class Prestamos ():




    def cargar_nuevo_prestamo(self,event):
       

     
     self.dlg = self.formulario_nuevo_prestamo()
     self.dlg.Show()




    def formulario_nuevo_prestamo(self):
         

        frame = wx.Frame(None)

        panel = wx.Panel(frame)

        # texto = wx.StaticText(panel, label="ventana de carga")
         

        

        titulo = wx.StaticText(panel, label="Carga de nueva prestamo")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(titulo, 0, wx.ALL, 10)



        sizer.Add(wx.StaticText(panel, label="Libro"))
        self.txt_dni = wx.TextCtrl(panel)
        sizer.Add(self.txt_dni, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Persona"))

        self.txt_nombre = wx.TextCtrl(panel)

        sizer.Add(self.txt_nombre, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Fecha"))
        self.txt_apellido = wx.TextCtrl(panel)
        sizer.Add(self.txt_apellido, 0, wx.EXPAND | wx.ALL, 5)

        

        b = wx.Button(panel, label="Guardar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.Click, b)

        b.SetDefault()
        b.SetSize(b.GetBestSize())


        c = wx.Button(panel, label="Cancelar")  # este  boton pertenece al panel, no a la clase Libro ( self)
        panel.Bind(wx.EVT_BUTTON, self.cerrar_ventana, c)

        c.SetDefault()
        c.SetSize(b.GetBestSize())

        sizer.Add(b, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(c, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)#esta linea es clave para q se vean los input, estube renegando mucho para que se vean los inputs que puse y era q me faltaba esta linea




        
        return frame
    


    def Click(self, event):

        libro = self.txt_libro.GetValue()
        persona = self.txt_persona.GetValue()
        fecha = self.txt_fecha.GetValue()
        

   

        self.guardar_prestamo()


        wx.MessageBox(
        "Prestamo guardado exitosamente!",
        "Éxito",
        wx.OK | wx.ICON_INFORMATION
    )

        self.dlg.Close()




    def guardar_json(self, prestamo):
   


        if not os.path.exists("prestamos.json"):
            with open("prestamos.json", "w", encoding="utf-8") as archivo:
                json.dump([], archivo)

   
        with open("prestamos.json", "r", encoding="utf-8") as archivo:
            prestamos = json.load(archivo)

  
        prestamos.append(prestamo)

        with open("prestamos.json", "w", encoding="utf-8") as archivo:
            json.dump(prestamos, archivo, indent=4, ensure_ascii=False)





    def guardar_prestamo(self):

     prestamos = {
        "libro": self.txt_libro.GetValue(),
        "persona": self.txt_persona.GetValue(),
        "fecha": self.txt_fecha.GetValue()
        
    }

     self.guardar_json(prestamos)



    def cerrar_ventana(self, event):
        self.dlg.Close()




    











        