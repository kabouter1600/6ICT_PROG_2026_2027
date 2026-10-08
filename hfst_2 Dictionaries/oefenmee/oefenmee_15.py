# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgi?': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}

for grote_land in grootste_steden:
    print(f"de grooste steden in het land{grote_land} zijn: ")
    for stad in grootste_steden[grote_land]:
        bevolking = grootste_steden[grote_land][stad]
        print(f"de stad {stad} met {bevolking} inwoners")