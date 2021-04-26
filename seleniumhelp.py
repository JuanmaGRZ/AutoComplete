import pyodbc 

server = 'DESKTOP-40TDACU' 
database = 'DBLicencia' 
username = 'juanma' 
password = 'asdasd123' 
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-40TDACU;'
                      'Database=DBLicencia;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("SELECT TOP(1) Nombre,Dni,Genero FROM dbo.Tramites")
resultado = cursor.fetchall()
tabla = [list(i) for i in resultado]
tabla_final = tabla[0]
print(tabla_final[0])