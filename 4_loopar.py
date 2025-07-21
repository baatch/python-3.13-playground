# Nu ska vi lära oss om loopar!
# En loop är som "repetera" blocket i Scratch
# Den gör samma sak flera gånger

# Först ska vi räkna till 5
print("Nu ska vi räkna till 5:")
for i in range(5):  # range(5) betyder "gör detta 5 gånger"
    print(i + 1)    # Vi lägger till 1 eftersom datorn börjar räkna från 0

# Nu ska vi göra något roligt - rita en trappa med *
print("\nHär kommer en trappa:")  # \n betyder "ny rad"
for i in range(5):
    print("*" * (i + 1))  # * gånger ett nummer ritar ut stjärnor

# Prova att ändra siffrorna i range() och se vad som händer!
# Till exempel, ändra range(5) till range(10)
