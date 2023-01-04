from tkinter import *

from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):
    print('Button clicked')  # testi
    radius = user_input.get()
    # print(radius)  # Test
    if is_float(radius):
        user_input.delete(0, END)  # Tühjenda input
        radius = float(radius)  # nüüd on raadius float
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # kasutaja saab fieldi muuta(kirjutada)
        txt_field.delete('1.0', END)  # tühjenda 1- lõpuni
        txt_field.insert(END, 'Raadius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Läbimõõt: ' + str(circle.diameter()) + '\n')
        txt_field.insert(END, 'Ümbermõõt: ' + str(circle.perimeter()) + '\n')
        txt_field.insert(END, 'Pindala: ' + str(circle.area()) + '\n')
        txt_field['state'] = 'disabled'  # kasutaja ei saa fieldi muuta(kirjutada

        # print('Number')  # Test
    # else:
        # print('Error')  # Test


# Main window atribuudid
window = Tk()  # Teeb main Windowi akna
window.title('Geometry - Circle')
# window.geometry('400x500')  # w=400 h=500
window.resizable(True, False)  # Laiust saab muuta ja kõrgust ei saa muuta (saab panna nii piirangu mida soovid et saaks muuta)

# Frames (raam)  bg= backround
frame_top = Frame(window, bg='#89CFF0', height=50)  # määran värvi ja kõrguse
frame_top.pack(fill='both')  # panen akna peale, both tähendab, et täislaius

frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)  # võib ka nii kirjutada, suurte tähtedega

# Ülemise raami peale tuleb kolm objekti
lbl = Label(frame_top, text='Ringi raadius', bg='#89CFF0')
lbl.pack(side='left')

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus()

btn_calc = Button(frame_top, text='Arvuta', command=lambda: calculate(0))  # nupu tegemine
btn_calc.pack(side=LEFT, padx=2, pady=2)  # esimene padx muudab küljepealt ja teine pady alt ja ülevalt ruumi

# Second line, one big textfiled (suur teksti kast)
txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side='left', padx=2, pady=2)

#  tuvasta enter klahvi vajutus (seda saab teha vaid ühele nupule)
window.bind('<Return>', lambda event: calculate(event))

# No MVC last line
window.mainloop()
