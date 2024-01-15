import sqlite3

end = True

while end:
    firstname = ['Daniel', 'Declan', 'Ryan', 'Peter', 'end']
    lastname = ['Daniels', 'Bates', 'Adams', 'Schofield']
    address = ['17 Friar Street', '57 Annfield Rd', '54 Iolaire Road', '83 Temple Way']
    phonenumber = ['078 6041 5406', '079 7990 9820', '078 6809 6684', '079 4673 6393']
    predicted = ['AAA', 'BBC', 'BAC', 'CCC']

    for i in range(len(firstname)):
        if firstname == 'end':
            end = False
        connection = sqlite3.connect('D:/Atom/Python/LoginForm/Databases/student_information_year12')
        transfer = connection.cursor()
        transfer.execute('INSERT INTO student_data VALUES(:firstname, :lastname, :address, :phonenumber, :predictedgrades)',
                         {"firstname": firstname[i], "lastname": lastname[i], "address": address[i], "phonenumber": phonenumber[i], "predictedgrades": predicted[i]})
        connection.commit()
