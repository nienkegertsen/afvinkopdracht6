import mysql.connector
import tkinter
from tkinter import messagebox

conn = mysql.connector.connect(host="145.74.104.145",
                               user="nzkst",
                               password="Aa650868!",
                               auth_plugin='mysql_native_password',
                               db="nzkst")

class Applicatie:
    def __init__(self):
        """"Opbouw GUI"""

        self.__cursor = conn.cursor()
        try:
            # Maakt main-window aan
            self.main_window = tkinter.Tk()
            # Maakt de achtergrond kleur van de window wit.
            self.main_window.config(bg="white")
            # Geeft de main window een naam.
            self.main_window.title("PyPiep 0.01 alpha")
            # Maakt drie frames aan en geeft met config ook deze frames
            # Een kleur.
            self.top_frame = tkinter.Frame(self.main_window)
            self.top_frame.config(bg="white")
            self.middle_frame = tkinter.Frame(self.main_window)
            self.middle_frame.config(bg="white")
            self.bottom_frame = tkinter.Frame(self.main_window)
            self.bottom_frame.config(bg="white")

            # create the widgets for the topframe
            self.bericht_entry = tkinter.Entry(self.top_frame,
                                               width= 25)
            self.post_button = tkinter.Button(self.top_frame,
                                              text = "Plaats Bericht",
                                              bg="light grey",
                                              command=self.post)

            # create the widgets for the middle frame
            self.ververs_button = tkinter.Button(self.middle_frame,
                                                 text= "Ververs",
                                                 bg= "light grey",
                                                 command=self.show)
            self.text_label = tkinter.Label(self.middle_frame,
                                            text="     Filter op #tag",
                                            bg= "white")
            self.filter_entry = tkinter.Entry(self.middle_frame,
                                              width=15)

            # Pack de frames
            self.top_frame.pack()
            self.middle_frame.pack()
            self.bottom_frame.pack()
            # pack the top frame's widgets
            self.bericht_entry.pack(side="left")
            self.post_button.pack(side="right")
            # pack the middle frame's widgets
            self.ververs_button.pack(side="left")
            self.text_label.pack(side="left")
            self.filter_entry.pack(side="right")
            # Zorgt dat de GUI verschijnt
            tkinter.mainloop()
        except NameError:
            print("Is de module tkinter bovenaan geimporteerd?")

    def post(self):
        """

        :return:
        """
        tekst = str(self.bericht_entry.get())
        bericht = ("insert into piep(bericht, datum, tijd, student_nr) \
        values ('{}', curdate(), curtime(), '123456')").format\
            (tekst)

        self.__cursor.execute(bericht)
        conn.commit()

    def show(self):
        """

        :return:
        """
        zoeken = str(self.filter_entry.get())
        self.__cursor.execute("select voornaam, bericht, datum, tijd\
        from piep natural join student\
        where bericht like '%#"+zoeken+"%'")
        alle_rijen = self.__cursor.fetchall()
        tkinter.messagebox.showinfo("berichten", alle_rijen)


if __name__ == '__main__':
    applicatie_1 = Applicatie()





