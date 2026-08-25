def employee(**details):
    for key, value in details.items():
        print(key, ":", value)
employee(name="Ravi", department="IT", salary=50000)