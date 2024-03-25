cars = ["Ford", "Volvo", "BMW", "Ferrari","Fusca"]

item = cars.pop(0)

while item != "BMW":
    print('Item não encontrado!')
    item = cars.pop(0)

print('Item encontrado com sucesso!')