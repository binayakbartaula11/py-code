# Function to convert units of length
def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1.0,
        'kilometers': 0.001,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        return "Invalid length unit"

# Function to convert units of weight
def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1.0,
        'grams': 1000.0,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])
    else:
        return "Invalid weight unit"

# Function to convert units of temperature
def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid temperature unit"

# Main function to use the converters
def unit_converter():
    print("Unit Converter")
    print("Choose the type of conversion:")
    print("1. Length\n2. Weight\n3. Temperature")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit (meters, kilometers, centimeters, etc.): ").lower()
        to_unit = input("Enter the to unit (meters, kilometers, centimeters, etc.): ").lower()
        result = length_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
        
    elif choice == '2':
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the from unit (kilograms, grams, pounds, etc.): ").lower()
        to_unit = input("Enter the to unit (kilograms, grams, pounds, etc.): ").lower()
        result = weight_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
        
    elif choice == '3':
        value = float(input("Enter the temperature to convert: "))
        from_unit = input("Enter the from unit (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("Enter the to unit (celsius, fahrenheit, kelvin): ").lower()
        result = temperature_converter(value, from_unit, to_unit)
        print(f"{value}° {from_unit} is equal to {result}° {to_unit}")
        
    else:
        print("Invalid choice")

if __name__ == "__main__":
    unit_converter()
