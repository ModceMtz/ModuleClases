class Alumno:
    #crea la function constructor con atributos vacíos
    def __init__(self):
        # Atributos privados
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos 'set' para agregar valores a los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos 'get' para obtener los valores de los atributos
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_nombre_completo(self):
        return self.__nombre+" "+ self.__apellido_paterno+" "+ self.__apellido_materno


registro_alumnos = {}

#ciclo para capturar los registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre(input("Introduce el nombre del alumno: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el No. de Control del alumno: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

#ciclo para capturar los nombres de los registros
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")

# alumno.set_nombre("Victor")
# alumno.set_apellido_paterno("Garcia")
# alumno.set_apellido_materno("Lopez")
# alumno.set_no_control("12345678")
# alumno.set_semestre(5)

registro_alumnos[3] = alumno
