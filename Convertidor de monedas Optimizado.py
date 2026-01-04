import tkinter as tk
from tkinter import ttk, messagebox

#clase para la conversión de monedas
class currencyConverter:
    #lógica para la conversión de moneda

    def __init__(self):
        #Diccionario que incluirá los tipos de moneda usando como base la modeda USD
        self.exchange_rate = {
            "USD": 1.0,  #Dolar americano
            "COP": 3767, #Peso colombiano
            "EUR": 0.92, #Euro
            "CNY": 7.25  #Yuan Chino
        }

# Metodo de las monedas disponibles
def get_currencies(self):

    #retornar las claves del diccionario 
    return list(self.exchange_rates_keys())

# Metodo que realiza la conversión entre monedas

    def convert(self, amount:float, from_currency: str, to_currency: str) -> float:
        #convertimos el monto original a dolares
        amount_in_usd = amount / self.exchange_rates[from_currency]

        # Convertimos de dólares a la destino y retornamos el resultado
        return amount_in_usd * self.exchange_rates[to_currency]
    
    # Clase encargada únicamente 

    class CurrencyConverterGUI:
        "***Interfaz gráfica del conversor***"
    
    #contructor de la interfaz gráfica
    def __ini__(self,root):
        self.root = root

        self.root.title("Conversor de monedas")

        self.root.resizable(false,false)

    #creación de una instancia, debemos separar y realizar la lógica de la interfaz
    self.converter = currencyConverter()

    #llamado de metodo para crear los widgets
    self.create_widget()

    


