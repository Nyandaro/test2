import wx


# def scale_bitmap(bitmap, width, height):
#     """ 画像のリサイズ """
#     image = wx.ImageFromBitmap(bitmap)
#     image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
#     result = wx.BitmapFromImage(image)
#     return result


class Tub2(wx.Panel):
    flag = "not found flag"

    def __init__(self, parent):
        super(Tub2, self).__init__(parent)
        """フラグ"""

        """タブ２の設定"""
        """checkboxの設定"""
        Tub2.checkbox1 = wx.CheckBox(self, 0, 'check1')
        self.checkbox2 = wx.CheckBox(self, 0, 'check2')
        self.checkbox3 = wx.CheckBox(self, 0, 'check3')
        self.result_text2 = wx.StaticText(self, 0, "押された")

        """checkboxにイベントのバインド"""
        Tub2.checkbox1.Bind(wx.EVT_CHECKBOX, self.checkboxclick1)
        self.checkbox2.Bind(wx.EVT_CHECKBOX, self.checkboxclick2)

        """各ボタンの設定"""
        self.button1 = wx.Button(self, 1, 'button1')

        """各ボタンへのイベントのバインド"""
        self.button1.Bind(wx.EVT_BUTTON, self.buttonclick1)

        """ビットマップ設定"""
        image = wx.Bitmap('Candybar.ico')
        # image = wx.Image('Candybar.ico')
        # bitmap = image.ConvertToBitmap()
        # self.btmp = wx.StaticBitmap(self, 1, image, pos=(0, 0), size=image.GetSize())
        # self.btmp = wx.StaticBitmap(self, 1, bitmap, pos=(0, 0), size=image.GetSize())

        # caption = ("No", "都道府県", "男女計", "男", "女")
        #
        # data = [
        #     (1, "北海道", 5570, 2638, 2933),
        #     (2, "青森県", 1407, 663, 744),
        # ]

        """Listコントロール(これも表のようなもの)の表示"""
        self.list = wx.ListCtrl(self, 0, style=wx.LC_REPORT)

        # self.list.InsertColumn(0, caption[0], wx.LIST_FORMAT_RIGHT)
        # self.list.InsertColumn(1, caption[1])
        # self.items = data
        # self.list.SetItemCount(len(self.items))
        # self.list.SetItem(self.list)

        self.list.InsertColumn(0, "氏名", wx.LIST_FORMAT_LEFT, 150)
        self.list.InsertColumn(1, "性別", wx.LIST_FORMAT_LEFT, 100)
        self.list.InsertColumn(2, "年齢", wx.LIST_FORMAT_LEFT, 100)

        # ListCtrlにアイテムを追加
        # for x in range(4):
        #     self.list.InsertItem(x, '山田　%s郎' % x)
        #     self.list.SetItem(x, 1, "男")
        #     self.list.SetItem(x, 2, str((x + 1) * 5))
        # convert_image = scale_bitmap(image, 20, 20)
        imageb = image.ConvertToImage()
        # imageb = wx.ImageFromBitmap(image)#非推奨
        convert_image = imageb.Scale(40, 40, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(convert_image)
        self.listimag = wx.ImageList(40, 40)
        self.listimag.Add(result)
        # self.list.SetImageList(self.listimag, wx.IMAGE_LIST_SMALL)
        # self.list.InsertItem(0, '山田')
        # self.list.SetItem(0, 1, "男")
        # self.list.SetItem(0, 2, "12")
        #
        # self.list.SetImageList(self.listimag, wx.IMAGE_LIST_SMALL)
        # self.list.InsertItem(1, '田中')
        # self.list.SetItem(1, 1, "女")
        # self.list.SetItem(1, 2, "23")

        # self.list.AssignImageList(0, 2, self.listimag)
        # self.list.InsertImageItem(0, 2, self.listimag)
        # self.list.SetItem(0, 2, "111")
        # self.list.InsertItem(2, '山田', '太郎')
        # self.list.InsertItem(3, '山田', '太郎')

        """水平並びのBoxSizerの設定"""
        h_layout = wx.BoxSizer(wx.HORIZONTAL)
        h_layout.Add(Tub2.checkbox1, flag=wx.TOP)
        h_layout.Add(self.checkbox2, flag=wx.TOP)
        h_layout.Add(self.checkbox3, flag=wx.TOP)

        """垂直並びのBoxSizerの設定"""
        v_layout2 = wx.BoxSizer(wx.VERTICAL)
        v_layout2.Add(h_layout)
        v_layout2.Add(self.result_text2, proportion=0, flag=wx.TOP, border=5)
        v_layout2.Add(self.list, proportion=0, flag=wx.TOP, border=5)
        v_layout2.Add(self.button1, proportion=0, flag=wx.TOP, border=10)

        self.SetSizer(v_layout2)

    def checkboxclick1(self, event):
        if Tub2.checkbox1.IsChecked():
            self.result_text2.SetLabel("on")
        else:
            self.result_text2.SetLabel("off")

    def checkboxclick2(self, event):
        if self.checkbox2.IsChecked():
            Tub2.flag = "on"
        else:
            Tub2.flag = "off"

    def getflag2():
        return Tub2.flag

    def buttonclick1(self, event):
        self.list.InsertItem(0, '佐藤')
        self.list.SetItem(0, 1, "釜")
        self.list.SetItem(0, 2, "25")
