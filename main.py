import sqlite3
from datetime import date

from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        global IDdana
        self.showMaximized()
        self.setId()
        self.ucitajBazu(IDdana)
        self.save_btn.clicked.connect(self.sacuvajPromene)
        self.next_btn.clicked.connect(self.sledecaNedelja)
        self.prev_btn.clicked.connect(self.prethodnaNedelja)
        self.add_btn.clicked.connect(self.dodajZadatak)
        print("first commit")

    def dodajZadatak(self):
        db = sqlite3.connect("baza.db")
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        if newTask == "":
            return

        query = "SELECT * FROM Zadaci WHERE id = ?"
        row = (IDdana + self.cb_day.currentIndex(),)

        results = cursor.execute(query, row)
        db.commit()

        zadaci = ""
        uradjen = ""
        for result in results:
            zadaci = result[1]
            uradjen = result[2]

        if zadaci != "":
            zadaci = zadaci + ", " + newTask
            uradjen = uradjen + ", " + "NO"
        else:
            zadaci = newTask
            uradjen = "NO"

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        query = "UPDATE Zadaci SET zadatak = ?, uradjen = ? WHERE id = ?"
        row = (zadaci, uradjen, IDdana + self.cb_day.currentIndex(),)
        cursor.execute(query, row)
        db.commit()
        self.ucitajBazu(IDdana)
        self.taskLineEdit.clear()

    def prethodnaNedelja(self):
        global IDdana
        if IDdana == 1:
            print("Ne postoji prethodna nedelja u bazi!")
        else:
            IDdana = IDdana - 7
            self.ucitajBazu(IDdana)

    def setId(self):
        db = sqlite3.connect("baza.db")
        cursor = db.cursor()

        query0 = "SELECT id FROM DnevneObaveze where DanID = ?"
        row0 = (date.today(),)
        results0 = cursor.execute(query0, row0)
        print(results0)
        trazeni_id = 0
        for result in results0:
            trazeni_id = result[0]
        global IDdana
        IDdana = trazeni_id - date.today().weekday()

    def sledecaNedelja(self, id):
        global IDdana
        IDdana = IDdana + 7
        self.ucitajBazu(IDdana)

    def sacuvajPromene(self):

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        id = IDdana
        osam = str(self.textM8.toPlainText())
        deset = str(self.textM10.toPlainText())
        dvanaest = str(self.textM12.toPlainText())
        cetrnaest = str(self.textM14.toPlainText())
        sesnaest = str(self.textM16.toPlainText())
        osamnaest = str(self.textM18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        print("BROJAC", self.listWidgetM.count())
        for i in range(self.listWidgetM.count()):
            print("Usao u petlju")
            print(self.listWidgetM.count())
            item = self.listWidgetM.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            elif item.checkState() == QtCore.Qt.Unchecked:
                uradjen = uradjen + "NO, "

        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textT8.toPlainText())
        deset = str(self.textT10.toPlainText())
        dvanaest = str(self.textT12.toPlainText())
        cetrnaest = str(self.textT14.toPlainText())
        sesnaest = str(self.textT16.toPlainText())
        osamnaest = str(self.textT18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        for i in range(self.listWidgetT.count()):
            item = self.listWidgetT.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textW8.toPlainText())
        deset = str(self.textW10.toPlainText())
        dvanaest = str(self.textW12.toPlainText())
        cetrnaest = str(self.textW14.toPlainText())
        sesnaest = str(self.textW16.toPlainText())
        osamnaest = str(self.textW18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        for i in range(self.listWidgetW.count()):
            item = self.listWidgetW.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textTH8.toPlainText())
        deset = str(self.textTH10.toPlainText())
        dvanaest = str(self.textTH12.toPlainText())
        cetrnaest = str(self.textTH14.toPlainText())
        sesnaest = str(self.textTH16.toPlainText())
        osamnaest = str(self.textTH18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        for i in range(self.listWidgetTH.count()):
            item = self.listWidgetTH.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textF8.toPlainText())
        deset = str(self.textF10.toPlainText())
        dvanaest = str(self.textF12.toPlainText())
        cetrnaest = str(self.textF14.toPlainText())
        sesnaest = str(self.textF16.toPlainText())
        osamnaest = str(self.textF18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()


        uradjen = ""
        for i in range(self.listWidgetF.count()):
            item = self.listWidgetF.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textS8.toPlainText())
        deset = str(self.textS10.toPlainText())
        dvanaest = str(self.textS12.toPlainText())
        cetrnaest = str(self.textS14.toPlainText())
        sesnaest = str(self.textS16.toPlainText())
        osamnaest = str(self.textS18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        for i in range(self.listWidgetS.count()):
            item = self.listWidgetS.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()
        osam = str(self.textSU8.toPlainText())
        deset = str(self.textSU10.toPlainText())
        dvanaest = str(self.textSU12.toPlainText())
        cetrnaest = str(self.textSU14.toPlainText())
        sesnaest = str(self.textSU16.toPlainText())
        osamnaest = str(self.textSU18.toPlainText())
        query = "UPDATE DnevneObaveze SET o_casova = ?, d_casova = ?, dv_casova = ?, c_casova = ?, s_casova = ?, os_casova = ? WHERE id = ?"
        row = (osam, deset, dvanaest, cetrnaest, sesnaest, osamnaest, id,)
        cursor.execute(query, row)
        db.commit()

        uradjen = ""
        for i in range(self.listWidgetSU.count()):
            item = self.listWidgetSU.item(i)
            task = str(item)
            if item.checkState() == QtCore.Qt.Checked:
                uradjen = uradjen + "YES, "
            else:
                uradjen = uradjen + "NO, "
        if uradjen != "":
            db = sqlite3.connect("baza.db")
            cursor = db.cursor()
            query = "UPDATE Zadaci SET uradjen = ? WHERE id = ?"
            row = (uradjen, id,)
            cursor.execute(query, row)
            db.commit()
        id = id + 1


    def ucitajBazu(self, pocetni_id):

        db = sqlite3.connect("baza.db")
        cursor = db.cursor()

        query = "SELECT * FROM DnevneObaveze d JOIN Zadaci z on d.id = z.id WHERE d.id BETWEEN ? AND ? ORDER BY z.id ASC"
        row = (pocetni_id, pocetni_id + 6,)
        results = cursor.execute(query, row)
        nedelja = ""

        i = 0
        for result in results:
            if i == 0:
                datum = result[0].split("-")
                self.text_monday.setText("Ponedeljak " + datum[2] + "." + datum[1] + ".")
                self.textM8.setText(result[1])
                self.textM10.setText(result[2])
                self.textM12.setText(result[3])
                self.textM14.setText(result[4])
                self.textM16.setText(result[5])
                self.textM18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetM.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetM.addItem(item)
                i = i + 1
                nedelja = datum[2] + "." + datum[1] + "."

            elif i == 1:
                datum = result[0].split("-")
                self.text_tuesday.setText("Utorak " + datum[2] + "." + datum[1] + ".")
                self.textT8.setText(result[1])
                self.textT10.setText(result[2])
                self.textT12.setText(result[3])
                self.textT14.setText(result[4])
                self.textT16.setText(result[5])
                self.textT18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetT.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetT.addItem(item)
                i = i + 1

            elif i == 2:
                datum = result[0].split("-")
                self.text_wednesday.setText("Sreda " + datum[2] + "." + datum[1] + ".")
                self.textW8.setText(result[1])
                self.textW10.setText(result[2])
                self.textW12.setText(result[3])
                self.textW14.setText(result[4])
                self.textW16.setText(result[5])
                self.textW18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetW.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetW.addItem(item)
                i = i + 1

            elif i == 3:
                datum = result[0].split("-")
                self.text_thursday.setText("Četvrtak " + datum[2] + "." + datum[1] + ".")
                self.textTH8.setText(result[1])
                self.textTH10.setText(result[2])
                self.textTH12.setText(result[3])
                self.textTH14.setText(result[4])
                self.textTH16.setText(result[5])
                self.textTH18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetTH.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetTH.addItem(item)
                i = i + 1

            elif i == 4:
                datum = result[0].split("-")
                self.text_friday.setText("Petak " + datum[2] + "." + datum[1] + ".")
                self.textF8.setText(result[1])
                self.textF10.setText(result[2])
                self.textF12.setText(result[3])
                self.textF14.setText(result[4])
                self.textF16.setText(result[5])
                self.textF18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetF.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetF.addItem(item)
                i = i + 1

            elif i == 5:
                datum = result[0].split("-")
                self.text_saturday.setText("Subota " + datum[2] + "." + datum[1] + ".")
                self.textS8.setText(result[1])
                self.textS10.setText(result[2])
                self.textS12.setText(result[3])
                self.textS14.setText(result[4])
                self.textS16.setText(result[5])
                self.textS18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetS.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetS.addItem(item)
                i = i + 1

            elif i == 6:
                datum = result[0].split("-")
                self.text_sunday.setText("Nedelja " + datum[2] + "." + datum[1] + ".")
                self.textSU8.setText(result[1])
                self.textSU10.setText(result[2])
                self.textSU12.setText(result[3])
                self.textSU14.setText(result[4])
                self.textSU16.setText(result[5])
                self.textSU18.setText(result[6])
                zadaci = result[9].split(", ")
                uradjeni = result[10].split(", ")
                self.listWidgetSU.clear()
                if uradjeni[0] != "":
                    for zadatak, uradjen in zip(zadaci, uradjeni):
                        item = QListWidgetItem(str(zadatak))
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                        if uradjen == "YES":
                            item.setCheckState(QtCore.Qt.Checked)
                        elif uradjen == "NO":
                            item.setCheckState(QtCore.Qt.Unchecked)
                        self.listWidgetSU.addItem(item)
                i = i + 1
                nedelja = nedelja + " - " + datum[2] + "." + datum[1] + "."

            self.text_date.setText(nedelja)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
