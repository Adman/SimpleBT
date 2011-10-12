import wx
from obrazky import *
 
class arrowsPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size=(210, 430), style=wx.SUNKEN_BORDER)


        self.imageUPLEFT = wx.Image(upleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageLEFT = wx.Image(left, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNLEFT = wx.Image(downleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUP = wx.Image(up, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageCENTRE = wx.Image(centre, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWN = wx.Image(down, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUPRIGHT = wx.Image(upright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageRIGHT = wx.Image(right, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNRIGHT = wx.Image(downright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        self.buttons = [wx.BitmapButton(self, id = upleftID, bitmap=self.imageUPLEFT),
                wx.BitmapButton(self, id = upID, bitmap = self.imageUP),
                wx.BitmapButton(self, id = uprightID, bitmap=self.imageUPRIGHT),
                wx.BitmapButton(self, id = leftID, bitmap=self.imageLEFT),
                wx.BitmapButton(self, id = centreID, bitmap=self.imageCENTRE),
                wx.BitmapButton(self, id = rightID, bitmap=self.imageRIGHT),
                wx.BitmapButton(self, id = downleftID, bitmap=self.imageDOWNLEFT),
                wx.BitmapButton(self, id = downID, bitmap=self.imageDOWN),
                wx.BitmapButton(self, id = downrightID, bitmap=self.imageDOWNRIGHT)]
 


        acceltbl = wx.AcceleratorTable( [
                (wx.ACCEL_NORMAL, ord('w'), upID),
                (wx.ACCEL_NORMAL, ord('s'), downID),
                (wx.ACCEL_NORMAL, ord('a'), leftID),
                (wx.ACCEL_NORMAL, ord('d'), rightID)
            ])
        self.SetAcceleratorTable(acceltbl)



        self.InitUI()
        
        self.buttons[0].Bind(wx.EVT_BUTTON, self.btnupleftClick)
        self.buttons[1].Bind(wx.EVT_BUTTON, self.btnupClick)
        self.buttons[2].Bind(wx.EVT_BUTTON, self.btnuprightClick)
        self.buttons[3].Bind(wx.EVT_BUTTON, self.btnleftClick)
        self.buttons[4].Bind(wx.EVT_BUTTON, self.btncentreClick)
        self.buttons[5].Bind(wx.EVT_BUTTON, self.btnrightClick)
        self.buttons[6].Bind(wx.EVT_BUTTON, self.btndownleftClick)
        self.buttons[7].Bind(wx.EVT_BUTTON, self.btndownClick)
        self.buttons[8].Bind(wx.EVT_BUTTON, self.btndownrightClick)

    def btnupleftClick(self, event):
        print 'button upleft pressed'

    def btnupClick(self, event):
        print 'button up pressed'

    def btnuprightClick(self, event):
        print 'button upright pressed'

    def btnleftClick(self, event):
        print 'button left pressed'

    def btncentreClick(self, event):
        print 'button centre pressed'

    def btnrightClick(self, event):
        print 'button right pressed'

    def btndownleftClick(self, event):
        print 'button downleft pressed'

    def btndownClick(self, event):
        print 'button down pressed'

    def btndownrightClick(self, event):
        print 'button downright pressed'
       

        
        
        
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.gs = wx.GridSizer(3, 3, 5, 5)
 
        self.gs.AddMany(self.buttons)
        
        vbox.Add(self.gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
       
 



class Arrows(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(220, 430),
                          style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU |
                                  wx.RESIZE_BORDER | wx.MAXIMIZE_BOX |
                                          wx.MINIMIZE_BOX)
        Arrows = arrowsPanel(self, -1)
 
        
    
        

        self.Centre()
        self.Show()
        
 
       
 
       
   
 
app = wx.App()
Arrows(None, -1, 'Arrows')
app.MainLoop()
