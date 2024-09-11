
import tkinter as tk
from tkinter import messagebox
from ventana import Ventana

class CotizadorVentanasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cotización de Ventanas")
        
        # Variables para los inputs
        self.ancho_var = tk.StringVar()
        self.alto_var = tk.StringVar()
        self.estilo_var = tk.StringVar()
        self.vidrio_var = tk.StringVar()
        self.esmerilado_var = tk.BooleanVar()

        # Elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Labels y entradas para los parámetros de la ventana
        tk.Label(self.root, text="Ancho (cm):").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.ancho_var).grid(row=0, column=1)

        tk.Label(self.root, text="Alto (cm):").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.alto_var).grid(row=1, column=1)

        tk.Label(self.root, text="Estilo (O, XO, OXXO):").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.estilo_var).grid(row=2, column=1)

        tk.Label(self.root, text="Tipo de Vidrio:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.vidrio_var).grid(row=3, column=1)

        tk.Checkbutton(self.root, text="Vidrio Esmerilado", variable=self.esmerilado_var).grid(row=4, columnspan=2)

        # Botón para calcular cotización
        tk.Button(self.root, text="Calcular Cotización", command=self.calcular_cotizacion).grid(row=5, columnspan=2)

        # Espacio para mostrar el resultado
        self.resultado_label = tk.Label(self.root, text="", fg="blue")
        self.resultado_label.grid(row=6, columnspan=2)

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

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CotizadorVentanasApp(root)
    root.mainloop()
