
from datetime import datetime

class ImplanteMedico:
    def __init__(self, tipo, material, tamaño):
        self.tipo = tipo
        self.material = material
        self.tamaño = tamaño

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    def __str__(self):
        return f"Tipo: {self.tipo}\nMaterial: {self.material}\nTamaño: {self.tamaño}"
    def calcular_volumen(self):
        volumen = 0  
        return volumen


def main():
    implante = ImplanteMedico("Implante", "Material", "Tamaño")
    print("Información del implante:")
    print(implante)
    print("Volumen del implante:", implante.calcular_volumen())


class Marcapasos(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, electrodos, inalambrico, frecuencia_estimulacion):
        super().__init__(tipo, material, tamaño)
        self.electrodos = electrodos
        self.inalambrico = inalambrico
        self.frecuencia_estimulacion = frecuencia_estimulacion

    def __str__(self):
        return super().__str__() + f"\nElectrodos: {self.electrodos}\nInalámbrico: {self.inalambrico}\nFrecuencia de Estimulación: {self.frecuencia_estimulacion}"


class StentCoronario(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, diámetro, sistema_fijacion, tipo_fijacion):
        super().__init__(tipo, material, tamaño)
        self.diámetro = diámetro
        self.sistema_fijacion = sistema_fijacion
        self.tipo_fijacion = tipo_fijacion

    def __str__(self):
        return super().__str__() + f"\nDiámetro: {self.diámetro}\nSistema de Fijación: {self.sistema_fijacion}\nTipo de Fijación: {self.tipo_fijacion}"


class ImplanteDental(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, tipo_fijacion):
        super().__init__(tipo, material, tamaño)
        self.tipo_fijacion = tipo_fijacion

    def __str__(self):
        return super().__str__() + f"\nTipo de Fijación: {self.tipo_fijacion}"


class ImplanteRodilla(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, tipo_fijacion):
        super().__init__(tipo, material, tamaño)
        self.tipo_fijacion = tipo_fijacion

    def __str__(self):
        return super().__str__() + f"\nTipo de Fijación: {self.tipo_fijacion}"


class ImplanteCadera(ImplanteMedico):
    def __init__(self, tipo, material, tamaño, tipo_fijacion):
        super().__init__(tipo, material, tamaño)
        self.tipo_fijacion = tipo_fijacion

    def __str__(self):
        return super().__str__() + f"\nTipo de Fijación: {self.tipo_fijacion}"


class RegistroPacientes:
    def __init__(self):
        self.implantes_asignados = {}

    def asignar_implante(self, paciente, implante, fecha_implantacion, medico_responsable, estado):
        self.implantes_asignados[implante] = {
            "paciente": paciente,
            "fecha_implantacion": fecha_implantacion,
            "medico_responsable": medico_responsable,
            "estado": estado
        }

    def mostrar_implantes_asignados(self):
        for implante, info in self.implantes_asignados.items():
            print(f"Implante: {implante.tipo}\n"
                  f"Paciente: {info['paciente']}\n"
                  f"Fecha de Implante: {info['fecha_implantacion']}\n"
                  f"Médico Responsable: {info['medico_responsable']}\n"
                  f"Estado: {info['estado']}\n")


class SistemaGestionImplantes:
    def __init__(self):
        self.inventario = []

    def agregar_implante(self, implante):
        self.inventario.append(implante)
        print("Implante agregado al inventario exitosamente.")

    def eliminar_implante(self, implante):
        if implante in self.inventario:
            self.inventario.remove(implante)
            print("Implante eliminado del inventario exitosamente.")
        else:
            print("El implante no está en el inventario.")

    def editar_implante(self, implante, atributo, nuevo_valor):
        if hasattr(implante, atributo):
            setattr(implante, atributo, nuevo_valor)
            print("Implante editado correctamente.")
        else:
            print("El atributo especificado no existe para este implante.")

    def mostrar_inventario(self):
        if self.inventario:
            print("---------------Inventario de Implantes---------------")
            for i, implante in enumerate(self.inventario, 1):
                print(f"Implante {i}:\n{implante}\n")
        else:
            print("El inventario está vacío.")


    def vida_util(self):
        for implante, info in self.registro_pacientes.implantes_asignados.items():
            fecha_implantacion = datetime.strptime(info['fecha_implantacion'], "%Y-%m-%d")
            fecha_actual = datetime.now()
            vida_util = fecha_actual - fecha_implantacion
            print(f"Implante: {implante.tipo}\n"
                  f"Paciente: {info['paciente']}\n"
                  f"Fecha de Implante: {info['fecha_implantacion']}\n"
                  f"Vida útil: {vida_util.days} días\n")


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Menu:
    def __init__(self):
        self.usuarios = {"Juan": "12345"}  # Usuario y contraseña
        self.usuario_actual = None
        self.sistema_implantes = SistemaGestionImplantes()
        self.registro_pacientes = RegistroPacientes()

    def iniciar_sesion(self):
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if username in self.usuarios and self.usuarios[username] == password:
            print("Inicio de sesión exitoso.")
            self.usuario_actual = Usuario(username, password)
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def mostrar_menu_principal(self):
        while True:
            print("\n---------------Menú Principal---------------")
            print("1. Agregar Implante")
            print("2. Eliminar Implante")
            print("3. Mostrar Implantes")
            print("4. Editar Implante")
            print("5. Mostrar Inventario Completo")
            print("6. Vida Útil de Implantes")
            print("7. Cerrar Sesión")  # Opción para cerrar sesión
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_implante()
            elif opcion == "2":
                self.eliminar_implante()
            elif opcion == "3":
                self.mostrar_implantes()
            elif opcion == "4":
                self.editar_implante()
            elif opcion == "5":
                self.mostrar_inventario()
            elif opcion == "6":
                self.vida_util()
            elif opcion == "7":
                print("Sesion cerrada exitosamente.")
                self.usuario_actual = None
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def agregar_implante(self):
        tipo_implante = input("Ingrese el tipo de implante: ")
        material = input("Ingrese el material del implante")

        implante = input("Ingrese el tamaño del implante: ")
        tamaño = input("Ingrese el tamaño del implante: ")

        nuevo_implante = ImplanteMedico(tipo_implante, material, tamaño)

        self.sistema_implantes.agregar_implante(nuevo_implante)

        self.sistema_implantes.mostrar_inventario()

        num_implante = int(input("Ingrese el número del implante que desea asignar: "))
        try:
            implante_seleccionado = self.sistema_implantes.inventario[num_implante - 1]
        except IndexError:
            print("Número de implante no válido.")
            return

        paciente = input("Ingrese el nombre del paciente: ")
        fecha_implantacion = input("Ingrese la fecha de implantación (YYYY-MM-DD): ")
        medico_responsable = input("Ingrese el nombre del médico responsable: ")
        estado = input("Ingrese el estado del implante (Activo/Inactivo): ")
        self.registro_pacientes.asignar_implante(paciente, implante_seleccionado, fecha_implantacion, medico_responsable, estado)
        print("Implante asignado al paciente.")

        if self.usuario_actual:
            paciente = input("Ingrese el nombre del paciente: ")
            fecha_implantacion = input("Ingrese la fecha de implantación: ")
            medico_responsable = input("Ingrese el médico responsable: ")
            estado = input("Ingrese el estado del implante: ")
            self.registro_pacientes.asignar_implante(paciente, nuevo_implante, fecha_implantacion, medico_responsable, estado)

    def eliminar_implante(self):
        if self.sistema_implantes.inventario:
            self.sistema_implantes.mostrar_inventario()
            numero_implante = int(input("Ingrese el número del implante que desea eliminar: "))
            if 1 <= numero_implante <= len(self.sistema_implantes.inventario):
                implante_a_eliminar = self.sistema_implantes.inventario[numero_implante - 1]
                self.sistema_implantes.eliminar_implante(implante_a_eliminar)
            else:
                print("Número de implante inválido.")
        else:
            print("El inventario está vacío.")

    def mostrar_implantes(self):
        self.registro_pacientes.mostrar_implantes_asignados()

    def editar_implante(self):
        if self.sistema_implantes.inventario:
            self.sistema_implantes.mostrar_inventario()
            numero_implante = int(input("Ingrese el número del implante que desea editar: "))
            if 1 <= numero_implante <= len(self.sistema_implantes.inventario):
                implante_a_editar = self.sistema_implantes.inventario[numero_implante - 1]
                atributo = input("Ingrese el atributo que desea editar: ")
                nuevo_valor = input("Ingrese el nuevo valor: ")
                self.sistema_implantes.editar_implante(implante_a_editar, atributo, nuevo_valor)
            else:
                print("Número de implante inválido.")
        else:
            print("El inventario está vacío.")

    def mostrar_inventario(self):
        self.sistema_implantes.mostrar_inventario()


    def mostrar_implantes(self):
        self.registro_pacientes.mostrar_implantes_asignados()

    def mostrar_inventario(self):
        self.sistema_implantes.mostrar_inventario()

    def vida_util(self):
        self.sistema_implantes.vida_util()

    def vida_util(self):
        print("\n---------------Registro de Vida Útil de Implantes---------------")
        for implante, info in self.registro_pacientes.implantes_asignados.items():
            fecha_implantacion = datetime.strptime(info['fecha_implantacion'], "%Y-%m-%d")
            fecha_actual = datetime.now()
            vida_util = fecha_actual - fecha_implantacion
            print(f"Implante: {implante.tipo}\n"
                  f"Paciente: {info['paciente']}\n"
                  f"Fecha de Implante: {info['fecha_implantacion']}\n"
                  f"Vida útil: {vida_util.days} días\n")

if __name__ == "__main__":
    main()
    menu = Menu()
    while menu.usuario_actual is None:
        menu.iniciar_sesion()
    if menu.usuario_actual is not None:
        menu.mostrar_menu_principal()
