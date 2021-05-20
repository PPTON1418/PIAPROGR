class Curso:
    def __init__(self,IdCurso,Descripcion,IdEmpleado):
        self.IdCurso = IdCurso
        self.Descripcion = Descripcion
        self.IdEmpleado = IdEmpleado

    def Guardar(P_Id,P_Descripcion,P_IdEmpleado):
        curso = Curso(P_Id,P_Descripcion,P_IdEmpleado)

        lstCurso = []
        lstCurso.append(P_Id)
        lstCurso.append(P_Descripcion)
        lstCurso.append(P_IdEmpleado)

        return lstCurso

    def Consultar_Todo(P_tplCurso):
        print("| Id_Curso | Descripción | Id_Empleado 1")
        for curso in range(0,len(P_tplCurso)):
            print(f"| {P_tplCurso[curso][0]} | {P_tplCurso[curso][1]} | {P_tplCurso[curso][2]} |")

    def Consultar_Por_Id(P_tplCurso,P_Id):
        print("| Id_Curso | Descripción | Id_Empleado 1")
        for curso in range(0,len(P_tplCurso)):
            if P_tplCurso[curso][0] == P_Id:
                print(f"| {P_tplCurso[curso][0]} | {P_tplCurso[curso][1]} | {P_tplCurso[curso][2]} |")