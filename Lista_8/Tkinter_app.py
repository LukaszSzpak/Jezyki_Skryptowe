from tkinter import *
from tkinter import messagebox

from App_controller import App_controller


def start_gui():
    app = App_controller()
    window = Tk()

    window.title("Witamy w apce covidowej")
    window.geometry('650x400')

    label1 = Label(window, text='Wersja "suma" ', font=("Arial Bold", 30))
    label1.grid(column=0, row=0)

    label2 = Label(window, text="Rodzaj (zgony/zachorowania): ")
    label2.grid(column=0, row=1)
    deaths_or_cases = Entry(window, width=30)
    deaths_or_cases.grid(column=1, row=1)

    label3 = Label(window, text="Lokalizacja (np. Poland): ")
    label3.grid(column=0, row=2)
    location = Entry(window, width=30)
    location.grid(column=1, row=2)

    label4 = Label(window, text="Miesiąc: (styczeń - grudzień)")
    label4.grid(column=0, row=3)
    date_month = Entry(window, width=30)
    date_month.grid(column=1, row=3)

    label5 = Label(window, text="Dzień (np. 5, 15): ")
    label5.grid(column=0, row=4)
    date_day = Entry(window, width=30)
    date_day.grid(column=1, row=4)

    def normal_data():
        deaths_or_cases_text = deaths_or_cases.get()
        location_text = None if location.get() == '' else location.get()
        date_month_text = None if date_month.get() == '' else date_month.get()
        date_day_text = None
        if len(date_day.get()) == 1:
            date_day_text = '0{0}'.format(date_day.get())
        elif len(date_day.get()) == 2:
            date_day_text = date_day.get()

        if deaths_or_cases_text == 'zgony':
            result_text = app.check_location_and_get_deaths(location=location_text,
                                                            date_month=date_month_text,
                                                            date_day=date_day_text)
        elif deaths_or_cases_text == 'zachorowania':
            result_text = app.check_location_and_get_cases(location=location_text,
                                                           date_month=date_month_text,
                                                           date_day=date_day_text)
        else:
            result_text = 'Błędny rodzaj !'

        if result_text == 0 or result_text == '0':
            result_text = 'Brak danych !'

        messagebox.showinfo('Informacja', result_text)

    btn = Button(window, text="Potwierdź", command=normal_data)
    btn.grid(column=4, row=6)

    label6 = Label(window, text='Wersja "zakres" ', font=("Arial Bold", 30))
    label6.grid(column=0, row=8)

    label7 = Label(window, text="Rodzaj (zgony/zachorowania): ")
    label7.grid(column=0, row=9)
    deaths_or_cases_2 = Entry(window, width=30)
    deaths_or_cases_2.grid(column=1, row=9)

    label8 = Label(window, text="Ilość dni (1-30): ")
    label8.grid(column=0, row=10)
    range = Entry(window, width=30)
    range.grid(column=1, row=10)

    def range_data():
        deaths_or_cases_text = deaths_or_cases_2.get()
        range_text = range.get()

        result_text = ''
        if not range_text.isdigit():
            result_text = 'Zakres nie jest liczbą !'
        elif not 1 <= int(range_text) <= 30:
            result_text = 'Zakres poza skalą !'
        elif deaths_or_cases_text == 'zgony':
            result_text = app.get_max_deaths(int(range_text))
        elif deaths_or_cases_text == 'zachorowania':
            result_text = app.get_max_cases(int(range_text))
        else:
            result_text = 'Błędny wybór !'

        messagebox.showinfo('Informacja', result_text)

    btn2 = Button(window, text="Potwierdź", command=range_data)
    btn2.grid(column=4, row=11)

    window.mainloop()


if __name__ == '__main__':
    start_gui()
