import pandas as pd
from tkinter import *
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def abrirArchivo():
    rutaArchivo = fd.askopenfilename(
        initialdir="/", title="Selecione archivo", filetype=(("xlsx files", "*.xlsx*"), ("All files", "*.*")))
    mostrarRuta["text"] = rutaArchivo

    if not rutaArchivo:
        messagebox.showerror("Error", "No se selecciono un archivo UwU")
        return

    mostrarArchivosExcel(rutaArchivo)


def mostrarArchivosExcel(rutaArchivo):
    # Leer el archivo excel
    df = pd.read_excel(rutaArchivo)
    #obtener columnas de raaza y edad
    try:
        edad = df["edad"]
        raza = df["raza"]
    except ValueError:
        messagebox.showerror("Error', 'No se puede leer este tipo de archivo")
        return

    except FileNotFoundError:
        messagebox.showerror("Error', 'El archivo esta \n corrupto")
        return None

    try:
        #dibujamos la grafica
        edadFigure = plt.figure(figsize=(6, 7), dpi=70)
        graficaEdad = edadFigure.add_subplot(111)
        canvasEdad = FigureCanvasTkAgg(edadFigure, frameGrafica)
        canvasEdad.get_tk_widget().pack(side=tk.LEFT, fill=tk.NONE)
        edadData = edad.round(decimals=0).value_counts().sort_index()
        edadData.plot(kind='bar', legend=False, ax=graficaEdad, colormap="YlGn_r")
        graficaEdad.set_title("Edad de los perros")
        graficaEdad.set_xlabel("Edad")
        graficaEdad.set_ylabel("Frecuencia")

        razaFigure = plt.figure(figsize=(12, 10), dpi=70)
        graficaRaza = razaFigure.add_subplot(111)
        canvasRaza = FigureCanvasTkAgg(razaFigure, frameGrafica)
        canvasRaza.get_tk_widget().pack(side=tk.RIGHT, fill=tk.NONE)
        razaData = raza.value_counts().sort_index()
        razaData.plot(kind='bar', legend=False, ax=graficaRaza)
        graficaRaza.set_title("Raza de los perros")
        graficaRaza.set_ylabel("Raza")
        graficaRaza.set_xlabel("Frecuencia")
    except ValueError:

        messagebox.showerror("Error", "Revisa tu columna de datos")
        return



#creamos las configuraciones de la ventana
ventana = tk.Tk()
ventana.geometry("1050x1000")
ventana.minsize(width=800, height=500)
ventana.title("Grafica perritos")

ventana.columnconfigure(0, weight=25)
ventana.rowconfigure(0, weight=25)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
#creamos dos frames, uno para botones y otro para la grafica
frameGrafica = Frame(ventana, bg="gray")
frameGrafica.grid(column=0, row=0, sticky="nsew")
frameBotones = Frame(ventana, bg='gray26')
frameBotones.grid(column=0, row=1, sticky="nsew")

frameGrafica.columnconfigure(0, weight=1)
frameGrafica.rowconfigure(0, weight=1)

frameBotones.columnconfigure(0, weight=1)
frameBotones.rowconfigure(0, weight=1)
frameBotones.columnconfigure(1, weight=1)
frameBotones.rowconfigure(0, weight=1)

frameBotones.columnconfigure(2, weight=1)
frameBotones.rowconfigure(0, weight=1)

frameBotones.columnconfigure(3, weight=2)
frameBotones.rowconfigure(0, weight=1)


boton1 = Button(frameBotones, text="Abrir", bg="green2", command=abrirArchivo)
boton1.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)

#boton3 = Button(frameBotones, text= "Borrar Grafica", bg="yellow", command= limpiar)
#boton3.grid(column = 1, row = 0, sticky="nsew", padx=10, pady=10)

boton2 = Button(frameBotones, text="Salir", bg="red", command=ventana.destroy)
boton2.grid(column=2, row=0, sticky="nsew", padx=10, pady=10)

mostrarRuta = Label(frameBotones, fg="white", bg="gray26",
               text="Ubicación del archivo", font=("Arial", 10, "bold"))
mostrarRuta.grid(column=3, row=0)

try:
    ventana.mainloop()
except ValueError:
    messagebox.showerror("Error", "404 no se que paso we")
