import tkinter as tk
from tkinter import font
from tds_final import inicio

# Función que se ejecuta al presionar el botón
def procesar_lista():

    lista = entrada.get() 
    texto_resultado.config(text= inicio(lista) )


# Crear ventana
ventana = tk.Tk()
ventana.geometry("500x500")

# Tamaño de fuente
tamanio_fuente = 12

# Crear fuente
fuente = font.Font(size=tamanio_fuente)

entrada = tk.StringVar()


# Etiqueta de mensaje
mensaje_label = tk.Label(ventana, text="Ingrese una lista de cadenas:", font=fuente)
mensaje_label.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada
campo_texto = tk.Entry(ventana, textvariable=entrada, font=fuente)
campo_texto.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Botón
boton = tk.Button(ventana, text="Procesar lista", command=procesar_lista, font=fuente)
boton.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Cuadro de texto para el resultado
texto_resultado = tk.Label(ventana, text="", font=fuente)
texto_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
texto_resultado.configure(anchor="center")

# Configurar el ancho proporcional del campo de entrada
ventana.grid_columnconfigure(0, weight=8)
ventana.grid_columnconfigure(1, weight=2)

# Iniciar la ventana
ventana.mainloop()

