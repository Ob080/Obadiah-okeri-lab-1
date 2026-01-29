while True:
    try:
        voltage = float(input("Enter voltage (V): "))
        resistance = float(input("Enter resistance (Ohms): "))

        if resistance != 0:
            current = voltage / resistance
            power = voltage * current
            print("Current (A):", current)
            print("Power (W):", power)
        else:
            print("Error: Resistance cannot be zero.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

    repeat = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break