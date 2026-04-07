import tkinter as tk
from tkinter import messagebox

def log_calculo(func):
    def wrapper(*args, **kargs):
        print("f --- [LOG]: Ejecutando proyección financiera")
        return func(*args, **kargs)
    return wrapper

def calcular_recursion(capital, tasa, años):
    #Caso base: si no quedan añosm, el capital es el actual
    if años == 0:
        return capital
    #llamada recursiva: calculamos el interés del año actual y pasamos al siguiente
    return calcular_recursion(capital * (1 + tasa), tasa, años - 1)

# -- Programa principal con interfaz gráfica

class AppInversion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inversión Pro v1.0  - @Mr. Mijito")
        self.root.geometry("400x300")
        self.root.configure(bg='#1e1e1e')

        #Función lambda
        self.formatear_tasa = lambda t: t / 100
        
        #Elementos a la interfaz
        # 1. Elemento capital de inversión
        tk.Label(root, text = "Capital Inicial ($):", bg="#1e1e1e", fg="white").pack(pady=5)
        self.ent_capital = tk.Entry(root)
        self.ent_capital.pack()
        # 2. Tasa de interes
        tk.Label(root, text = "tasa de interes (%):", bg="#1e1e1e", fg="white").pack(pady=5)
        self.ent_tasa = tk.Entry(root)
        self.ent_tasa.pack()
        # 3. Tiempo - cantidad de años de inversión
        tk.Label(root, text = "años de inversión:", bg="#1e1e1e", fg="white").pack(pady=5)
        self.ent_años = tk.Entry(root)
        self.ent_años.pack()

        self.btn_calcular = tk.Button(root, text="¡PROYECTAR AHORA!", command=self.ejecutar, bg = "#00b4d8", fg="black", font=("Arial", 12, "bold"))
        self.btn_calcular.pack(pady=20)

    @log_calculo # Aplicamos nuestro decorador
    def ejecutar(self):
        try:
            #obtenemos datos de la interfaz
            cap = float (self.ent_capital.get())
            #Usamos la lambda para procesar la  tasa
            tasa = self.formatear_tasa(float(self.ent_tasa.get()))
            años = int (self.ent_años.get())

            #llamar a la función recursiva
            resultado = calcular_recursion(cap, tasa, años)
            #Mostramos el resultado con formato de moneda limpio
            messagebox.showinfo("Proyección de lista", f"En {años} años, tendrás: \n${resultado:,.2f}" )
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos")

# --- INICIALIZACIÓN DEL PROGRAMA ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AppInversion(root)
    root.mainloop()



