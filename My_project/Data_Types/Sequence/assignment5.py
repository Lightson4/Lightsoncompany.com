cocoma = ["Light", "Mercy", "Mctim", "Grace", "Gift", "Excell", "Miracle", "Stanley", "France", "Solomon", "Uche", "Ibe", "Bliss", " Light", "Gift", "Gift", "Light", "Bliss", "Light", "Bliss", "Grace", "Precious", "Ibe"] 
cocoma_new_workers = ["Blessing", "Friday", "Victoria", "Favour", "Fortune"]
cocoma_workers = cocoma + cocoma_new_workers
print(cocoma_workers)
for name in set(cocoma_workers):
    if cocoma_workers.count(name) > 1:
        print(f"{name} appeard more than once")
print(cocoma_workers.count("Light"))
print(cocoma_workers.count("Gift"))
print(cocoma_workers.count("Ibe"))
print(cocoma_workers.count("Grace"))
print(cocoma_workers.count("Bliss"))
print(cocoma_workers.remove("Light"))
print(cocoma_workers.remove("Gift"))
print(cocoma_workers.remove("Ibe"))
print(cocoma_workers.remove("Grace"))
print(cocoma_workers.remove("Bliss"))
print(cocoma_workers)