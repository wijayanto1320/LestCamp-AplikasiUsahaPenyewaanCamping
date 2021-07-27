import wx
import camp
import sqlite3


class DataManager:
    def __init__(self):
        self.conn = sqlite3.connect('camp.db')
        self.cursor = self.conn.cursor()

    def Jalankan(self, query, returnData=False):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        if returnData:
            return result


class Main(DataManager, camp.MyFrame1):
    def __init__(self, parent):
        camp.MyFrame1.__init__(self, parent)
        self.DM = DataManager()

    def button_login(self, event):
        username = self.m_textCtrl1.GetValue()
        password = self.m_textCtrl2.GetValue()
        self.query = f"SELECT * FROM admin where username = '{username}' and password = '{password}'"
        hasil = self.DM.Jalankan(self.query, returnData=True)

        if len(hasil) <= 0:
            wx.MessageBox(
                'Username atau Password yang anda masukkan salah', 'Terjadi Kesalahan')
        for row in hasil:
            if row[1] == username and row[5] == password:
                event = Main3(None, adminn=row[1])
                event.Show()
                self.Destroy()
                self.DM.conn.close()



class Main2(Main, camp.MyFrame2):
    def __init__(self, parent,adminn):
        camp.MyFrame2.__init__(self, parent)
        self.DM = DataManager()
        self.adminn = adminn

    def button_daftar(self, event):
        username = self.m_textCtrl3.GetValue()
        umur = self.m_textCtrl4.GetValue()
        alamat = self.m_textCtrl5.GetValue()
        email = self.m_textCtrl6.GetValue()
        password = self.m_textCtrl7.GetValue()

        if username != "" and umur != "" and alamat != "" and email != "" and password != "":
            self.query = 'INSERT INTO admin (username, umur, alamat, email, password) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
            self.query = self.query % (username, umur, alamat, email, password)
            self.DM.Jalankan(self.query)
            event = Main(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

    def button_batal(self, event):
        event = Main3(None, adminn=self.adminn)
        event.Show()
        self.Destroy()


class Main3(Main2, camp.MyFrame3):
    def __init__(self, parent, adminn):
        camp.MyFrame3.__init__(self, parent)
        self.m_grid4.SetColLabelValue(0, "kodepinjaman Pinjam")
        self.m_grid4.SetColLabelValue(1, "Nama")
        self.m_grid4.SetColLabelValue(2, "KTP")
        self.m_grid4.SetColLabelValue(3, "Tanggal Peminjaman")
        self.m_grid4.SetColLabelValue(4, "Tanggal Pengembalian")
        self.m_grid4.SetColLabelValue(5, "Tenda Max4")
        self.m_grid4.SetColLabelValue(6, "Tenda Max2")
        self.m_grid4.SetColLabelValue(7, "Tas")
        self.m_grid4.SetColLabelValue(8, "Sepatu")
        self.m_grid4.SetColLabelValue(9, "Kompor")
        self.m_grid4.SetColLabelValue(10, "Edit")
        self.DM = DataManager()
        self.adminn = adminn
        self.tampil()
        self.m_staticText39.SetLabel(adminn)

    def tampil(self):
        self.query = 'SELECT * FROM datapeminjam'
        hasil = self.DM.Jalankan(self.query, returnData=True)
        for a in hasil:
            self.m_grid4.AppendRows(1)
        for b in range(10):
            a = 0
            for row in hasil:
                self.m_grid4.SetCellValue(a, b, str(row[b]))
                a = a + 1

    def m_grid4OnGridCmdSelectCell(self, event):
        row = event.GetRow()
        self.showTex(row)

    def showTex(self, row):
        kodepinjaman = self.m_grid4.GetCellValue(row, 0)
        nama = self.m_grid4.GetCellValue(row, 1)
        ktp = self.m_grid4.GetCellValue(row, 2)
        tanggalpeminjaman = self.m_grid4.GetCellValue(row, 3)
        tanggalpengembalian = self.m_grid4.GetCellValue(row, 4)
        tenda4 = self.m_grid4.GetCellValue(row, 5)
        tenda2 = self.m_grid4.GetCellValue(row, 6)
        tas = self.m_grid4.GetCellValue(row, 7)
        sepatu = self.m_grid4.GetCellValue(row, 8)
        kompor = self.m_grid4.GetCellValue(row, 9)

        self.m_textCtrl18.SetValue(kodepinjaman)
        self.m_textCtrl19.SetValue(nama)
        self.m_textCtrl20.SetValue(ktp)
        self.m_textCtrl21.SetValue(tanggalpeminjaman)
        self.m_textCtrl22.SetValue(tanggalpengembalian)
        self.m_textCtrl23.SetValue(tenda4)
        self.m_textCtrl24.SetValue(tenda2)
        self.m_textCtrl25.SetValue(tas)
        self.m_textCtrl26.SetValue(sepatu)
        self.m_textCtrl27.SetValue(kompor)

    def btn_simpanEdit(self, event):
        kodepinjaman = self.m_textCtrl18.GetValue()
        nama = self.m_textCtrl19.GetValue()
        ktp = self.m_textCtrl20.GetValue()
        tanggalpeminjaman = self.m_textCtrl21.GetValue()
        tanggalpengembalian = self.m_textCtrl22.GetValue()
        tenda4 = self.m_textCtrl23.GetValue()
        tenda2 = self.m_textCtrl24.GetValue()
        tas = self.m_textCtrl25.GetValue()
        sepatu = self.m_textCtrl26.GetValue()
        kompor = self.m_textCtrl27.GetValue()

        self.query = "update datapeminjam set nama = \'%s\', ktp = \'%s\', tanggalpeminjaman = \'%s\', tanggalpengembalian = \'%s\', tenda4 = \'%s\', tenda2 = \'%s\', tas = \'%s\', sepatu = \'%s\', kompor = \'%s\' WHERE kodepinjaman = \'%s\'"
        self.query = self.query % (nama, ktp, tanggalpeminjaman, tanggalpengembalian,
                                   tenda4, tenda2, tas, sepatu, kompor, kodepinjaman)
        self.DM.Jalankan(self.query)
        if kodepinjaman != "":
            self.refresh(event)

    def refresh(self, event):
        event = Main3(None, adminn=self.adminn)
        event.Show()
        self.Destroy()

    def btn_deletedatapeminjam(self, event):
        kodepinjaman = self.m_textCtrl18.GetValue()
        self.query = f"DELETE From datapeminjam WHERE kodepinjaman = '{kodepinjaman}'"
        self.DM.Jalankan(self.query)
        if kodepinjaman != "":
            self.refresh(event)

    def button_tambah_peminjam(self, event):
        event = Main4(None)
        event.Show()

    def klik_tambah_admin(self, event):
        event = Main2(None,adminn=self.adminn)
        event.Show()
        self.Destroy()

    def button_keluar(self, event):
        self.DM.conn.close()
        event = Main(None)
        event.Show()
        self.Destroy()


class Main4(Main3, camp.MyFrame4):
    def __init__(self, parent):
        camp.MyFrame4.__init__(self, parent)
        self.DM = DataManager()

    def button_batal(self, event):
        self.Destroy()

    def button_simpan(self, event):
        nama = self.m_textCtrl8.GetValue()
        ktp = self.m_textCtrl9.GetValue()
        tanggalpeminjaman = self.m_textCtrl10.GetValue()
        tanggalpengembalian = self.m_textCtrl11.GetValue()
        tenda4 = self.m_textCtrl12.GetValue()
        tenda2 = self.m_textCtrl13.GetValue()
        tas = self.m_textCtrl14.GetValue()
        sepatu = self.m_textCtrl15.GetValue()
        kompor = self.m_textCtrl15.GetValue()

        if nama != "" and ktp != "" and tanggalpeminjaman != "" and tanggalpengembalian != "" and tenda4 != "" and tenda2 != "" and tas != "" and sepatu != "" and kompor != "":
            self.query = 'INSERT INTO datapeminjam (nama, ktp, tanggalpeminjaman, tanggalpengembalian, tenda4, tenda2, tas, sepatu, kompor) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'
            self.query = self.query % (nama, ktp, tanggalpeminjaman,
                                       tanggalpengembalian, tenda4, tenda2, tas, sepatu, kompor)
            self.DM.Jalankan(self.query)
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')


run = wx.App()
frame = Main(parent=None)
frame.Show()
run.MainLoop()
