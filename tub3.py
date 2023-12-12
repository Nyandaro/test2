import wx


class Tub3(wx.Panel):
    def __init__(self, parent):
        super(Tub3, self).__init__(parent)

        """タブ３の設定"""
        """ラジオボタンの設定"""
        self.radiobutton1 = wx.RadioButton(self, 1, "ラジオボタン1", style=wx.RB_GROUP)
        self.radiobutton2 = wx.RadioButton(self, 2, "ラジオボタン2")
        self.radiobutton3 = wx.RadioButton(self, 3, "ラジオボタン3")
        self.radiobutton4 = wx.RadioButton(self, 4, "ラジオボタン4", style=wx.RB_GROUP)
        self.radiobutton5 = wx.RadioButton(self, 5, "ラジオボタン5")
        self.radiobutton6 = wx.RadioButton(self, 6, "ラジオボタン6")
        self.result_text3 = wx.StaticText(self, 0, "押された")

        """ラジオボタンのイベントのバインド"""
        self.radiobutton1.Bind(wx.EVT_RADIOBUTTON, self.radio1click)
        self.radiobutton2.Bind(wx.EVT_RADIOBUTTON, self.radio2click)
        self.radiobutton3.Bind(wx.EVT_RADIOBUTTON, self.radio3click)

        """水平並びのBoxSizerの設定"""
        h_layout2 = wx.BoxSizer(wx.HORIZONTAL)
        h_layout2.Add(self.radiobutton1, proportion=0, flag=wx.TOP, border=10)
        h_layout2.Add(self.radiobutton2, proportion=0, flag=wx.TOP, border=10)
        h_layout2.Add(self.radiobutton3, proportion=0, flag=wx.TOP, border=10)

        """水平並びのBoxSizerの設定"""
        h_layout3 = wx.BoxSizer(wx.HORIZONTAL)
        h_layout3.Add(self.radiobutton4, proportion=0, flag=wx.TOP, border=10)
        h_layout3.Add(self.radiobutton5, proportion=0, flag=wx.TOP, border=10)
        h_layout3.Add(self.radiobutton6, proportion=0, flag=wx.TOP, border=10)

        """垂直並びのBoxSizerの設定"""
        v_layout3 = wx.BoxSizer(wx.VERTICAL)
        v_layout3.Add(h_layout2)
        v_layout3.Add(h_layout3)
        v_layout3.Add(self.result_text3, proportion=0, flag=wx.TOP, border=5)

        """panel3にイベントのバインド"""
        self.Bind(wx.EVT_RADIOBUTTON, self.radio4click, self.radiobutton4)
        self.Bind(wx.EVT_RADIOBUTTON, self.radio4click, self.radiobutton5)
        self.Bind(wx.EVT_RADIOBUTTON, self.radio4click, self.radiobutton6)

        self.SetSizer(v_layout3)

        """上の段の処理"""
    def radio1click(self, event):
        self.result_text3.SetLabel("ラジオボタン1")

    def radio2click(self, event):
        self.result_text3.SetLabel("ラジオボタン2")

    def radio3click(self, event):
        self.result_text3.SetLabel("ラジオボタン3")

        """"下の段の処理 一括"""
    def radio4click(self, event):
        if event.GetId() == 4:
            self.result_text3.SetLabel("ラジオ4")
        elif event.GetId() == 5:
            self.result_text3.SetLabel("ラジオ5")
        elif event.GetId() == 6:
            self.result_text3.SetLabel("ラジオ6")
