import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas (API Live)")
        self.root.geometry("380x330")
        self.root.resizable(False, False)

        self.rates = {}
        self.fetch_rates()  # Trae tasas al iniciar

        self.create_ui()

    def fetch_rates(self):
        """Obtiene tasas de la API (base USD)."""
        try:
            url = "https://cdn.moneyconvert.net/api/latest.json"
            response = requests.get(url, timeout=10)
            data = response.json()
            self.rates = data.get("rates", {})
        except Exception as e:
            messagebox.showerror("Error API", f"No se pudo obtener tasas: {e}")

    def create_ui(self):
        tk.Label(self.root, text="Conversor de Monedas (Live)", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.root, text="Monto:").pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        tk.Label(self.root, text="Moneda origen:").pack()
        self.from_currency = ttk.Combobox(self.root, values=list(self.rates.keys()), state="readonly")
        self.from_currency.pack(pady=5)

        tk.Label(self.root, text="Moneda destino:").pack()
        self.to_currency = ttk.Combobox(self.root, values=list(self.rates.keys()), state="readonly")
        self.to_currency.pack(pady=5)

        tk.Button(self.root, text="Convertir", command=self.convert, bg="#4CAF50", fg="white").pack(pady=15)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Monto inválido")

            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            # Convertir: amount -> USD -> destino
            usd_value = amount / self.rates[from_curr]
            converted = usd_value * self.rates[to_curr]

            self.result_label.config(text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}")

        except ValueError:
            messagebox.showerror("Error de datos", "Ingresa un monto válido.")
        except KeyError:
            messagebox.showerror("Error de monedas", "Selecciona monedas válidas.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()



    


        



    