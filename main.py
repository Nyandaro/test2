import wx
from MenuBar import CalcMenu
from tub1 import Tub1
from tub2 import Tub2
from tub3 import Tub3


class Main(wx.Frame):
    def __init__(self, parent, id, title):
        """ レイアウトの作成 """

        wx.Frame.__init__(self, parent, id, title, size=(600, 600))
        notebook = wx.Notebook(self, 0)

        """タブへの追加"""
        notebook.InsertPage(0, Tub1(notebook), "タブ1")
        notebook.InsertPage(1, Tub2(notebook), "タブ2")
        notebook.InsertPage(2, Tub3(notebook), "タブ3")

        """ステータスバー追加"""
        # self.CreateStatusBar()
        # self.SetStatusText("ステータスバー")

        """メニューバー追加"""
        self.SetMenuBar(CalcMenu())

        """アイコン設定"""
        icon = wx.Icon("Candybar.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        self.Centre()
        self.Show(True)


def main():
    app = wx.App()
    Main(None, 0, "タイトル")
    app.MainLoop()


if __name__ == "__main__":
    main()
