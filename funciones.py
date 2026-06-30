import wx
import json
import os
import random
import string


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
        panel.Bind(wx.EVT_BUTTON, self.Click, b)

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




        