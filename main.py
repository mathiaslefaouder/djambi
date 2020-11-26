import tkinter

if __name__ == '__main__':
    fenetre = tkinter.Tk()
    fenetre.title('Djambi')
    label = tkinter.Label(fenetre, text='Bonjour')
    label.pack()
    fenetre.mainloop()
