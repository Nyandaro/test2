import wx


class CalcMenu(wx.MenuBar):
    """
    CalcFrameにセットするメニューバークラス
    """

    def __init__(self):
        super().__init__()

        menu_file = wx.Menu()
        menu_file.Append(wx.ID_ANY, '保存')
        menu_file.Append(wx.ID_ANY, '終了')
        menu_edit = wx.Menu()
        menu_edit.Append(wx.ID_ANY, 'コピー')
        menu_edit.Append(wx.ID_ANY, 'ペースト')

        self.Append(menu_file, 'ファイル')
        self.Append(menu_edit, '編集')
