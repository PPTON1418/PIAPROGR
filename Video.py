class Video:
    def __init__(self,IdVideo,Nombre,Url,FechaPublicacion):
        self.IdVideo = IdVideo
        self.Nombre = Nombre
        self.Url = Url
        self.FechaPublicacion = FechaPublicacion

    def Guardar(P_Id,P_Nombre,P_Url,P_FechaPublicacion):
        video = Video(P_Id,P_Nombre,P_Url,P_FechaPublicacion)

        lstVideo = []
        lstVideo.append(video.IdVideo)
        lstVideo.append(video.Nombre)
        lstVideo.append(video.Url)
        lstVideo.append(video.FechaPublicacion)

        return lstVideo

    def Consultar_Todo(P_tplCurso):
        print("| Id_Curso | Descripción | Id_Empleado")
        for curso in range(0,len(P_tplCurso)):
            print(f"| {P_tplCurso[curso][0]} | {P_tplCurso[curso][1]} | {P_tplCurso[curso][2]} |")

    def Consultar_Por_Id(P_tplCurso,P_Id):
        print("| Id_Curso | Descripción | Id_Empleado")
        for curso in range(0,len(P_tplCurso)):
            if P_tplCurso[curso][0] == P_Id:
                print(f"| {P_tplCurso[curso][0]} | {P_tplCurso[curso][1]} | {P_tplCurso[curso][2]} |")