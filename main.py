# Calculator times
# Divisions--
#     Basic-- Addition, Substraction, Multiplication, Division
#     Normalised - Exponent, Square, Square-root, Cube, Cube-root
#     advanced - Factorial, Modulas

# Core-Calculation
import sys
# Total takin input
int_count = int(input("Enter the number of input u have:- "))
draft = input("Enter the number seperated by ',':- ")
int_value = draft.split(",")

# key element
empty = []
# Basic 
def addition():
    sum = 0
    while(int_value != empty):
        storage = int_value.pop()
        sum = sum + int(storage)
    print(sum)
def substraction():
    sub = int(int_value.pop(0))
    while(int_value != empty):
        storage = int_value.pop()
        sub = sub - int(storage)
    print(sub)
def multiplication():
    mul = 1
    while(int_value != empty):
        storage = int_value.pop()
        mul = mul * int(storage)
    print(mul)
def division():
    div = int(int_value.pop(0))
    while(int_value != empty):
        storage = int_value.pop()
        div = int(div / int(storage))
    print(div)

# normalised
def Exponent():
    expo = int(int_value.pop(0))
    while(int_value != empty):
        storage = int_value.pop(0)
        expo = expo ** int(storage)
    print(expo)
def square():
    storage = []
    while(int_value != empty):
        sqr = int(int_value.pop(0))
        sqr_result = int(sqr ** 2)
        storage.append(sqr_result)
    print(storage)
def square_root():
    storage = []
    while(int_value != empty):
        sqrt = int(int_value.pop(0))
        sqrt_result = int(sqrt ** 0.5)
        storage.append(sqrt_result)
    print(storage)
def cube():
    storage = []
    while(int_value != empty):
        cube = int(int_value.pop(0))
        cube_result = int(cube ** 3)
        storage.append(cube_result)
    print(storage)
def cube_root():
    storage = []
    while(int_value != empty):
        cubert = int(int_value.pop(0))
        cubert_result = round(cubert ** (1/3))
        storage.append(cubert_result)
    print(storage)
def factorial():
    storage = []
    while int_value != empty:
        n = int(int_value.pop(0))
        if n == 0:
            storage.append(1)
        else:
            d = n
            while d != 1:
                d = d - 1
                n = n * d 
            storage.append(n)
    print(storage)
def modulus():
    mod = int(int_value.pop(0))
    while(int_value != empty):
        storage = int_value.pop(0)
        mod = mod % int(storage)
    print(mod)

# Gui and Logic
# --- Your Exact Prompt Flow Kept Exactly Safe ---
if(int_count == len(int_value)):
    # Beautiful Custom Terminal Canvas
    print("\n" + "═"*60)
    print(" 🚀  BATCH PROCESSING CALCULATOR v1.0  🚀 ".center(60, "═"))
    print("═"*60)
    print("  [ CORE ENVIRONMENT DETECTED ]".center(60))
    print(f"  Inputs Loaded Successfully: {draft}\n")
    
    print(" ┌────────────────────────────────────────────────────────┐ ")
    print(" │  🔢 BASIC UTILITIES     │  ⚡ NORMALISED ENGINE       │ ")
    print(" ├─────────────────────────┼──────────────────────────────┤ ")
    print(" │  [1]  Addition          │  [5]  Exponent (xʸ)          │ ")
    print(" │  [2]  Substraction      │  [6]  Square (x²)            │ ")
    print(" │  [3]  Multiplication    │  [7]  Square-Root (√)        │ ")
    print(" │  [4]  Division          │  [8]  Cube (x³)              │ ")
    print(" │                         │  [9]  Cube-Root (³√)         │ ")
    print(" ├─────────────────────────┴──────────────────────────────┤ ")
    print(" │  🛠️  ADVANCED SUITE & CONTROL                         │ ")
    print(" ├────────────────────────────────────────────────────────┤ ")
    print(" │  [10] Factorial (!)     │  [11] Modulus (%)            │ ")
    print(" │  [12] Emergency Exit    │                              │ ")
    print(" └────────────────────────────────────────────────────────┘ ")
    print("═"*60)

    decision = int(input(" ➔ Select Operation (1-12): "))
    # core if-elif-else ladder
    if(decision == 1):
        addition()
    elif(decision == 2):
        substraction()
    elif(decision == 3):
        multiplication()
    elif(decision == 4):
        division()
    elif(decision == 5):
        Exponent()
    elif(decision == 6):
        square()
    elif(decision == 7):
        square_root()
    elif(decision == 8):
        cube()
    elif(decision == 9):
        cube_root()
    elif(decision == 10):
        factorial()
    elif(decision == 11):
        modulus()
    elif(decision == 12):
        sys.exit()
    else:
        print("Your input is Out of Option")
else:
    print("Ur options are not enough or more than the number u gave")
    sys.exit()