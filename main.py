import wx






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

        sizer.Add(wx.StaticText(self, label="Libros registrados: 0"),
                  0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="Personas registradas: 0"),
                  0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="Préstamos activos: 0"),
                  0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.AddStretchSpacer()

        self.SetSizer(sizer)




class PanelLibros(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Libros")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)

        sizer.Add(wx.StaticText(self, label="Título"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="ISBN"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.Button(self, label="+ Nuevo Libro"),
                  0, wx.ALL, 10)
        


        

        tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        tabla.InsertColumn(0, "ID", width=80)
        tabla.InsertColumn(1, "Título", width=300)
        tabla.InsertColumn(2, "ISBN", width=200)

        sizer.Add(tabla, 1, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(sizer)




class PanelPersonas(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Personas")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)

        sizer.Add(wx.StaticText(self, label="Nombre"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="DNI"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.Button(self, label="Guardar Persona"),
                  0, wx.ALL, 10)

        tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        tabla.InsertColumn(0, "ID", width=80)
        tabla.InsertColumn(1, "Nombre", width=250)
        tabla.InsertColumn(2, "DNI", width=150)

        sizer.Add(tabla, 1, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(sizer)



class PanelPrestamos(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Nuevo Préstamo")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)

        sizer.Add(wx.StaticText(self, label="Persona"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="Libro"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.Button(self, label="Registrar Préstamo"),
                  0, wx.ALL, 10)

        tabla = wx.ListCtrl(self, style=wx.LC_REPORT)

        tabla.InsertColumn(0, "ID", width=80)
        tabla.InsertColumn(1, "Persona", width=250)
        tabla.InsertColumn(2, "Libro", width=250)
        tabla.InsertColumn(3, "Fecha", width=150)

        sizer.Add(tabla, 1, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(sizer)




class PanelDevoluciones(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Devoluciones")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 15)

        sizer.Add(
            wx.StaticText(
                self,
                label="Módulo en desarrollo",
              
            ),
            0,
            wx.ALL,
            20



        )



        # sizer.Add(
        #     wx.StaticText(
        #         self,
        #         label="Módulo en desarrollo22",
              
        #     ),
        #     0,
        #     wx.ALL,
        #     40



        # )




        

        self.SetSizer(sizer)




class PanelReportes(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Reportes")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 15)

        sizer.Add(wx.Button(self, label="Libros Disponibles"),
                  0, wx.ALL, 5)

        sizer.Add(wx.Button(self, label="Libros Prestados"),
                  0, wx.ALL, 5)

        sizer.Add(wx.Button(self, label="Historial de Préstamos"),
                  0, wx.ALL, 5)

        self.SetSizer(sizer)




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
            ("Devoluciones", PanelDevoluciones),
            ("Reportes", PanelReportes)
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