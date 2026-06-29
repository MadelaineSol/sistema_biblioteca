import wx


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

        sizer.Add(wx.StaticText(panel, label="ISBN"))
        self.txt_isbn = wx.TextCtrl(panel)
        sizer.Add(self.txt_isbn, 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(panel, label="Autor"))
        self.txt_autor = wx.TextCtrl(panel)
        sizer.Add(self.txt_autor, 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(sizer)#esta linea es clave para q se vean los input, estube renegando mucho para que se vean los inputs que puse y era q me faltaba esta linea




        # sizer.Add(wx.StaticText(panel, label="Título"))
        # sizer.Add(wx.TextCtrl(panel), 0, wx.EXPAND | wx.ALL, 5)

        # sizer.Add(wx.StaticText(panel, label="ISBN"))
        # sizer.Add(wx.TextCtrl(panel), 0, wx.EXPAND | wx.ALL, 5)
        return frame




        