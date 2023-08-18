import itertools
print("------------------------------------------------------------------")
print("*Programa para combinar palabras y armar una wordlist by nahumode*")
print("------------------------------------------------------------------")


def get_valid_input():
    while True:
        user_input = input("Ingresa una palabra o número:")
        if user_input.isalpha() or user_input.isdigit():
            return user_input
        else:
            print("Error: Debes ingresar solo letras o números enteros.")

def main():
    try:
        num_inputs = int(input("¿Cuántas palabras/números deseas ingresar? (máximo 10): "))
        if num_inputs > 10:
            print("Error: No puedes ingresar más de 10 palabras/números.")
            return

        inputs = []
        for _ in range(num_inputs):
            input_value = get_valid_input()
            inputs.append(input_value)

        combinations = list(itertools.permutations(inputs))

        with open("wordlist.txt", "w") as file:
            for combo in combinations:
                file.write("".join(combo) + "\n")

        print("Congratulations, your wordlist has been created successfully!")

    except ValueError:
        print("Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    main()
