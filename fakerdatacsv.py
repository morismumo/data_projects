from faker import Faker
import csv

fake = Faker()
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

with open("data.csv", "w", newline='') as output:
    mywriter = csv.writer(output)
    mywriter.writerow(header)

    for _ in range(1000):
        mywriter.writerow([
            fake.name(),
            fake.random_int(min=18, max=80, step=1),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.longitude(),
            fake.latitude()
        ])
