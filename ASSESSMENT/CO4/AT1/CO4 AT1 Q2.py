machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

for machine, status in machines.items():

    if status == "Active":
        print(machine, "-> Producing")

    elif status == "Maintenance":
        print(machine, "-> Not Producing")
