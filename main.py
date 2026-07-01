import wx

import funciones

import os

import json

libro = funciones.Libro()

personas=funciones.Personas()

prestamos=funciones.Prestamos()






class PanelInicio(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(
            self,
            label="SISTEMA DE GESTIÓN PARA BIBLIOTECAS"
        )

        titulo.SetFont(
            wx.Font(
                18,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_BOLD
            )
        )

        sizer.AddStretchSpacer()
        sizer.Add(titulo, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # sizer.Add(wx.StaticText(self, label="Libros registrados: 0"),
        #           0, wx.ALIGN_CENTER | wx.ALL, 5)

        # sizer.Add(wx.StaticText(self, label="Personas registradas: 0"),
        #           0, wx.ALIGN_CENTER | wx.ALL, 5)

        # sizer.Add(wx.StaticText(self, label="Préstamos activos: 0"),
        #           0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)

        




class PanelLibros(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Libros")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))


        sizer.Add(titulo, 0, wx.ALL, 10)

        

        btn_nuevo_libro = wx.Button(self, label="+ Nuevo Libro")
        sizer.Add(btn_nuevo_libro, 0, wx.ALL, 10)

        # sizer.Add(wx.Button(self, label="+ Nuevo Libro"),
        #           0, wx.ALL, 10)
        btn_nuevo_libro.Bind(wx.EVT_BUTTON,libro.cargar_nuevo_libro)
    
        



        

        self.tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.tabla.InsertColumn(0, "Código", width=100)
        self.tabla.InsertColumn(1, "Título", width=250)
        self.tabla.InsertColumn(2, "Autor", width=200)
        self.tabla.InsertColumn(3, "Género", width=150)

        sizer.Add(self.tabla, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)

        self.cargar_tabla()

    def cargar_tabla(self):

            self.tabla.DeleteAllItems()

            if not os.path.exists("libros.json"):
                return

            with open("libros.json", "r", encoding="utf-8") as archivo:
                libros = json.load(archivo)

            for libro in libros:

                fila = self.tabla.InsertItem(
                self.tabla.GetItemCount(),
                libro["codigo"] 
              
            )

                self.tabla.SetItem(fila, 1, libro["titulo"])
                self.tabla.SetItem(fila, 2, libro["autor"])
                self.tabla.SetItem(fila, 3, libro["genero"])
           




class PanelPersonas(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Personas")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)



       

        btn_nueva_persona = wx.Button(self, label="+ Nueva persona")
        sizer.Add(btn_nueva_persona, 0, wx.ALL, 10)

     
        btn_nueva_persona.Bind(wx.EVT_BUTTON,personas.cargar_nueva_persona)

        self.tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.tabla.InsertColumn(0, "Dni", width=80)
        self.tabla.InsertColumn(1, "Nombre", width=250)
        self.tabla.InsertColumn(2, "Apellido", width=150)

        sizer.Add(self.tabla, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)

        self.cargar_tabla()

    def cargar_tabla(self):

        self.tabla.DeleteAllItems()

        if not os.path.exists("personas.json"):
            return

        with open("personas.json", "r", encoding="utf-8") as archivo:
            personas = json.load(archivo)

        for persona in personas:

            fila = self.tabla.InsertItem(
            self.tabla.GetItemCount(),
            persona["dni"]
        )

            self.tabla.SetItem(fila, 1, persona["nombre"])
            self.tabla.SetItem(fila, 2, persona["apellido"])
               
           



class PanelPrestamos(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Prestamos activos")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)


        btn_nuevo_prestamo = wx.Button(self, label="+ Nuevo prestamo")
        sizer.Add(btn_nuevo_prestamo, 0, wx.ALL, 10)

     
        btn_nuevo_prestamo.Bind(wx.EVT_BUTTON,prestamos.cargar_nuevo_prestamo)





       

      

        self.tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        self.tabla.InsertColumn(0, "Libro", width=250)
        self.tabla.InsertColumn(1, "Persona", width=250)
  
        self.tabla.InsertColumn(2, "Fecha", width=150)

        sizer.Add(self.tabla, 1, wx.EXPAND | wx.ALL, 10)
        self.btn_devolver = wx.Button(self, label="Devolver libro")

        self.btn_devolver.Bind(
        wx.EVT_BUTTON,
        self.devolver_libro
        )

        sizer.Add(self.btn_devolver, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)


        self.cargar_tabla()

    def cargar_tabla(self):

        self.tabla.DeleteAllItems()

        if not os.path.exists("prestamos.json"):
            return

        with open("prestamos.json", "r", encoding="utf-8") as archivo:
            prestamos = json.load(archivo)

        for prestamo in prestamos:
            if prestamo["estado"] == "Activo":
                fila = self.tabla.InsertItem(
                    self.tabla.GetItemCount(),
                    prestamo["libro"]
                )
                self.tabla.SetItem(fila, 1, prestamo["persona"])
                self.tabla.SetItem(fila, 2, prestamo["fecha"])
    def devolver_libro(self, event):

        fila = self.tabla.GetFirstSelected()

        if fila == -1:
            wx.MessageBox(
            "Seleccione un préstamo.",
            "Aviso",
            wx.OK | wx.ICON_WARNING
        )
            return

        libro = self.tabla.GetItemText(fila, 0)
        persona = self.tabla.GetItemText(fila, 1)
     

        respuesta = wx.MessageBox(
        f"¿Desea devolver '{libro}'?",
        "Confirmar devolución",
        wx.YES_NO | wx.ICON_QUESTION
        )

        if respuesta != wx.YES:
            return

        prestamos.cambiar_estado_prestamo(libro, persona)
        prestamos.cambiar_estado_libro_devuelto(libro)

        wx.MessageBox(
        "Libro devuelto correctamente.",
        "Éxito",
        wx.OK | wx.ICON_INFORMATION
        )

        self.cargar_tabla()
               












class VentanaPrincipal(wx.Frame):

    def __init__(self):
        super().__init__(
            None,
            title="Sistema de Gestión para Bibliotecas",
            size=(1000, 650)
        )

        panel = wx.Panel(self)

        sizer_principal = wx.BoxSizer(wx.HORIZONTAL)

        # MENÚ
        menu = wx.Panel(panel)
        menu.SetBackgroundColour("#d9d9d9")

        menu_sizer = wx.BoxSizer(wx.VERTICAL)

        titulo_menu = wx.StaticText(menu, label="MENÚ")
        titulo_menu.SetFont(
            wx.Font(
                12,
                wx.DEFAULT,
                wx.NORMAL,
                wx.BOLD
            )
        )

        menu_sizer.Add(titulo_menu, 0, wx.ALL | wx.CENTER, 15)

        botones = [
            ("Inicio", PanelInicio),
            ("Libros", PanelLibros),
            ("Personas", PanelPersonas),
            ("Préstamos", PanelPrestamos),
            
      
        ]

        for texto, panel_clase in botones:
            boton = wx.Button(menu, label=texto, size=(160, 40))
            boton.Bind(
                wx.EVT_BUTTON,
                lambda evt, p=panel_clase: self.mostrar_panel(p)
            )
            menu_sizer.Add(boton, 0, wx.ALL, 5)

        menu_sizer.AddStretchSpacer()

        salir = wx.Button(menu, label="Salir", size=(160, 40))
        salir.Bind(wx.EVT_BUTTON, lambda e: self.Close())

        menu_sizer.Add(salir, 0, wx.ALL, 5)

        menu.SetSizer(menu_sizer)

        self.contenido = wx.Panel(panel)

        self.contenido_sizer = wx.BoxSizer(wx.VERTICAL)
        self.contenido.SetSizer(self.contenido_sizer)

        sizer_principal.Add(menu, 0, wx.EXPAND)
        sizer_principal.Add(self.contenido, 1, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(sizer_principal)

        self.mostrar_panel(PanelInicio)

        self.Centre()
        self.Show()

    def mostrar_panel(self, panel_clase):

        self.contenido_sizer.Clear(delete_windows=True)

        nuevo_panel = panel_clase(self.contenido)

        self.contenido_sizer.Add(
            nuevo_panel,
            1,
            wx.EXPAND
        )

        self.contenido.Layout()


# ==========================
# EJECUCIÓN
# ==========================

if __name__ == "__main__":
    app = wx.App(False)
    VentanaPrincipal()
    app.MainLoop()