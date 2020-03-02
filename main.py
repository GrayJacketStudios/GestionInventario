import wx as wx
import threading
from config.DB import DB as DB

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        self.conn = DB()
        self.conn.connect()
        self.Show()


if __name__ == "__main__":
    
    app = wx.App()
    fr = MainFrame(None, -1, "Venta cafeteria", size=(900,600))
    app.MainLoop()  
