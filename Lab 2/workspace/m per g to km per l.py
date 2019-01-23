mileage = 32
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934
fuel_consumption = 100 * (mileage * (LITRES_PER_GALLON ** -1) * KMS_PER_MILE) ** -1
print(fuel_consumption)
