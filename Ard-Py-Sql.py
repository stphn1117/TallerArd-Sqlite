import sys, time, serial, sqlite3

#cursor.execute('CREATE TABLE employees(id INTEGER PRIMARY KEY, value TEXT)')
#cursor.execute('INSERT INTO employees VALUES (?,?)', (2,"(b'102\r\n')"))


serialPort ='COM3'
flagCharacter = 107


#     ______________________________________
#____/PRIMER CORRIDA: CREAR LA BASE DE DATOS

"""
primero solo se escribe este código para crear un archivo de base de datos
y especificar la tabla en donde se intriducirá los datos,
esta tabla tendrá un ID y un VALUE


def Conection():
    connection = sqlite3.connect('FotoData.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE Fotocelda(id INTEGER PRIMARY KEY, value TEXT)')
"""

#     ______________________________________________
#____/SEGUNDA CORRIDA: INTRODUCIR DATOS Y OBTENERLOS

"""
La razon po la cual no se puede hacer todo junto, es porque cada vez
que se corra el programa este creará nuevamente una tabla con el mismo nombre
y por tanto habrá un error

connection = sqlite3.connect('FotoData.db') esta linea tiene la particularidad de que
si la bd no está entonces la crea, pero si ya existe, solo la utiliza por esa razon no
hay problema al usarla
"""

def Conection():
    connection = sqlite3.connect('FotoData.db')
    cursor = connection.cursor()
    #cursor.execute('CREATE TABLE Fotocelda(id INTEGER PRIMARY KEY, value TEXT)')
    infoSerial(connection, cursor)
    


#   _______________________
#__/conexión con el Arduino

"""
Para esta parte de especifica el puerto serial, que es el puerto donde se conectó
el arduino, y la velocidad de lectura del dato especificada en el arduino

en este caso:
arduinoPort = serial.Serial(serialPort, 9600, timeout=1)
"""



def infoSerial(con, cur):
 print ('\nDatos generales de la comunicación serial establecida')
 
 #   _________
 #__/Iniciando: conexión serial
 arduinoPort = serial.Serial(serialPort, 9600, timeout=1)
 
 print ('\nIniciando conexion.....')
 #   _____
 #__/Reset: manual del Arduino
 arduinoPort.setDTR(False)  
 time.sleep(0.3)
 arduinoPort.flushInput()  
 arduinoPort.setDTR()  
 time.sleep(0.3)

 print ('\nEstado del puerto: %s ' % (arduinoPort.isOpen()))
 print ('Nombre del dispositivo conectado: %s ' % (arduinoPort.name))

 

 
 insert(con,cur,arduinoPort)
 



#   ___________________________________________
#__/introducción de datos obtenidos del arduino




def insert(con,cur,DF):

    print("\nInsertando los datos...")
    i=0
    while(i<=10):
        cur.execute('INSERT INTO Fotocelda(value) VALUES (?)',(DF.readline(),))
        con.commit()
        i= i+1
    
    imp(con)


#  _________________________________________
#_/Obtención de datos desde la base de datos

def imp(x):
    cursorN = x.cursor()
    cursorN.execute('SELECT * FROM Fotocelda')
    rows = cursorN.fetchall()
    
    print("\nObteniendo los datos desde la base de datos")
    for row in rows:
        print(row)

    x.close()



Conection()
