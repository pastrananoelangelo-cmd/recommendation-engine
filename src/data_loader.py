import csv

def load_interactions(filename):
    interactions = {}

    with open(filename, "r") as file:
        data = csv.DictReader(file)

        for row in data:
            user = row["user"]
            item = row["item"]

            if user not in interactions:
                interactions[user] = []
            
            interactions[user].append(item)
    
    return interactions
            

