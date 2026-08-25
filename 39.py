def profile(**person):
    for key, value in person.items():
        print(key, ":", value)
profile(name="Deepika", age=20, city="Rajahmundry")