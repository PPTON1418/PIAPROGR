class Empleado:
    def __init__(self,IdEmpleado,Nombre,Direccion):
        self.IdEmpleado = IdEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion

    
    def Guardar(P_Id,P_Nombre,P_Direccion):
        empleado = Empleado(P_Id,P_Nombre,P_Direccion)
        
        lstEmpleados = []
        lstEmpleados.append(P_Id)
        lstEmpleados.append(P_Nombre)
        lstEmpleados.append(P_Direccion)

        return lstEmpleados

    def Consultar_Todo(P_tplEmpleados):
        print("| Id_Empleado | Nombre | Direccion")
        for empleado in range(0,len(P_tplEmpleados)):
            print(f"| {P_tplEmpleados[empleado][0]} | {P_tplEmpleados[empleado][1]} | {P_tplEmpleados[empleado][2]} |")

    def Consultar_Por_Id(P_tplEmpleados,P_Id):
        print("| Id_Empleado | Nombre | Direccion")
        for empleado in range(0,len(P_tplEmpleados)):
            if P_tplEmpleados[empleado][0] == P_Id:
                print(f"| {P_tplEmpleados[empleado][0]} | {P_tplEmpleados[empleado][1]} | {P_tplEmpleados[empleado][2]} |")