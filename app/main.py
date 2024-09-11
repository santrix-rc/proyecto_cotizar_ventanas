import tkinter as tk
from tkinter import ttk, messagebox
from ventana import Ventana

class CotizadorVentanasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cotización de Ventanas")
        
        # Listas de opciones predefinidas
        self.ancho_opciones = [100, 120, 150, 200]
        self.alto_opciones = [100, 120, 150, 180]
        self.estilo_opciones = ['O', 'XO', 'OXXO', 'OXO']
        self.vidrio_opciones = ['Transparente', 'Bronce', 'Azul']

        # Variables de las entradas
        self.ancho_var = tk.StringVar(value=self.ancho_opciones[0])
        self.alto_var = tk.StringVar(value=self.alto_opciones[0])
        self.estilo_var = tk.StringVar(value=self.estilo_opciones[0])
        self.vidrio_var = tk.StringVar(value=self.vidrio_opciones[0])
        self.esmerilado_var = tk.BooleanVar()

        # Crear interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Ancho
        tk.Label(self.root, text="Ancho (cm):").grid(row=0, column=0)
        self.ancho_combobox = ttk.Combobox(self.root, textvariable=self.ancho_var, values=self.ancho_opciones)
        self.ancho_combobox.grid(row=0, column=1)
        tk.Button(self.root, text="Añadir Ancho", command=self.agregar_ancho).grid(row=0, column=2)

        # Alto
        tk.Label(self.root, text="Alto (cm):").grid(row=1, column=0)
        self.alto_combobox = ttk.Combobox(self.root, textvariable=self.alto_var, values=self.alto_opciones)
        self.alto_combobox.grid(row=1, column=1)
        tk.Button(self.root, text="Añadir Alto", command=self.agregar_alto).grid(row=1, column=2)

        # Estilo
        tk.Label(self.root, text="Estilo (O, XO, OXXO):").grid(row=2, column=0)
        self.estilo_combobox = ttk.Combobox(self.root, textvariable=self.estilo_var, values=self.estilo_opciones)
        self.estilo_combobox.grid(row=2, column=1)
        tk.Button(self.root, text="Añadir Estilo", command=self.agregar_estilo).grid(row=2, column=2)

        # Tipo de vidrio
        tk.Label(self.root, text="Tipo de Vidrio:").grid(row=3, column=0)
        self.vidrio_combobox = ttk.Combobox(self.root, textvariable=self.vidrio_var, values=self.vidrio_opciones)
        self.vidrio_combobox.grid(row=3, column=1)
        tk.Button(self.root, text="Añadir Vidrio", command=self.agregar_vidrio).grid(row=3, column=2)

        # Checkbox para vidrio esmerilado
        tk.Checkbutton(self.root, text="Vidrio Esmerilado", variable=self.esmerilado_var).grid(row=4, columnspan=2)

        # Botón para calcular cotización
        tk.Button(self.root, text="Calcular Cotización", command=self.calcular_cotizacion).grid(row=5, columnspan=3)

        # Espacio para mostrar el resultado
        self.resultado_label = tk.Label(self.root, text="", fg="blue")
        self.resultado_label.grid(row=6, columnspan=3)

        # Espacio para mostrar el dibujo de la ventana
        self.canvas = tk.Canvas(self.root, width=400, height=200, bg="white")
        self.canvas.grid(row=7, columnspan=3)

        # Botón para visualizar el diseño de la ventana
        tk.Button(self.root, text="Visualizar Diseño", command=self.visualizar_diseno).grid(row=8, columnspan=3)

    def agregar_ancho(self):
        nuevo_ancho = self.pedir_valor("Ancho")
        if nuevo_ancho and nuevo_ancho not in self.ancho_opciones:
            self.ancho_opciones.append(nuevo_ancho)
            self.ancho_combobox['values'] = self.ancho_opciones

    def agregar_alto(self):
        nuevo_alto = self.pedir_valor("Alto")
        if nuevo_alto and nuevo_alto not in self.alto_opciones:
            self.alto_opciones.append(nuevo_alto)
            self.alto_combobox['values'] = self.alto_opciones

    def agregar_estilo(self):
        nuevo_estilo = self.pedir_valor("Estilo")
        if nuevo_estilo and nuevo_estilo not in self.estilo_opciones:
            self.estilo_opciones.append(nuevo_estilo)
            self.estilo_combobox['values'] = self.estilo_opciones

    def agregar_vidrio(self):
        nuevo_vidrio = self.pedir_valor("Tipo de Vidrio")
        if nuevo_vidrio and nuevo_vidrio not in self.vidrio_opciones:
            self.vidrio_opciones.append(nuevo_vidrio)
            self.vidrio_combobox['values'] = self.vidrio_opciones

    def pedir_valor(self, tipo):
        nuevo_valor = tk.simpledialog.askstring("Añadir " + tipo, "Introduce nuevo " + tipo + ":")
        return nuevo_valor

    def calcular_cotizacion(self):
        try:
            # Obtener los valores de los inputs
            ancho = float(self.ancho_var.get())
            alto = float(self.alto_var.get())
            estilo = self.estilo_var.get()
            vidrio = self.vidrio_var.get()
            esmerilado = self.esmerilado_var.get()

            # Crear una instancia de Ventana
            ventana = Ventana(ancho, alto, estilo, vidrio, esmerilado)
            costo = ventana.calcular_costo()

            # Mostrar el resultado en la etiqueta
            self.resultado_label.config(text=f"Costo calculado: ${costo:.2f}")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para todos los campos.")
        except KeyError:
            messagebox.showerror("Error", "Tipo de vidrio o estilo no válido.")

    def visualizar_diseno(self):
        # Limpiar el canvas
        self.canvas.delete("all")
        
        ancho = float(self.ancho_var.get())
        alto = float(self.alto_var.get())
        estilo = self.estilo_var.get()
        
        # Dibujar diferentes estilos
        if estilo == "O":
            self.canvas.create_rectangle(50, 50, 50 + ancho, 50 + alto, outline="black", fill="lightblue")
        elif estilo == "XO":
            self.canvas.create_rectangle(50, 50, 50 + ancho // 2, 50 + alto, outline="black", fill="lightblue")
            self.canvas.create_rectangle(50 + ancho // 2, 50, 50 + ancho, 50 + alto, outline="black", fill="white")
        elif estilo == "OXXO":
            self.canvas.create_rectangle(50, 50, 50 + ancho // 4, 50 + alto, outline="black", fill="lightblue")
            self.canvas.create_rectangle(50 + ancho // 4, 50, 50 + 3 * ancho // 4, 50 + alto, outline="black", fill="white")
            self.canvas.create_rectangle(50 + 3 * ancho // 4, 50, 50 + ancho, 50 + alto, outline="black", fill="lightblue")
        elif estilo == "OXO":
            self.canvas.create_rectangle(50, 50, 50 + ancho // 3, 50 + alto, outline="black", fill="lightblue")
            self.canvas.create_rectangle(50 + ancho // 3, 50, 50 + 2 * ancho // 3, 50 + alto, outline="black", fill="white")
            self.canvas.create_rectangle(50 + 2 * ancho // 3, 50, 50 + ancho, 50 + alto, outline="black", fill="lightblue")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CotizadorVentanasApp(root)
    root.mainloop()
