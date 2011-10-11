import wx
from obrazky import *
 
class arrowsPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size=(210, 430), style=wx.SUNKEN_BORDER)
 
 
        self.imageUPLEFT = wx.Image(upleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUPLEFT2 = wx.Image(upleftblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageLEFT = wx.Image(left, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageLEFT2 = wx.Image(leftblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNLEFT = wx.Image(downleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNLEFT2 = wx.Image(downleftblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUP = wx.Image(up, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUP2 = wx.Image(upblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageCENTRE = wx.Image(centre, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageCENTRE2 = wx.Image(centreblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWN = wx.Image(down, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWN2 = wx.Image(downblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUPRIGHT = wx.Image(upright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUPRIGHT2 = wx.Image(uprightblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageRIGHT = wx.Image(right, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageRIGHT2 = wx.Image(rightblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNRIGHT = wx.Image(downright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNRIGHT2 = wx.Image(downrightblue, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
       
 
        self.InitUI()
        # self.Centre()
        # self.Show()
       
 
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        gs = wx.GridSizer(3, 3, 5, 5)
 
        gs.AddMany( [
            wx.BitmapButton(self, id = upleftID, bitmap=self.imageUPLEFT),
            wx.BitmapButton(self, id = upID, bitmap = self.imageUP),
            wx.BitmapButton(self, id = uprightID, bitmap=self.imageUPRIGHT),
            wx.BitmapButton(self, id = leftID, bitmap=self.imageLEFT),
            wx.BitmapButton(self, id = centreID, bitmap=self.imageCENTRE),
            wx.BitmapButton(self, id = rightID, bitmap=self.imageRIGHT),
            wx.BitmapButton(self, id = downleftID, bitmap=self.imageDOWNLEFT),
            wx.BitmapButton(self, id = downID, bitmap=self.imageDOWN),
            wx.BitmapButton(self, id = downrightID, bitmap=self.imageDOWNRIGHT)
                    ])
 
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
       
 
class Arrows(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(220, 430),
                          style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU |
                                  wx.RESIZE_BORDER | wx.MAXIMIZE_BOX |
                                          wx.MINIMIZE_BOX)
        Arrows = arrowsPanel(self, -1)
 
        acceltbl = wx.AcceleratorTable( [
                (wx.ACCEL_NORMAL, ord('w'), upID),
                (wx.ACCEL_NORMAL, ord('s'), downID),
                (wx.ACCEL_NORMAL, ord('a'), leftID),
                (wx.ACCEL_NORMAL, ord('d'), rightID)
            ])
        self.SetAcceleratorTable(acceltbl)

        self.Centre()
        self.Show()
 
       
 
       
   
 
app = wx.App()
Arrows(None, -1, 'Arrows')
app.MainLoop()
