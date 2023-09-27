# I am creating a code that will print important information about the car.

# I am going to use the fuction in python to print 

# Here is the function. I used keywords and positional only that can be used with python 
def create_car(model, year, plate, color, /, *, brand, motor, fuel):
    print(model, year, plate, color, brand, motor, fuel)


# here is my car that will print
create_car("Revuelto", 2023, "BBH-8973", "Orange", brand="Lamborghini", motor="V12", fuel="Hybrid")

create_car("Onix", 2022, "MJO-0924", "Black", brand="Chevrolet", motor="1.4", fuel="Gasoline")