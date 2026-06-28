sizer = wx.BoxSizer(wx.VERTICAL)

        titulo = wx.StaticText(self, label="Gestión de Libros")
        titulo.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        sizer.Add(titulo, 0, wx.ALL, 10)

        sizer.Add(wx.StaticText(self, label="Título"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)

        sizer.Add(wx.StaticText(self, label="ISBN"))
        sizer.Add(wx.TextCtrl(self), 0, wx.EXPAND | wx.ALL, 5)
