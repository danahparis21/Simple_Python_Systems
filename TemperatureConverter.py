def main():
    while True: 
        try: 
            temperature = float(input("\nEnter the temperature value: "))
            convertFrom = int(input("Enter the unit to convert from (1. Celsius | 2. Fahrenheit | 3. Kelvin): "))
            convertTo = int(input("Enter the unit to convert to (1. Celsius | 2. Fahrenheit | 3. Kelvin): "))

            if convertTo in [1,2,3] and convertFrom in [1,2,3]: 
                if convertFrom is convertTo:
                    print("Units are the same; No conversion needed")

                #if original temperature is Celsius
                elif convertFrom == 1: 
                    if convertTo == 2:
                        CelsiusToFahrenheit(temperature)
                    elif convertTo == 3:
                        CelsiusToKelvin(temperature)

                #if original temperature is Fahrenheit
                elif convertFrom == 2: 
                    if convertTo == 1:
                        FahrenheitToCelsius(temperature)
                    elif convertTo == 3:
                        FahrenheitToKelvin(temperature)
                    
                #if original temperature is Kelvin
                elif convertFrom == 3:
                    if convertTo == 1:
                        KelvinToCelsius(temperature)
                    elif convertTo == 2:
                        KelvinToFahrenheit(temperature)
                
            else: 
                print("Invalid Unit Conversion.")


        except ValueError:
            print("Invalid input. Please choose a number only")

        #prompt to exit the loop
        try: 
            choose = input("Would you like to convert another temperature? (yes/no): ")
            if choose.lower() == 'yes':
                continue;
            else:
                print("END PROGRAM")
                break
            
        except ValueError:
            print("Invalid input, yes or no only")

#Celsius Conversion functions
def CelsiusToFahrenheit(temperature):
    convertedTemp = temperature * (9/5) + 32
    print(f"{temperature} Celsius is {convertedTemp} Fahrenheit.")

def CelsiusToKelvin(temperature):
    convertedTemp = temperature + 273.15
    print(f"{temperature} Celsius is {convertedTemp} Kelvin.")


#Fahrenheit Conversion functions
def FahrenheitToCelsius(temperature):
    convertedTemp = (temperature - 32) * (5/9)
    print(f"{temperature} Fahrenheit is {convertedTemp} Celsius.")

def FahrenheitToKelvin(temperature):
    convertedTemp = (temperature - 32) * (5/9) + 273.15
    print(f"{temperature} Fahrenheit is {convertedTemp} Celsius.")


#Kelvin Conversion functions
def KelvinToCelsius(temperature):
    convertedTemp = temperature - 273.15
    print(f"{temperature} Kelvin is {convertedTemp} Celsius.")

def KelvinToFahrenheit(temperature):
    convertedTemp = (temperature - 273.15) * (9/5) + 32
    print(f"{temperature} Kelvin is {convertedTemp} Fahrenheit.")





main()