# main.py

# Importa la clase desde el archivo mi_clase
from mi_clase import Alumno

for i in range(3):
    alumno = Alumno()
    alumno.set_nombre(input("Introduce el nombre del alumno: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el No. de Control del alumno: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))