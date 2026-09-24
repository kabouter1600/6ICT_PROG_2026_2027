# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 8,
    "Werk":  8,
    "Ontspanning": 8
}
uur = 24
print("planning morgen:")
for plan, waarde in planner.items():
    print(f"-{plan}: {waarde}uur mee bezig")
    uur -= waarde
print(f"je hebt {uur}uur over")