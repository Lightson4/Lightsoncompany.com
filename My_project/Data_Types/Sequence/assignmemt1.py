light_workers = ["Victor Light", "Mercy Chibuchi", "Mctim Timothy", "Grace Goodness", "Excel justice", "Miracle Okeoma", "Monday Stanley", "France Prince", "Solomon Benjemin", "Uche  Smart", "Victor Light", "Eman Bliss", "Victor Light", "Pleasure Gift", "Victor Light", "Eman Bliss", "Victor Light", "Eman Bliss", "Precious Alison", "Ibe Okeugo"] 
new_employed_workers = ["Blessing Nelson", "Ochor Friday", "Victoria Frank", "Divine Favour", "Fortune Ezeane"]
light_new_workers = light_workers + new_employed_workers
print(light_new_workers)
for name in set(light_new_workers):
    if light_new_workers.count(name) > 1:
        print(f"{name} appeard more than once")
print(light_new_workers.count("Victor Light"))
print(light_new_workers.count("Eman Bliss"))