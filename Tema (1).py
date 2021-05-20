class Tema:
    def __init__(self,IdTema,Nombre):
        self.IdTema = IdTema
        self.Nombre = Nombre

    def Guardar(P_Id,P_Nombre):
        tema = Tema(P_Id,P_Nombre)

        lstTema = []
        lstTema.append(P_Id)
        lstTema.append(P_Nombre)

        return lstTema

    def Consultar_Todo(P_tplTema):
        print("| Id_Tema | Nombre |")
        for tema in range(0,len(P_tplTema)):
            print(f"| {P_tplTema[tema][0]} | {P_tplTema[tema][1]} |")

    def Consultar_Por_Id(P_tplTema,P_Id):
        print("| Id_Tema | Nombre |")
        for tema in range(0,len(P_tplTema)):
            if P_tplTema[tema][0] == P_Id:
                print(f"| {P_tplTema[tema][0]} | {P_tplTema[tema][1]} |")