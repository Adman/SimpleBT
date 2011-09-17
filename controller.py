import wx


upleft = "icons/upleft.png"
left = "icons/left.png"
downleft = "icons/downleft.png"
up = "icons/up.png"
centre = "icons/centre.png"
down = "icons/down.png"
upright = "icons/upright.png"
right = "icons/right.png"
downright = "icons/downright.png"

class Arrows(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(220, 430), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self, -1, pos=(0, 0), size=(204, 204))

        self.Bind(wx.EVT_CHAR, self.appMove)
        self.panel.Bind(wx.EVT_CHAR, self.appMove)
        self.SetFocus()

        
        imageUPLEFT = wx.Image(upleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btnupleft = wx.BitmapButton(self.panel, id = 1, bitmap=imageUPLEFT,
            pos=(5, 5), size = (imageUPLEFT.GetWidth()+5, imageUPLEFT.GetHeight()+5))
        self.btnupleft.Bind(wx.EVT_BUTTON, self.btnupleftClick)

        imageLEFT = wx.Image(left, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btnleft = wx.BitmapButton(self.panel, id = 2, bitmap=imageLEFT,
            pos=(5, 69), size = (imageLEFT.GetWidth()+5, imageLEFT.GetHeight()+5))
        self.btnleft.Bind(wx.EVT_BUTTON, self.btnleftClick)
        
        imageDOWNLEFT = wx.Image(downleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btndownleft = wx.BitmapButton(self.panel, id = 3, bitmap=imageDOWNLEFT,
            pos=(5, 133), size = (imageDOWNLEFT.GetWidth()+5, imageDOWNLEFT.GetHeight()+5))
        self.btndownleft.Bind(wx.EVT_BUTTON, self.btndownleftClick)
        
        imageUP = wx.Image(up, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btnup = wx.BitmapButton(self.panel, id = 4, bitmap=imageUP,
            pos=(69, 5), size = (imageUP.GetWidth()+5, imageUP.GetHeight()+5))
        self.btnup.Bind(wx.EVT_BUTTON, self.btnupClick)
        
        imageCENTRE = wx.Image(centre, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btncentre = wx.BitmapButton(self.panel, id = 5, bitmap=imageCENTRE,
            pos=(69, 69), size = (imageCENTRE.GetWidth()+5, imageCENTRE.GetHeight()+5))
        self.btncentre.Bind(wx.EVT_BUTTON, self.btncentreClick)
        
        imageDOWN = wx.Image(down, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btndown = wx.BitmapButton(self.panel, id = 6, bitmap=imageDOWN,
            pos=(69, 133), size = (imageDOWN.GetWidth()+5, imageDOWN.GetHeight()+5))
        self.btndown.Bind(wx.EVT_BUTTON, self.btndownClick)
        
        imageUPRIGHT = wx.Image(upright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btnupright = wx.BitmapButton(self.panel, id = 7, bitmap=imageUPRIGHT,
            pos=(133, 5), size = (imageUPRIGHT.GetWidth()+5, imageUPRIGHT.GetHeight()+5))
        self.btnupright.Bind(wx.EVT_BUTTON, self.btnuprightClick)
        
        imageRIGHT = wx.Image(right, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btnright = wx.BitmapButton(self.panel, id = 8, bitmap=imageRIGHT,
            pos=(133, 69), size = (imageRIGHT.GetWidth()+5, imageRIGHT.GetHeight()+5))
        self.btnright.Bind(wx.EVT_BUTTON, self.btnrightClick)
        
        imageDOWNRIGHT = wx.Image(downright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.btndownright = wx.BitmapButton(self.panel, id = 9, bitmap=imageDOWNRIGHT,
            pos=(133, 133), size = (imageDOWNRIGHT.GetWidth()+5, imageDOWNRIGHT.GetHeight()+5))
        self.btndownright.Bind(wx.EVT_BUTTON, self.btndownrightClick)


        self.Centre()
        self.Show(True)

    def btnupleftClick(self,event):
        self.SetTitle("UPLEFT")

    def btnleftClick(self,event):
        self.SetTitle("LEFT")

    def btndownleftClick(self,event):
        self.SetTitle("DOWNLEFT")

    def btnupClick(self,event):
        self.SetTitle("UP")

    def btncentreClick(self,event):
        self.SetTitle("CENTRE")

    def btndownClick(self,event):
        self.SetTitle("DOWN")

    def btnuprightClick(self,event):
        self.SetTitle("UPRIGHT")

    def btnrightClick(self,event):
        self.SetTitle("RIGHT")

    def btndownrightClick(self,event):
        self.SetTitle("DOWNRIGHT")

    def OnQuit(self, event):
        self.Close()

    def appMove(self, event):
        self.keycode = event.GetKeyCode()
        if self.keycode == 119 or self.keycode == 87:
            self.btnupClick(None)
        elif self.keycode == 115 or self.keycode == 83:
            self.btndownClick(None)
        elif self.keycode == 97 or self.keycode == 65:
            self.btnleftClick(None)
        elif self.keycode == 100 or self.keycode == 68:
            self.btnrightClick(None)

 
if __name__ == "__main__":
    app = wx.App()
    Arrows(None, -1, 'Arrows')
    app.MainLoop()
