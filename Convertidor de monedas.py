# CONVERSOR DE MONEDAS 

# Diccionario con tasas base respecto al USD
# Esto significa: 1 USD equivale a X moneda
exchange_rates = {
    "USD": 1.0,        # Dólar base
    "COP": 4000.0,     # Peso colombiano aproximado
    "EUR": 0.92,       # Euro aproximado
    "CNY": 7.25        # Yuan chino aproximado
}

# Mostramos bienvenida al usuario
print("=== CONVERSOR DE MONEDAS ===")

# Mostramos las monedas disponibles
print("Monedas disponibles:")
for currency in exchange_rates:
    print("-", currency)

# Pedimos al usuario la moneda de origen
from_currency = input("Moneda origen: ").upper()

# Pedimos la moneda destino
to_currency = input("Moneda destino: ").upper()

# Pedimos el monto a convertir
amount = float(input("Monto a convertir: "))

# Convertimos primero el monto a USD
amount_in_usd = amount / exchange_rates[from_currency]

# Luego convertimos de USD a la moneda destino
converted_amount = amount_in_usd * exchange_rates[to_currency]

# Mostramos el resultado
print(f"\nResultado: {amount} {from_currency} = {converted_amount:.2f} {to_currency}") 



