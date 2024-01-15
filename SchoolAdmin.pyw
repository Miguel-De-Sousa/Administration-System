import tkinter as tk
from tkinter import messagebox
from functools import partial
import base64
import csv
import sqlite3

# encrypts passwords for CSV


def Encrypt(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i])+ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def validation(username, password):
    resultPassword = (Encrypt(username.get(), password.get())).split()
    resultUsername = username.get().split()
    message = True
    with open('D:/Paradigms/Python/LoginForm/Databases/username_records.csv', 'r') as csvufile:
        csvureader = csv.reader(csvufile, delimiter=',')
        line_count = 0
        for row in csvureader:
            if row == resultUsername:
                with open('D:/Paradigms/Python/LoginForm/Databases/password_records.csv', 'r') as csvpfile:
                    csvpreader = csv.reader(csvpfile, delimiter=',')
                    for row in csvpreader:
                        if row == resultPassword:
                            root.destroy()
                            mainwindow.deiconify()
                            message = False
        if message:
            messagebox.showerror('', 'invalid username/password')


def registerOpen():

    def registration(newuser, newpass):
        complete = tk.messagebox.askokcancel('', 'Complete Registration?')
        if complete == False:
            messagebox.showinfo('', 'Registration Cancelled')
            return
        with open('D:/Paradigms/Python/LoginForm/Databases/password_records.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([Encrypt(newuser.get(), newpass.get())])
        with open('D:/Paradigms/Python/LoginForm/Databases/username_records.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([newuser.get()])
        registerwindow.destroy()
        mainwindow.deiconify()
        messagebox.showinfo('', 'Registration complete')

    mainwindow.deiconify()
    registerwindow = tk.Tk()
    registerwindow.geometry('200x125')
    registerwindow.title('New Registration')
    registerwindow.withdraw()
    registerwindow.eval('tk::PlaceWindow . center')
    registerwindow.resizable(False, False)

    newuserLabel = tk.Label(registerwindow, text='New Username').pack()
    newuser = tk.StringVar()
    newuserEntry = tk.Entry(registerwindow, textvariable=newuser).pack()

    newpassLabel = tk.Label(registerwindow, text='New Password').pack()
    newpass = tk.StringVar()
    newpassEntry = tk.Entry(registerwindow, textvariable=newpass, show='*').pack()

    registration = partial(registration, newuser, newpass)
    saveButton = tk.Button(registerwindow, text='Save', command=registration).pack()
    registerwindow.bind('<Return>', lambda event: registration())

    registerwindow.mainloop()


root = tk.Tk()
root.geometry('250x175')
root.title('Login Page')
root.overrideredirect(True)
root.configure(background='white')
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)
root.lift()


def FocusIn_username():
    usernameEntry.delete(0, tk.END)
    usernameEntry.config(fg='black')


def FocusIn_password():
    passwordEntry.delete(0, tk.END)
    passwordEntry.config(fg='black')


login_title = tk.Label(root, text='Admin Login', font=('sans', '15', 'bold'), bg='white', fg='#3676d1')
login_title.grid(row=0, column=0, columnspan=2)

UserPicture = tk.PhotoImage(file=r'D:/Paradigms/Python/LoginForm/ProgramImages/UserPicture.png')
UserPicture_sample = UserPicture.subsample(2, 2)
PassPicture = tk.PhotoImage(file=r'D:/Paradigms/Python/LoginForm/ProgramImages/PassPicture.png')
PassPicture_sample = PassPicture.subsample(2, 2)

username_label = tk.Label(root, image=UserPicture_sample).grid(row=1, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(root, textvariable=username, borderwidth=3, fg='grey')
usernameEntry.grid(row=1, column=1, ipady=5, ipadx=20)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', lambda event: FocusIn_username())

password_label = tk.Label(root, image=PassPicture_sample).grid(row=2, column=0)
password = tk.StringVar()
passwordEntry = tk.Entry(root, textvariable=password, borderwidth=3, fg='grey', show='*')
passwordEntry.grid(row=2, column=1, ipady=5, ipadx=20)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', lambda event: FocusIn_password())

validation = partial(validation, username, password)

loginButton = tk.Button(root, text='Login', bg='#3676d1', fg='white', font=('Sans', '14', 'bold'), command=validation)
loginButton.grid(row=3, column=0, columnspan=2, pady=20, ipadx=90, ipady=2)
root.bind('<Return>', lambda event: validation())
root.bind('<Escape>', lambda event: root.destroy())
root.bind('<Down>', lambda event: passwordEntry.focus())
root.bind('<Up>', lambda event: usernameEntry.focus())


mainwindow = tk.Tk()


def destroy():
    mainwindow.destroy()


def FocusIn():
    search_bar.delete(0, tk.END)
    search_bar.config(fg='black')


def FocusOut():
    search_bar.delete(0, tk.END)
    search_bar.config(fg='grey')
    search_bar.insert(0, 'search database')


def InsertRow():
    options = [
        'Student Database',
        'Teacher Database',
        'Cover Database',
        'Cleaner Database'
    ]
    Insert = tk.Tk()
    Insert.title('Administrator Database Management')
    Insert.geometry('400x400')
    selectedDatabase = tk.StringVar()
    DatabaseChoice = tk.OptionMenu(Insert, selectedDatabase, *options)
    DatabaseChoice.pack()

    if selectedDatabase.get() == 'Student Database':
        InsertFN = tk.Entry(Insert, text='Firstname')
        InsertFN.pack()
        InsertLN = tk.Entry(Insert, text='Lastname')
        InsertLN.pack()
        InsertAD = tk.Entry(Insert, text='Address')
        InsertAD.pack()
        InsertPN = tk.Entry(Insert, text='Phonenumber')
        InsertPN.pack()
        InsertPG = tk.Entry(Insert, text='Predicted')
        InsertPG.pack()


mainwindow.withdraw()
mainwindow.attributes('-fullscreen', True)
mainwindow.title('Entry Database')
mainwindow.configure(bg='#ffffff')
mainwindow.bind('<Escape>', lambda event: mainwindow.destroy())

mainwindow_menu = tk.Menu(mainwindow)
mainwindow.config(menu=mainwindow_menu)

file_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
mainwindow_menu.add_cascade(label='File', menu=file_dropdown)
file_dropdown.add_command(label='New')
file_dropdown.add_command(label='Open')
file_dropdown.add_separator()
file_dropdown.add_command(label='Save')
file_dropdown.add_command(label='Save As...')
file_dropdown.add_separator()
file_dropdown.add_command(label='Import')
file_dropdown.add_command(label='Export')
file_dropdown.add_separator()
file_dropdown.add_command(label='Exit', command=destroy)

edit_dropdown = tk.Menu(mainwindow, tearoff=False)
mainwindow.config(menu=mainwindow_menu)
mainwindow_menu.add_cascade(label='Edit', menu=edit_dropdown)
edit_dropdown.add_command(label='Undo')
edit_dropdown.add_command(label='Redo')
edit_dropdown.add_separator()
edit_dropdown.add_command(label='Cut')
edit_dropdown.add_command(label='Copy')
edit_dropdown.add_command(label='Paste')

view_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
mainwindow_menu.add_cascade(label='View', menu=view_dropdown)

insert_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
mainwindow_menu.add_cascade(label='Insert', menu=insert_dropdown)
insert_dropdown.add_command(label='Insert Row', command=InsertRow)
insert_dropdown.add_command(label='Insert Column')
insert_dropdown.add_separator()
insert_dropdown.add_command(label='Clear Row')
insert_dropdown.add_command(label='Clear Column')
insert_dropdown.add_command(label='Clear Data')

register_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
mainwindow_menu.add_cascade(label='Register', menu=register_dropdown)
register_dropdown.add_command(label='Register', command=registerOpen)
register_dropdown.add_command(label='About')

help_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
mainwindow_menu.add_cascade(label='Help', menu=help_dropdown)


def cell_creation(cellrow, cellcolumn, DatabaseInformation):
    unique = tk.Text(mainframe, font=('sans', '15'), borderwidth=2, height=1, width=10)
    unique.insert(tk.END, DatabaseInformation)
    unique.configure(state='disabled')
    unique.grid(row=cellrow, column=cellcolumn)


def studentdatabasePopUp():
    currentdatabase.set('student')
    for widget in mainframe.winfo_children():
        widget.destroy()
    firstname_label = tk.Label(mainframe, text='Firstname', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    firstname_label.grid(row=3, column=1)
    lastname_label = tk.Label(mainframe, text='Lastname',  bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    lastname_label.grid(row=3, column=2)
    address_label = tk.Label(mainframe, text='Address', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    address_label.grid(row=3, column=3)
    phonenumber_label = tk.Label(mainframe, text='Phonenumber', fg='white', bg='#3676d1', font=('sans', '13', 'bold'))
    phonenumber_label.grid(row=3, column=4)
    predicted_label = tk.Label(mainframe, text='Predicted', fg='white', bg='#3676d1', font=('sans', '13', 'bold'))
    predicted_label.grid(row=3, column=5)

    connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/student_information_year12')
    transfer = connection.cursor()
    transfer.execute('SELECT firstname FROM student_data')
    DBfirstname = transfer.fetchall()
    transfer.execute('SELECT lastname FROM student_data')
    DBlastname = transfer.fetchall()
    transfer.execute('SELECT address FROM student_data')
    DBaddress = transfer.fetchall()
    transfer.execute('SELECT phonenumber FROM student_data')
    DBphonenumber = transfer.fetchall()
    transfer.execute('SELECT predicted FROM student_data')
    DBpredicted = transfer.fetchall()
    connection.close()
    for row in range(36):
        for column in range(5):
            if column == 0:
                cell_creation(row+4, column+1,  DBfirstname[row-1])
            elif column == 1:
                cell_creation(row+4, column+1, DBlastname[row-1])
            elif column == 2:
                cell_creation(row+4, column+1, DBaddress[row-1])
            elif column == 3:
                cell_creation(row+4, column+1, DBphonenumber[row-1])
            elif column == 4:
                cell_creation(row+4, column+1, DBpredicted[row-1])


def teacherdatabasePopUp():
    currentdatabase.set('teacher')
    for widget in mainframe.winfo_children():
        widget.destroy()
    firstname_label = tk.Label(mainframe, text='Firstname', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    firstname_label.grid(row=3, column=1)
    lastname_label = tk.Label(mainframe, text='Lastname',  bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    lastname_label.grid(row=3, column=2)
    subject_label = tk.Label(mainframe, text='Subject', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    subject_label.grid(row=3, column=3)
    phonenumber_label = tk.Label(mainframe, text='Phonenumber', fg='white', bg='#3676d1', font=('sans', '13', 'bold'))
    phonenumber_label.grid(row=3, column=4)

    connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/teacher_information')
    transfer = connection.cursor()
    transfer.execute('SELECT firstname FROM teacher_data')
    DBfirstname = transfer.fetchall()
    transfer.execute('SELECT lastname FROM teacher_data')
    DBlastname = transfer.fetchall()
    transfer.execute('SELECT subject FROM teacher_data')
    DBsubject = transfer.fetchall()
    transfer.execute('SELECT phonenumber FROM teacher_data')
    DBphonenumber = transfer.fetchall()
    connection.close()
    for row in range(36):
        for column in range(4):
            if column == 0:
                cell_creation(row+4, column+1,  DBfirstname[row-1])
            elif column == 1:
                cell_creation(row+4, column+1, DBlastname[row-1])
            elif column == 2:
                cell_creation(row+4, column+1, DBsubject[row-1])
            elif column == 3:
                cell_creation(row+4, column+1, DBphonenumber[row-1])


def coverdatabasePopUp():
    currentdatabase.set('cover')
    for widget in mainframe.winfo_children():
        widget.destroy()
    firstname_label = tk.Label(mainframe, text='Firstname', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    firstname_label.grid(row=3, column=1)
    lastname_label = tk.Label(mainframe, text='Lastname',  bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    lastname_label.grid(row=3, column=2)
    subjectCover_label = tk.Label(mainframe, text='SubjectCover', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    subjectCover_label.grid(row=3, column=3)
    phonenumber_label = tk.Label(mainframe, text='Phonenumber', fg='white', bg='#3676d1', font=('sans', '13', 'bold'))
    phonenumber_label.grid(row=3, column=4)

    connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/cover_information')
    transfer = connection.cursor()
    transfer.execute('SELECT firstname FROM cover_data')
    DBfirstname = transfer.fetchall()
    transfer.execute('SELECT lastname FROM cover_data')
    DBlastname = transfer.fetchall()
    transfer.execute('SELECT coversubject FROM cover_data')
    DBcoversubject = transfer.fetchall()
    transfer.execute('SELECT phonenumber FROM cover_data')
    DBphonenumber = transfer.fetchall()
    connection.close()

    for row in range(36):
        for column in range(4):
            if column == 0:
                cell_creation(row+4, column+1,  DBfirstname[row-1])
            elif column == 1:
                cell_creation(row+4, column+1, DBlastname[row-1])
            elif column == 2:
                cell_creation(row+4, column+1, DBcoversubject[row-1])
            elif column == 3:
                cell_creation(row+4, column+1, DBphonenumber[row-1])


def cleanerdatabasePopUp():
    currentdatabase.set('cleaner')
    for widget in mainframe.winfo_children():
        widget.destroy()
    firstname_label = tk.Label(mainframe, text='Firstname', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    firstname_label.grid(row=3, column=1)
    lastname_label = tk.Label(mainframe, text='Lastname',  bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    lastname_label.grid(row=3, column=2)
    contractType_label = tk.Label(mainframe, text='ContractType', bg='#3676d1', fg='white', font=('sans', '13', 'bold'))
    contractType_label.grid(row=3, column=3)
    phonenumber_label = tk.Label(mainframe, text='Phonenumber', fg='white', bg='#3676d1', font=('sans', '13', 'bold'))
    phonenumber_label.grid(row=3, column=4)

    connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/cleaner_information')
    transfer = connection.cursor()
    transfer.execute('SELECT firstname FROM cleaner_data')
    DBfirstname = transfer.fetchall()
    transfer.execute('SELECT lastname FROM cleaner_data')
    DBlastname = transfer.fetchall()
    transfer.execute('SELECT contracttype FROM cleaner_data')
    DBcontracttype = transfer.fetchall()
    transfer.execute('SELECT phonenumber FROM cleaner_data')
    DBphonenumber = transfer.fetchall()
    connection.close()
    for row in range(36):
        for column in range(4):
            if column == 0:
                cell_creation(row+4, column+1,  DBfirstname[row-1])
            elif column == 1:
                cell_creation(row+4, column+1, DBlastname[row-1])
            elif column == 2:
                cell_creation(row+4, column+1, DBcontracttype[row-1])
            elif column == 3:
                cell_creation(row+4, column+1, DBphonenumber[row-1])


'''def displayselected():
    if currentdatabase.get=='student':
        connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/student_infomration')
        transfer = connection.cursor()
        transfer.execute('SELECT * FROM student_data WHERE firstname OR lastname OR address OR phonenumber OR predicted LIKE {}'.format(searchvariable.get()))
        showInfo= transfer.fetchall()
        for widget in mainframe.winfo_children():
            widget.destroy()'''


selectframe = tk.LabelFrame(mainwindow, highlightthickness=2, bg='#3676d1')
selectframe.grid(row=0, column=0, ipady=153)

abbeygate_Logo = tk.PhotoImage(file=r'D:/Paradigms/Python/LoginForm/ProgramImages/abbeygate.png', master=mainwindow)
abbeygateLogo_sample = abbeygate_Logo.subsample(1, 1)

logoLabel = tk.Label(selectframe, image=abbeygateLogo_sample, borderwidth=0)
logoLabel.pack(pady=10)

searchvariable = tk.StringVar()
search_bar = tk.Entry(selectframe, textvariable=searchvariable, fg='grey', borderwidth=2, font=('sans', '15'))
search_bar.pack(pady=10)
search_bar.insert(0, 'search database...')
search_bar.bind('<FocusIn>', lambda event: FocusIn())
search_bar.bind('<FocusOut>', lambda event: FocusOut())
search_database_BTN = tk.Button(selectframe, text='Search', bg='#3676d1',
                                fg='white', font=('sans', '13', 'bold'))
search_database_BTN.pack(ipadx=10)

breakerLabel = tk.Label(selectframe, text='-----------------',
                        borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
breakerLabel.pack()

identifyLabel = tk.Label(selectframe, text='Students',
                         borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
identifyLabel.pack(pady=10)
breakerLabel = tk.Label(selectframe, text='-----------------',
                        borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
breakerLabel.pack()
student12_database_BTN = tk.Button(selectframe, text='Year 12 Database', bg='#3676d1',
                                   fg='white', relief='flat', font=('sans', '13', 'bold'), command=studentdatabasePopUp)
student12_database_BTN.pack(pady=20)
student13_database_BTN = tk.Button(selectframe, text='Year 13 Database', bg='#3676d1',
                                   fg='white', relief='flat', font=('sans', '13', 'bold'), command=studentdatabasePopUp)
student13_database_BTN.pack(pady=20)
breakerLabel = tk.Label(selectframe, text='-----------------',
                        borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
breakerLabel.pack()
identifyLabel = tk.Label(selectframe, text='Employees',
                         borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
identifyLabel.pack(pady=10)
breakerLabel = tk.Label(selectframe, text='-----------------',
                        borderwidth=0, bg='#3676d1', fg='white', relief='flat', font=('sans', '13', 'bold'))
breakerLabel.pack()
teacher_database_BTN = tk.Button(selectframe, text='Teacher Database', bg='#3676d1',
                                 fg='white', relief='flat', font=('sans', '13', 'bold'), command=teacherdatabasePopUp)
teacher_database_BTN.pack(pady=20)
cover_database_BTN = tk.Button(selectframe, text='Cover Database', bg='#3676d1',
                               fg='white', relief='flat', font=('sans', '13', 'bold'), command=coverdatabasePopUp)
cover_database_BTN.pack(pady=20)
cleaner_database_BTN = tk.Button(selectframe, text='Cleaner Database', bg='#3676d1',
                                 fg='white', relief='flat', font=('sans', '13', 'bold'), command=cleanerdatabasePopUp)
cleaner_database_BTN.pack(pady=20)

mainframe = tk.LabelFrame(mainwindow, highlightthickness=2, bg='#3676d1')
mainframe.grid(row=0, column=1)
currentdatabase = tk.StringVar()


mainwindow.mainloop()

root.mainloop()
