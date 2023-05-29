from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image

from PIL import ImageTk, Image

def Fun_Ventana_Inicio():
    global ventana_inicio
    ventana_inicio = Tk()
    w = 670
    h = 500
    ws = ventana_inicio.winfo_screenwidth()
    hs = ventana_inicio.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_inicio.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ventana_inicio.resizable(1,1)
    ventana_inicio.title("INSUMO DE UÑAS")
   
    btn_iniciar = Button(ventana_inicio, text="Iniciar Sesión", fg="#fff", bg="#00008c", width=35, height=2, command=ir_login)
    btn_iniciar.pack(pady=35)
    
    imagen = ImageTk.PhotoImage(Image.open("SGIU.png"))
    label_imagen = Label(ventana_inicio, image=imagen, width=500, height=400)

    label_imagen.pack()
    

    ventana_inicio.mainloop()


def Fun_Ventana_Login():
    global ventana_login
    #* -------
    ventana_login = Tk()
    w = 370
    h = 330
    ws = ventana_login.winfo_screenwidth()
    hs = ventana_login.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_login.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ventana_login.resizable(0,0)
    #* -------

    ventana_login.title("Ingresar al Sistema")


    def Login():
        if usuario.get() == "":
            messagebox.showinfo("Falta Dato", "Falta Ingresar el USUARIO")
            entry_usuario.focus()
            return
        if contra.get() == "":
            messagebox.showinfo("Falta Dato", "Falta ingresar la CONTRASEÑA")
            entry_contra.focus()
            return




    frame_formulario = Frame(ventana_login)
    frame_formulario.pack()

    lbl_usuario = Label(frame_formulario, text="Usuario")
    lbl_usuario.config(pady=10, padx=10)
    lbl_usuario.grid(row=0 , column=0)

    lbl_contra = Label(frame_formulario, text="Contraseña")
    lbl_contra.config(pady=10, padx=10)
    lbl_contra.grid(row=1, column=0)

    usuario = StringVar()
    entry_usuario = ttk.Entry(frame_formulario, textvariable=usuario)
    entry_usuario.grid(row=0 , column=1, pady=10, padx=10)

    contra = StringVar()
    entry_contra = ttk.Entry(frame_formulario, textvariable=contra, show="*")
    entry_contra.grid(row=1, column=1, pady=10, padx=10)

    frame_botones = Frame(ventana_login)
    frame_botones.pack()

    btn_entrar = Button(frame_botones, text="Entrar", fg="#fff", bg="green", command=Login)
    btn_entrar.config(width=15)
    btn_entrar.grid(row=0, column=0, padx=20, pady=15)

    btn_salir = Button(frame_botones, text="Volver", fg="#fff", bg="#00008c", command=ir_inicio)
    btn_salir.config(width=15)
    btn_salir.grid(row=0, column=1, padx=20, pady=15)

    ventana_login.mainloop()

def Fun_Ventana_Contenido():
    global ventana_contenido
    #* -------
    ventana_contenido = Tk()
    w = 550
    h = 300
    ws = ventana_contenido.winfo_screenwidth()
    hs = ventana_contenido.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    ventana_contenido.geometry('%dx%d+%d+%d' % (w, h, x, y))
    ventana_contenido.resizable(0,0)
    #* -------

    ventana_contenido.title("Gestíon Librería")
    ventana_contenido.iconbitmap("img/logoProA.ico")

    def Limpiar_Datos():
        apellido.set("")
        nombre.set("")
        dni.set("")
        opcion.set(0)
        cmbx_genero.set("Seleccionar: ")
        precio.set("")
        dias.set("")
        total.set("")

        messagebox.showinfo("Contenido", "Se resetearon los datos correctamente!")

    def Calcular():
        if apellido.get() == "":
            messagebox.showinfo("Falta Dato", "Ingrese APELLIDO")
            entry_apellido.focus()
            return
        apellido_dato = apellido.get()
        if apellido_dato.isdigit() == True:
            messagebox.showerror("Error", "Datos incorrectos")
            apellido.set("")
            entry_apellido.focus()
            return

        if nombre.get() == "":
            messagebox.showinfo("Falta Dato", "Ingrese NOMBRE")
            entry_nombre.focus()
            return
        nombre_dato = nombre.get()
        if nombre_dato.isdigit() == True:
            messagebox.showerror("Error", "Datos incorrectos")
            nombre.set("")
            entry_nombre.focus()
            return

        if dni.get() == "":
            messagebox.showinfo("Falta Dato", "Ingrese DNI")
            entry_dni.focus()
            return
        for caracter in dni.get():
            if caracter != "." and caracter.isdigit() == False:
                messagebox.showerror("Error", "Datos incorrectos")
                dni.set("")
                entry_dni.focus()
                return

        if opcion.get() == 0:
            messagebox.showinfo("Falta Dato", "Seleccione si sos socio")
            return

        if cmbx_genero.get() == "Seleccionar: ":
            messagebox.showinfo("Falta Dato", "Ingrese GENERO")
            return
        
        if precio.get() == "":
            messagebox.showinfo("Falta Dato", "Ingrese PRECIO")
            entry_precio.focus()
            return
        for caracter in precio.get():
            if caracter != "." and caracter.isdigit() == False:
                messagebox.showerror("Error", "Datos incorrectos")
                precio.set("")
                entry_precio.focus()
                return

        if dias.get() == "":
            messagebox.showinfo("Falta Dato", "Ingrese DIAS")
            entry_dias.focus()
            return
        dia = dias.get()
        if dia.isdigit() == False:
            messagebox.showerror("Error", "Datos incorrectos")
            dias.set("")
            entry_dias.focus()
            return

        monto = int(precio.get()) * int(dias.get())

        if opcion.get() == 1:
            if cmbx_genero.get() == "Drama":
                monto = monto * 0.92
                return total.set(monto)
            elif cmbx_genero.get() == "Comedia":
                monto = monto * 0.88
                return total.set(monto)
            else:
                monto = monto * 0.83
                return total.set(monto)
        else:
            return total.set(monto)
        

    frame_datos_personales = LabelFrame(ventana_contenido, text="Datos Personales")
    frame_datos_personales.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10)

    frame_datos_servicio = LabelFrame(ventana_contenido, text="Datos del servicio")
    frame_datos_servicio.grid(row=0 , column=1, padx=5, pady=5, ipadx=10, ipady=10)

    frame_pago = LabelFrame(ventana_contenido)
    frame_pago.grid(row=1, column=0 ,columnspan=2, padx=5, pady=5)

    frame_botones = Frame(ventana_contenido)
    frame_botones.grid(row=2, column=0)

    # Datos Personales
    lbl_apellido = Label(frame_datos_personales, text="Apellido")
    lbl_apellido.grid(row=0 ,column=0, pady=3, padx=10)

    apellido = StringVar()
    entry_apellido = Entry(frame_datos_personales, textvariable=apellido)
    entry_apellido.grid(row=0, column=1, pady=3, padx=5)

    lbl_nombre = Label(frame_datos_personales, text="Nombre")
    lbl_nombre.grid(row=1, column=0, pady=3, padx=10)

    nombre = StringVar()
    entry_nombre = Entry(frame_datos_personales, textvariable=nombre)
    entry_nombre.grid(row=1, column=1, pady=3, padx=5)
    
    lbl_dni = Label(frame_datos_personales, text="DNI")
    lbl_dni.grid(row=2, column=0, pady=3, padx=10)

    dni = StringVar()
    entry_dni = Entry(frame_datos_personales, textvariable=dni)
    entry_dni.grid(row=2, column=1, pady=3, padx=5)

    lbl_socio = Label(frame_datos_personales, text="Socio")
    lbl_socio.grid(row=3, column=0)

    frame_opciones = Frame(frame_datos_personales)
    frame_opciones.grid(row=4, column=0)

    opcion = IntVar()
    opcion.set(0)
    rbtn_si = Radiobutton(frame_opciones, variable=opcion, value=1, text="Si")
    rbtn_si.grid(row=0, column=0)

    rbtn_no = Radiobutton(frame_opciones, variable=opcion, value=2, text="No")
    rbtn_no.grid(row=0, column=1)

    # Datos Del Servicio
    lbl_seleccion = Label(frame_datos_servicio, text="Seleccione Género")
    lbl_seleccion.grid(row=0, column=0)

    lista_genero = ["Drama", "Comedia", "Ficcion"]
    cmbx_genero = ttk.Combobox(frame_datos_servicio, values = lista_genero, state="readonly")
    cmbx_genero.set("Seleccionar: ")
    cmbx_genero.grid(row=1, column=0, columnspan=2, padx=5, pady=3)

    lbl_precio = Label(frame_datos_servicio, text="Precio $")
    lbl_precio.grid(row=2, column=0, pady=3)

    precio = StringVar()
    entry_precio = Entry(frame_datos_servicio, textvariable=precio)
    entry_precio.grid(row=2 , column=1, pady=3)

    lbl_dias = Label(frame_datos_servicio, text="Días")
    lbl_dias.grid(row=3, column=0, pady=3)

    dias = StringVar()
    entry_dias = Entry(frame_datos_servicio, textvariable=dias)
    entry_dias.grid(row = 3, column=1, pady=3)

    # Pago
    lbl_pago = Label(frame_pago, text="Pago")
    lbl_pago.grid(row=0, column=0, pady=5, padx=15)

    total = StringVar()
    entry_total = Entry(frame_pago, textvariable=total, state=DISABLED)
    entry_total.grid(row=0, column=1, pady=5)

    btn_calcular = Button(frame_pago, text="Calcular", bg="blue", fg="#fff", width=15, command=Calcular)
    btn_calcular.grid(row=0, column=2, padx=10, pady=5)

    btn_guardar = Button(frame_pago, text="Guardar", bg="blue", fg="#fff", width=15)
    btn_guardar.grid(row=0, column=3, padx=10, pady=5)

    # Botones
    btn_limpiar = Button(frame_botones, text="Limpiar", fg="#fff", bg="green", width=10, command=Limpiar_Datos)
    btn_limpiar.grid(row=0, column=0, pady=10, padx=15)

    btn_salir = Button(frame_botones, text="Salir", fg="#fff", bg="red", width=10, command=ventana_contenido.destroy)
    btn_salir.grid(row=0, column=1, pady=10, padx=15)

    ventana_contenido.mainloop()

def ir_login():
    ventana_inicio.destroy()
    Fun_Ventana_Login()

def ir_inicio():
    ventana_login.destroy()
    Fun_Ventana_Inicio()

def ir_contenido():
    ventana_login.destroy()
    Fun_Ventana_Contenido()

Fun_Ventana_Inicio()



