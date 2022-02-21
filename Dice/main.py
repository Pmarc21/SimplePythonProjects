# dice.py
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string): #Definimos la función parse_input.
    #Validamos que el input es un integer entre 1 y 6.
    # Si es así, devolvemos un integer con el mismo valor. Si no devolvemos frase de error.
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}: #comprobamos que está dentro de 1 a 6 y strip elimina espacios indeseados.
        return int(input_string) #Convierte el input en int y lo devolvemos
    else:
        print("Please enter a number from 1 to 6.") #Algo ha ido mal y lo devolvemos por pantalla
        raise SystemExit(1) #Salimos de la app debido al error

def roll_dice(num_dice):
    #Devuelve una lista de integers con longitud 'num_dice'.
    #Cada integer en la lista que se devuelve es un número random entre 1 y 6.
    roll_results=[]
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def generate_dice_faces_diagram(dice_values):
    """#Devuelve un diagrama ASCII de las diferentes caras de los dados
    # Si el string es dice_values = [4,1,3,2] devolverá:
    #  ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    #Genera una lista de caras con DICE_ART
    dice_faces = [] #Crea una lista vacía llamada dice_faces para guardar las correspondientes caras
    for value in dice_values: #Definimos loop para iterar sobre el valor de las caras de los dados
        dice_faces.append(DICE_ART[value]) #Recuperamos el valor del dado y lo añadimos a dice_faces

    #Genera una lista que contenga una fila de caras del dado
    dice_face_rows = [] #Generamos una lista vacía para meter los diagramas de los dados
    for row_idx in range(DIE_HEIGHT): #Definimos un loop que itera entre 0 y la última cara
        row_components = [] #Definimos una lista vacía de para guardar las porciones de las caras de los dados
        for die in dice_faces: #Definimos loop para iterar sobre las caras de los dados
            row_components.append(die[row_idx]) #Guardamos el componente de cada fila
        row_string = DIE_FACE_SEPARATOR.join(row_components) #Incluímos un separador entre las diferentes caras
        dice_face_rows.append(row_string)#Le ponemos cada row_string a la lista que mostrará el diagrama final

    #Genera cabecera con la palabara RESULTADO centrada
    width = len(dice_face_rows[0])
    diagram_header = " RESULTADOS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_face_rows)
    return dice_faces_diagram



# App's main code block

# 1. Get and validate user's input
num_dice_input = input("How many dice do you want to roll? [1-6]") #Mostramos esto por pantalla
num_dice = parse_input(num_dice_input) #Guardamos la variable introducida en num_dice

#2. Roll the dice
roll_results = roll_dice(num_dice)

#3. Generate the ASCII diagram of dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)

#4. Diplay de diagram
print(f"\n{dice_face_diagram}")
exit(0)

