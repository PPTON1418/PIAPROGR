import os
import Tema
import Video
import Empleado
import Curso

lstTemas = []
lstVideos = []
lstEmpleados = []
lstCursos = []

while True:
    print("1.- TEMAS")
    print("2.- VIDEOS")
    print("3.- CURSOS")
    print("4.- EMPLEADOS")
    print("5.- SALIR")
    Op = input("Seleccione una opcion: ")

    if Op != "1" and Op != "2" and Op != "3" and Op != "4" and Op != "5":
        print("Seleccione un valor valido dentro del menu")
    elif Op == "5":
        print("Abandonando sistema...")
        #Guardar datos
        # print(lstTemas)
        # print(lstCursos)
        # print(lstVideos)
        ruta_archivo=os.path.abspath(os.getcwd())
        archivo_Empleado=ruta_archivo+"\\Empleado.txt"
        archivo_Video=ruta_archivo+"\\Video.txt"
        archivo_Curso=ruta_archivo+"\\Curso.txt"
        archivo_Tema=ruta_archivo+"\\Tema.txt"
        
        e = open(archivo_Empleado,"w+")
        e.write("Id Empleado | Nombre | Direccion\n")
        for empleado in range(0,len(lstEmpleados)):
            e.write(f"{lstEmpleados[empleado][0]} | {lstEmpleados[empleado][1]} | {lstEmpleados[empleado][2]} |")
        e.close()

        v = open(archivo_Video,"w+")
        v.write("IdVideo | Nombre | Url |FechaPublicacion\n")
        for video in range(0,len(lstVideos)):
            v.write(f"{lstVideos[video][0]} | {lstVideos[video][1]} | {lstVideos[video][2]} | {lstVideos[video][3]}")
        v.close()
        
        t = open(archivo_Video,"w+")
        t.write("IdTema | Nombre\n")
        for tema in range(0,len(lstTemas)):
            t.write(f"{lstTemas[tema][0]} | {lstTemas[tema][1]}")
        t.close()

        c = open(archivo_Video,"w+")
        c.write("IdTema | Nombre\n")
        for curso in range(0,len(lstCursos)):
            c.write(f"{lstCursos[curso][0]} | {lstCursos[curso][1]}")
        c.close()
        
        break

    elif Op == "1":
        while True:
            print("MENU DE TEMAS")
            print("1.- AGREGAR TEMAS")
            print("2.- LISTAR TEMAS")
            print("3.- BUSCAR UN TEMA")
            print("4.- VOLVER")
            Accion = input("SELECCIONE UNA ACCIÓN: ")
            if Accion != "1" and Accion != "2" and Accion != "3" and Accion != "4":
                print("Seleccione un valor valido dentro del menu")
            elif Accion == "4":
                break
            elif Accion == "1":
                ID = input("Ingrese ID del TEMA: ")
                Nombre = input("Ingrese Nombre del TEMA: ")

                lstTemas.append(Tema.Tema.Guardar(ID,Nombre))

            elif Accion == "2":
                Tema.Tema.Consultar_Todo(lstTemas)

            elif Accion == "3":
                ID = input("Ingresa el ID del Tema que deseas buscar: ")
                Tema.Tema.Consultar_Por_Id(lstTemas,ID)

    elif Op == "2":
        while True:
            print("MENU DE VIDEOS")
            print("1.- AGREGAR VIDEOS")
            print("2.- LISTAR VIDEOS")
            print("3.- BUSCAR UN VIDEOS")
            print("4.- VOLVER")
            Accion = input("SELECCIONE UNA ACCIÓN: ")
            if Accion != "1" and Accion != "2" and Accion != "3" and Accion != "4":
                print("Seleccione un valor valido dentro del menu")
            elif Accion == "4":
                break
            elif Accion == "1":
                ID = input("Ingrese ID del VIDEOS: ")
                Nombre = input("Ingrese Nombre del VIDEO: ")
                Url = input("Ingrese Url del VIDEO: ")
                Fecha = input("Ingrese Fecha de Publicación del VIDEO: ")
                
                lstVideos.append(Video.Video.Guardar(ID,Nombre,Url,Fecha))

            elif Accion == "2":
                Video.Video.Consultar_Todo(lstVideos)

            elif Accion == "3":
                ID = input("Ingresa el ID del Tema que deseas buscar: ")
                Video.Video.Consultar_Por_Id(lstVideos,ID)

    elif Op == "3":
        while True:
            print("MENU DE CURSOS")
            print("1.- AGREGAR CURSOS")
            print("2.- LISTAR CURSOS")
            print("3.- BUSCAR UN CURSOS")
            print("4.- VOLVER")
            Accion = input("SELECCIONE UNA ACCIÓN: ")
            if Accion != "1" and Accion != "2" and Accion != "3" and Accion != "4":
                print("Seleccione un valor valido dentro del menu")
            elif Accion == "4":
                break
            elif Accion == "1":
                ID = input("Ingrese ID del CURSOS: ")
                Descripcion = input("Ingrese Descripcion del CURSOS: ")
                ID_Empleado = input("Ingrese ID del EMPLEADO del que depende el curso: ")
                if Curso.Curso.Consultar_Por_Id(lstCursos,ID_Empleado) != None:
                    lstCursos.append(Curso.Curso.Guardar(ID,Descripcion,ID_Empleado))
                else:
                    print("El Empleado no existe dentro de los registros")

            elif Accion == "2":
                Curso.Curso.Consultar_Todo(lstCursos)

            elif Accion == "3":
                ID = input("Ingresa el ID del Tema que deseas buscar: ")
                Curso.Curso.Consultar_Por_Id(lstCursos,ID)

    elif Op == "4":
        while True:
            print("MENU DE EMPLEADOS")
            print("1.- AGREGAR EMPLEADOS")
            print("2.- LISTAR EMPLEADOS")
            print("3.- BUSCAR UN EMPLEADO")
            print("4.- VOLVER")
            Accion = input("SELECCIONE UNA ACCIÓN: ")
            if Accion != "1" and Accion != "2" and Accion != "3" and Accion != "4":
                print("Seleccione un valor valido dentro del menu")
            elif Accion == "4":
                break
            elif Accion == "1":
                ID = input("Ingrese ID del Empleado: ")
                Nombre = input("Ingrese Nombre del Empleado: ")
                Direccion = input("Ingrese Dirección del Empleado:")

                lstEmpleados.append(Empleado.Empleado.Guardar(ID,Nombre,Direccion))

            elif Accion == "2":
                Empleado.Empleado.Consultar_Todo(lstEmpleados)

            elif Accion == "3":
                ID = input("Ingresa el ID del empleado que deseas buscar: ")
                Empleado.Empleado.Consultar_Por_Id(lstEmpleados,ID)