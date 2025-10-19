tagam = "palau"
tagam_kal = 150.0
tagam_salmak = 200.0

paidalanyshy_tagamy = input("Sizdin suiikti tagamyńyz: ")
paidalanyshy_kal = float(input("Ol tagamnyń 100 g úshin kaloriasy: "))
paidalanyshy_salmak = float(input("Siz zheitin mólsher (g): "))

jalpy_kal = (paidalanyshy_kal * paidalanyshy_salmak) / 100
ortasha_kal = (tagam_kal + paidalanyshy_kal) / 2

print("\n--- As mәziri ---")
print(f"Negizgi tagam: {tagam}")
print(f"Sizdin tańdauyńyz: {paidalanyshy_tagamy}")
print(f"100 g kaloria: {paidalanyshy_kal}")
print(f"Zhegen mólsherińiz: {paidalanyshy_salmak} g")
print(f"Barlygy: {jalpy_kal:.1f} kkal")
print(f"Ortasha kaloria: {ortasha_kal:.1f} kkal")


tagamdar = ["beshbarmaq", "palaý", "sushi", "tort", "kofe", "bauyrsaq", "steik", "omlet", "shai", "burger"]
print("\nTagamdar tizimi:", tagamdar)

biregei_tagamdar = set(tagamdar)
print("Biregei tagamdar:", biregei_tagamdar)

as_turleri = ("tańǵy as", "túski as", "keshki as")
print("\nQai asqa mәzir quraǵymyz?")
for nomer, as_turi in enumerate(as_turleri, 1):
    print(f"{nomer}. {as_turi}")

tańdau = int(input("Nómirin tańdańyz: "))

if tańdau == 1:
    print("Siz tańǵy as mәzirin tańdadyńyz.")
elif tańdau == 2:
    print("Siz túski as mәzirin tańdadyńyz.")
elif tańdau == 3:
    print("Siz keshki as mәzirin tańdadyńyz.")
else:
    print("Qate tańdau!")


izdeletin_tagam = input("\nQai tagamdy izdeisińiz? ").lower()
if izdeletin_tagam in biregei_tagamdar:
    print("Iә, mundaı tagam mәzirde bar!")
else:
    print("Ondaı tagam mәzirde joq.")

sipattama = "Búginǵi mәzirde dәmdi palaý, jumsaq bauyrsaq jáne qoıu kofe bar."
print("\nSipattama:", sipattama)

sózder = sipattama.split()
print("Sózder sany:", len(sózder))

zhańartylǵan_sipattama = sipattama.replace("kofe", "shai")
print("Zhańartylǵan sipattama:", zhańartylǵan_sipattama)

tagamdar_dict = {
    "beshbarmaq": 320,
    "palaý": 290,
    "sushi": 150,
    "tort": 340,
    "kofe": 40,
    "bauyrsaq": 270,
    "steik": 310,
    "omlet": 154,
    "shai": 10,
    "burger": 330
}

while True:
    print("\n--- Mәzir ---")
    print("1 - Tagamdar tizimi")
    print("2 - Tagam qosu")
    print("3 - Kaloria kóru")
    print("4 - Jalpy kaloria")
    print("5 - Shyǵu")

    tańdau_turi = input("Tańdauyńyz: ")

    if tańdau_turi == "1":
        print("\nBarlyq tagamdar:")
        for ataý, kal in tagamdar_dict.items():
            print(f"{ataý}: {kal} kkal (100 g)")
    elif tańdau_turi == "2":
        ataý = input("Tagam ataýy: ")
        kal = float(input("100 g úshin kaloria: "))
        tagamdar_dict[ataý] = kal
        print(f"{ataý} mәzirge qosyldy!")
    elif tańdau_turi == "3":
        ataý = input("Qai tagamnyń kaloriasyn bilgińiz keledi? ")
        if ataý in tagamdar_dict:
            print(f"{ataý} tagamy: {tagamdar_dict[ataý]} kkal (100 g)")
        else:
            print("Ondaı tagam joq.")
    elif tańdau_turi == "4":
        jalpy = sum(tagamdar_dict.values())
        ortasha = jalpy / len(tagamdar_dict)
        print(f"Barlyq tagamdardyń jalpy kaloriasy: {jalpy:.1f} kkal")
        print(f"Ortasha kaloria: {ortasha:.1f} kkal")
    elif tańdau_turi == "5":
        print("Baǵdarlama ayaqtaldy. Raqmet!")
        break
    else:
        print("Qate tańdau! Dúrys nómir engizińiz.")
