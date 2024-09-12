marks = {
    "Aadi" : 100,
    "Veer" : 56,
    "Nilay" : 23,
    0: "Aadi"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Aadi" : 99, "Rishi" : 100})

print(marks.get("Aadi")) # Prints None
print(marks["Aadi"]) # Returns an error