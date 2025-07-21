# Nu ska vi göra ett spel där datorn gissar din ålder!
# Detta är som att "fråga och vänta" i Scratch

print("Hej! Jag ska gissa din ålder.")
print("Men först behöver jag veta några saker...")

# input betyder att datorn väntar på att du ska skriva något
favorit_färg = input("Vilken är din favoritfärg? ")
print("Aha!", favorit_färg, "är en fin färg!")

# Nu ska vi göra om svaret till ett nummer
födelse_månad = int(input("Vilken månad är du född i? (1-12): "))

# Här använder vi if-else, som är som "om-då" i Scratch
if födelse_månad <= 6:
    print("Du är född på första halvan av året!")
else:
    print("Du är född på andra halvan av året!")

# Vi kan också använda and (och) för att kolla flera saker
if födelse_månad >= 6 and födelse_månad <= 8:
    print("Du är född på sommaren!")

print("Tack för att du lekte med mig!")
