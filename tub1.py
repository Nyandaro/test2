import wx
import subprocess
from subprocess import Popen, PIPE
from mesod1 import Test2class
from tub2 import Tub2
import wx.grid
# import _thread
import threading


class Tub1(wx.Panel):
    flag = False

    def __init__(self, parent):
        super(Tub1, self).__init__(parent)
        # text = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(250, 150))

        """タブ１の設定"""
        """ wx用のテキスト表示方法 """
        self.text1 = wx.StaticText(self, 1, "text1")
        self.text2 = wx.StaticText(self, 1, "text2")
        self.result_text = wx.StaticText(self, 1, "text3")

        """ テキスト毎へのイベントのバインド """
        self.text1.Bind(wx.EVT_LEFT_DOWN, self.click)
        self.text2.Bind(wx.EVT_LEFT_DOWN, self.click)

        """ビットマップ設定"""
        # image = wx.Bitmap('Candybar.ico')
        # image = wx.Image('Candybar.ico')
        # bitmap = image.ConvertToBitmap()
        # self.btmp = wx.StaticBitmap(self, 1, image, pos=(0, 0), size=image.GetSize())
        # self.btmp = wx.StaticBitmap(self, 1, bitmap, pos=(0, 0), size=image.GetSize())

        """各ボタンの設定"""
        self.button1 = wx.Button(self, 1, 'm3u8録画')
        self.button2 = wx.Button(self, 1, '録画終了')
        self.button3 = wx.Button(self, 1, '押された')

        """各ボタンへのイベントのバインド"""
        self.button1.Bind(wx.EVT_BUTTON, self.buttonclick1)
        # self.button1.Bind(wx.EVT_BUTTON, self.threadmesod)
        self.button2.Bind(wx.EVT_BUTTON, self.buttonclick2)
        self.button3.Bind(wx.EVT_BUTTON, self.buttonclick3)

        """ボタンビットマップ設定"""
        # self.button1.SetBitmapLabel(self, image)

        """テキストコントロールの設定"""
        self.textctl = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(600, 200))

        """grid 表 の表示"""
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(5, 3)

        # Set column labels.
        self.grid.SetColLabelValue(0, "Title")
        self.grid.SetColLabelValue(1, "URL")

        # Set cell values.
        self.grid.SetCellValue(0, 0, "Google")
        self.grid.SetCellValue(0, 1, "http://google.com/")
        self.grid.SetCellValue(0, 2, "http://google.com/")
        self.grid.SetCellValue(1, 0, "Yahoo! JAPAN")
        self.grid.SetCellValue(1, 1, "http://www.yahoo.co.jp/")
        self.grid.SetCellValue(2, 0, "Python")
        self.grid.SetCellValue(2, 1, "http://www.python.org/")
        self.grid.SetCellValue(2, 2, "http://www.python.org/")
        self.grid.SetCellValue(3, 0, "Python Documentation")
        self.grid.SetCellValue(3, 1, "http://docs.python.org/")
        self.grid.SetCellValue(3, 2, "http://docs.python.org/")
        self.grid.SetCellValue(4, 0, "wxPython")
        self.grid.SetCellValue(4, 1, "http://www.wxpython.org/")
        self.grid.SetCellValue(4, 2, "http://www.wxpython.org/")

        # Alignment.
        self.grid.AutoSize()

        """水平並びのBoxSizerの設定"""
        h_layout2 = wx.BoxSizer(wx.HORIZONTAL)
        h_layout2.Add(self.button1, proportion=0, flag=wx.TOP, border=10)
        h_layout2.Add(self.button2, proportion=0, flag=wx.TOP, border=10)
        h_layout2.Add(self.button3, proportion=0, flag=wx.TOP, border=10)

        """垂直並びのBoxSizerの設定"""
        v_layout = wx.BoxSizer(wx.VERTICAL)

        """水平を差し込む"""
        v_layout.Add(h_layout2)
        v_layout.Add(self.text1, proportion=0, flag=wx.TOP, border=5)
        v_layout.Add(self.text2, proportion=0, flag=wx.TOP, border=5)
        v_layout.Add(self.textctl, proportion=0, flag=wx.TOP, border=5)
        v_layout.Add(self.result_text, proportion=0, flag=wx.TOP, border=5)
        v_layout.Add(self.grid, proportion=0, flag=wx.TOP, border=5)

        # v_layout.Add(self.btmp, proportion=0, flag=wx.TOP, border=5)

        self.SetSizer(v_layout)
        # panel.SetSizer(v_layout)

    """textの文字変更をしているだけ"""
    def click(self, event):
        click = event.GetEventObject()
        click_text = click.GetLabel()
        self.result_text.SetLabel(click_text)

    def buttonclick1(self, event):
        """_threadの場合の方法"""
        # _thread.start_new_thread(self.Run, ())

        """threadingの場合の方法"""
        t = threading.Thread(target=self.run)
        t.start()

        """mesod1ファイルの処理を引き取ってるだけ"""
        # # a = Test2class()
        # # self.result_text.SetLabel(a.test2mesod("ewqweq"))

    def run(self):
        self.textctl.SetLabel("")
        """m3u8での録画方法"""
        result = subprocess.Popen(
            r'ffmpeg.exe -i https://movie.freshlive.tv/x/playlist/2102398.m3u8?version=2 -c copy out.ts',
            stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        self.result_text.SetLabel("処理中")

        """ FLVを終了時間付きMP4に変換する方法 （write q は必要ない）"""
        # result = subprocess.Popen('ffmpeg.exe -i zzz.flv -vcodec copy -acodec copy zzz.mp4', stdout=PIPE,
        # stderr=subprocess.STDOUT)

        while True:
            c = result.stdout.readline()
            self.textctl.AppendText(c)

            """stdout内の文字列が無くなったら終了"""
            if not c:
                break

            """フラグにより終了"""
            if Tub1.flag:
                break

        result.stdin.write("q")
        result.stdin.flush()
        result.stdout.flush()
        result.terminate()
        # result.kill()
        self.result_text.SetLabel("終了")

        """必ずフラグを元に戻すこと"""
        Tub1.flag = False
        # _thread.exit_thread()

    def buttonclick2(self, event):
        Tub1.flag = True

        """Tub2からフラグ取ってるだけ"""
        # self.result_text.SetLabel(Tub2.getflag2())

    def buttonclick3(self, event):
        """textctrlから値取ってるだけ"""
        # self.result_text.SetLabel(self.textctl.GetValue())
