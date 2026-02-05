contacts = {
    "tulsi": "9876543210",
    "Riya": "9123456780",
    "Karan": "9988776655"
}
contacts["Megha"] = "9001122334"
contacts["Riya"] = "7000000001"
found = contacts.get("tulsi", "Contact not found")
not_found = contacts.get("Rahul", "Contact not found")
print("tulsi's number:", found)
print("Rahul's number:", not_found)
print("\nAll Contacts:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)