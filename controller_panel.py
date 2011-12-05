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

        self.pressedBtns = []
        

    
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
        self.buttons[0].Bind(wx.EVT_LEFT_DOWN, self.btnUpLeftDown)
        self.buttons[1].Bind(wx.EVT_LEFT_DOWN, self.btnUpDown)
        self.buttons[2].Bind(wx.EVT_LEFT_DOWN, self.btnUpRightDown)
        self.buttons[3].Bind(wx.EVT_LEFT_DOWN, self.btnLeftDown)
        self.buttons[4].Bind(wx.EVT_LEFT_DOWN, self.btnCentreDown)
        self.buttons[5].Bind(wx.EVT_LEFT_DOWN, self.btnRightDown)
        self.buttons[6].Bind(wx.EVT_LEFT_DOWN, self.btnDownLeftDown)
        self.buttons[7].Bind(wx.EVT_LEFT_DOWN, self.btnDownDown)
        self.buttons[8].Bind(wx.EVT_LEFT_DOWN, self.btnDownRightDown)

        self.buttons[10].Bind(wx.EVT_BUTTON, self.OnConnect)

        for self.x in self.buttons:
            self.x.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
            self.x.Bind(wx.EVT_KEY_UP, self.OnKeyUp)
            self.x.Bind(wx.EVT_LEFT_UP, self.released)

        self.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.port = None

    def OnCombo(self, event):
        self.port = self.availablePorts.GetValue()

    def OnConnect(self, event):
        pass

    def btnUpLeftDown(self, event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.buttons[0].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnUpDown(self, event):
        if "Up" not in self.pressedBtns:
            self.pressedBtns.append("Up")
        self.buttons[1].SetBackgroundColour('#3a90d1')
        event.Skip()
        
    def btnUpRightDown(self, event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.buttons[2].SetBackgroundColour('#3a90d1')
        event.Skip()
        
    def btnLeftDown(self, event):
        if "Left" not in self.pressedBtns:
            self.pressedBtns.append("Left")
        self.buttons[3].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnCentreDown(self, event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.buttons[4].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnRightDown(self, event):
        if "Right" not in self.pressedBtns:
            self.pressedBtns.append("Right")
        self.buttons[5].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownLeftDown(self, event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.buttons[6].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownDown(self, event):
        if "Down" not in self.pressedBtns:
            self.pressedBtns.append("Down")
        self.buttons[7].SetBackgroundColour('#3a90d1')
        event.Skip()

    def btnDownRightDown(self, event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.buttons[8].SetBackgroundColour('#3a90d1')
        event.Skip()


    # released
    def released(self,event):
        for n in self.buttons:
            n.SetBackgroundColour(None)
        self.pressedBtns = []
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

        self.pressedBtns.sort()
        # print self.pressedBtns
        a = ''.join(self.pressedBtns)
        if a == 'LeftUp':
            self.btnUpLeftDown(event)
        if a == 'RightUp':
            self.btnUpRightDown(event)
        if a == 'DownLeft':
            self.btnDownLeftDown(event)
        if a == 'DownRight':
            self.btnDownRightDown(event)
        if a == 'DownUp':
            self.btnCentreDown(event)
        if a == 'LeftRight':
            self.btnCentreDown(event)
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

    # sizers
    def InitUI(self):
        self.portText = wx.StaticText(self, -1, 'Port:')
        s = scan()
        self.availablePorts = wx.ComboBox(self, -1, choices='salala', 
					style=wx.CB_READONLY)
        self.connectBtn = wx.Button(self, -1, 'Connect', style=wx.EXPAND )

        gs = wx.GridSizer(3, 3, 3, 3)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        gs.AddMany(self.buttons)

        hbox.Add(self.portText, 1)
        hbox.Add(self.availablePorts, 1)
        hbox.Add(self.connectBtn, 1)

        self.buttons.append(self.availablePorts)
        self.buttons.append(self.connectBtn)


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
