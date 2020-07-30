import wx
class PDFPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        label_file_control = wx.StaticText(self, label='Selecione um modelo (Opcional)')
        self.main_sizer.Add(label_file_control, 0, wx.ALL | wx.EXPAND, 5)
        self.file_control = wx.FilePickerCtrl(self)
        self.main_sizer.Add(self.file_control, 0 , wx.ALL | wx.EXPAND , 5)

        label_dir_control = wx.StaticText(self, label='Selecione um diretorio')
        self.main_sizer.Add(label_dir_control, 0, wx.ALL | wx.EXPAND, 5)
        self.dir_control = wx.DirPickerCtrl(self)
        self.main_sizer.Add(self.dir_control, 0 , wx.ALL | wx.EXPAND , 5)
        self.btn_process = wx.Button(self, label="&Processar")
        self.main_sizer.Add(self.btn_process, 0 , wx.ALL | wx.CENTER , 5)
        self.SetSizer(self.main_sizer)
    def initUI():
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label='Diretorio',
                              size=(50, -1))
        row_sizer.Add(label, 0, wx.ALL, 5)
        self.file_control = wx.FilePickerCtrl(self)
        row_sizer.Add(self.file_control, 1, wx.ALL | wx.EXPAND, 5)
        self.main_sizer.Add(row_sizer, 0, wx.EXPAND)
class PDFFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                        title="PDF-DOCX", size=(500,550))
        self.panel = PDFPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = PDFFrame()
    app.MainLoop()