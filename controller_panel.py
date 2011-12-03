import wx, glob, serial, sys
from obrazky import *



def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    if sys.platform == 'linux2':
        return list(glob.glob('/dev/ttyUSB*'))
    else:
        available = []
        for i in range(256):
            try:
                s = serial.Serial("COM" + str(i))
                available.append( s.portstr)
                s.close() # explicit close 'cause of delayed GC in java
            except serial.SerialException:
                pass
        return available

    
 
class arrowsPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size=(220, 430), style=wx.SUNKEN_BORDER)

    
        self.imageUPLEFT = wx.Image(upleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageLEFT = wx.Image(left, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNLEFT = wx.Image(downleft, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUP = wx.Image(up, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageLOGO = wx.Image(logo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWN = wx.Image(down, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageUPRIGHT = wx.Image(upright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageRIGHT = wx.Image(right, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.imageDOWNRIGHT = wx.Image(downright, wx.BITMAP_TYPE_ANY).ConvertToBitmap()


        self.buttons = [wx.BitmapButton(self, id = upleftID, bitmap=self.imageUPLEFT),
                wx.BitmapButton(self, id = upID, bitmap = self.imageUP),
                wx.BitmapButton(self, id = uprightID, bitmap=self.imageUPRIGHT),
                wx.BitmapButton(self, id = leftID, bitmap=self.imageLEFT),
                wx.BitmapButton(self, id = logoID, bitmap=self.imageLOGO),
                wx.BitmapButton(self, id = rightID, bitmap=self.imageRIGHT),
                wx.BitmapButton(self, id = downleftID, bitmap=self.imageDOWNLEFT),
                wx.BitmapButton(self, id = downID, bitmap=self.imageDOWN),
                wx.BitmapButton(self, id = downrightID, bitmap=self.imageDOWNRIGHT)]


        self.InitUI()
        
        # binding buttons
        self.buttons[0].Bind(wx.EVT_LEFT_DOWN, self.btnUpleftDown)
        self.buttons[1].Bind(wx.EVT_LEFT_DOWN, self.btnUpDown)
        self.buttons[2].Bind(wx.EVT_LEFT_DOWN, self.btnUprightDown)
        self.buttons[3].Bind(wx.EVT_LEFT_DOWN, self.btnLeftDown)
        self.buttons[4].Bind(wx.EVT_LEFT_DOWN, self.btnCentreDown)
        self.buttons[5].Bind(wx.EVT_LEFT_DOWN, self.btnRightDown)
        self.buttons[6].Bind(wx.EVT_LEFT_DOWN, self.btnDownleftDown)
        self.buttons[7].Bind(wx.EVT_LEFT_DOWN, self.btnDownDown)
        self.buttons[8].Bind(wx.EVT_LEFT_DOWN, self.btnDownrightDown)

        

      
        for self.x in self.buttons:
            self.x.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
            self.x.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
            self.x.Bind(wx.EVT_LEFT_UP, self.released)

        

        

    def btnUpleftDown(self, event):
        self.buttons[0].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnUpDown(self, event):
        self.buttons[1].SetBackgroundColour('#3a90d1')
        event.Skip()
        
    def btnUprightDown(self, event):
        self.buttons[2].SetBackgroundColour('#3a90d1')
        event.Skip()
        
    def btnLeftDown(self, event):
        self.buttons[3].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnCentreDown(self, event):
        self.buttons[4].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnRightDown(self, event):
        self.buttons[5].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownleftDown(self, event):
        self.buttons[6].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownDown(self, event):
        self.buttons[7].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownrightDown(self, event):
        self.buttons[8].SetBackgroundColour('#3a90d1')
        event.Skip()


    # released
    def released(self,event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        event.Skip()




    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        if keycode == 87 or keycode == 119: 
            self.btnUpDown(event)
        if keycode == 83 or keycode == 115:
            self.btnDownDown(event)
        if keycode == 68 or keycode == 100:
            self.btnRightDown(event)
        if keycode == 65 or keycode == 97:
            self.btnLeftDown(event)
        event.Skip()

    def OnKeyUp(self, event):
        keycode = event.GetKeyCode()
        if keycode == 87 or keycode == 119:
            self.released(event)
        if keycode == 83 or keycode == 115:
            self.released(event)
        if keycode == 68 or keycode == 100:
            self.released(event)
        if keycode == 65 or keycode == 97:
            self.released(event)
        event.Skip()


    def update_buttons(self, event):
        # 210, 214
        # print self.GetSize()
        pass
        
        
        
    def InitUI(self):
        portText = wx.StaticText(self, -1, 'Port:')
        s = scan()
        availablePorts = wx.ComboBox(self, -1, choices=s, 
					style=wx.CB_READONLY)
        connectBtn = wx.Button(self, -1, 'Connect', style=wx.EXPAND )

        gs = wx.GridSizer(3, 3, 3, 3)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        gs.AddMany(self.buttons)

        hbox.Add(portText, 1)
        hbox.Add(availablePorts, 1)
        hbox.Add(connectBtn, 1)


        vbox.Add(gs, 0, flag=wx.EXPAND)
        vbox.Add(hbox, 0, flag=wx.EXPAND)
        
        self.SetSizer(vbox)
        

        
       
class Arrows(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(220, 430),
                          style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU |
                                  wx.RESIZE_BORDER | wx.MINIMIZE_BOX)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Disconnected')

        Arrows = arrowsPanel(self, -1)
        
 
        
        self.SetMinSize((230, 300))
        self.SetMaxSize((230, 300))
        self.Centre()
        self.Show()
        
 
if __name__ == "__main__":
    app = wx.App()
    Arrows(None, -1, 'SimpleBT')
    app.MainLoop()
