palestrantes = (
    ("João", "HTML", "Infinity"),
    ("Maria", "Python", "UFC"),
    ("Ana", "JavaScript", "UECE"),
    ("Pedro", "Java", "Infinity"),
    ("Abel", "React", "Infinity"),
    ("Amanda", "Django", "UFC")
)

print(f"""
    Nome do(a) palestrante: {palestrantes[2][0]}
    Tema da palestra: {palestrantes[2][1]}
    Instituição do(a) palestrante: {palestrantes[2][2]}
""")

cont = 0
nome_dos_palestrantes_infinity = []
for palestrante_da_vez in palestrantes:
    if palestrante_da_vez[2] == "Infinity":
        cont +=1
        nome_dos_palestrantes_infinity.append(palestrante_da_vez[0])

print(f"Tinham {cont} palestrantes da Infinity School")

print("Os nomes dos palestrantes da Infinity são: ")
for palestrante in nome_dos_palestrantes_infinity:
    print(palestrante)