def recharge_energy(current_energy, recharge):

    updated_energy = current_energy + recharge

    if updated_energy > 100:
        return 100

    return updated_energy


current_energy = int(input("Enter current energy: "))

recharge = int(input("Enter recharge energy: "))

updated_energy = recharge_energy(current_energy, recharge)

print(f"Updated Energy Level: {updated_energy}%")