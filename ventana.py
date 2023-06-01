import tkinter as tk

def ejecutar_accion():
    texto_resultado.set("Resultado: " + campo_texto.get())

# Crear ventana
ventana = tk.Tk()
ventana.geometry("400x200")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Ingrese una lista de cadenas:")
etiqueta.grid(row=0, column=0, padx=5, pady=5)


# Campo de texto
campo_texto = tk.Entry(ventana)
campo_texto.grid(row=1, column=0, padx=5, pady=5)

# Crear botón
boton = tk.Button(ventana, text="Procesar", command=ejecutar_accion)
boton.grid(row=1, column=4, padx=5, pady=5)

# Crear etiqueta para mostrar el resultado
texto_resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=texto_resultado)
etiqueta_resultado.grid(row=2, column=0)


# Iniciar la ventana
ventana.mainloop()
