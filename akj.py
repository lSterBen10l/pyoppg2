# Oppgave 1:
start_tall = int(input("skriv et tall for å starte nedtellingen:"))
while start_tall >= 0:
    print(start_tall)
    start_tall -= 1

# Oppgave 2:
bruker_tall = int(input("skriv et tall for å se gangetabellen: "))
for i in range(1, 11):
    print(f"{bruker_tall} x {i} = {bruker_tall * i}")

# Oppgave 3:
hemmelig_tall = 42 
print("Gjett et tall mellom 1 og 100")
while True:
    gjett = int(input("Skriv inn ditt gjett: "))
    if gjett == hemmelig_tall:
        print("Gratulerer. Du gjettet riktig!")
        break
    elif gjett < hemmelig_tall:
        print("For lavt! Prøv igjen.")
    else:
        print("For høyt! Prøv igjen.")

# Oppgave 4: 
def er_primtall(tall):
    if tall < 2:
        return False
    for i in range(2, int(tall ** 0.5) + 1):
        if tall % i == 0:
            return False
    return True

print("Primtall mellom 1 og 100:")
for nummer in range(1, 101):
    if er_primtall(nummer):
        print(nummer)

# Oppgave 5: 
def areal_av_sirkel(radius):
    import math
    return math.pi * radius ** 2

print("Beregn arealet av sirkler. Skriv inn -1 for å avslutte.")
while True:
    radius = float(input("Oppgi radiusen til sirkelen: "))
    if radius == -1:
        print("Avslutter...")
        break
    elif radius < 0:
        print("Radius kan ikke være negativ. Prøv igjen.")
    else:
        print(f"Arealet av sirkelen med radius {radius} er {areal_av_sirkel(radius):.2f}")