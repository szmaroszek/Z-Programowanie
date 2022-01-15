from models.dieta import Dieta
from models.pacjent import Pacjent
from models.dietetyk import Dietetyk
from models.zamowienie import Zamowienie


pacjent = Pacjent("Szymon", "Maroszek", 23, "male", 75, 180)

dietetyk = Dietetyk("Mariusz", "Pudzianowski", 69, "male", "Master's Degree", "Sport diet")

diet1 = Dieta('diet1', 'fasting', 1100, 500.123123)
diet2 = Dieta('diet2', 'fasting', 1200, 500.123)
diet3 = Dieta('diet3', 'fasting', 1300, 5100.123123)

order = Zamowienie()

order._diet_list = [diet1, diet2, diet3]
order._dietetyk = dietetyk
order._pacjent = pacjent
order._placowka = "Sosnowiec"

print(order)

print("Suma kalorii: " + str(order.get_kcal()) + "kcal.")

print("Łączny koszt: " + str(order.get_value()) + "PLN.")
