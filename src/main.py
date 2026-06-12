from data_loader import load_interactions
from build_graph import build_item_graph
from recommender import recommended_items

def main():
    filename = "data/interactions.csv"
    interactions = load_interactions(filename=filename)
    # for user, items in interactions.items():
    #     print(f"User: {user}")
    #     for item in items:
    #         print(" -", item)
    #     print()
    
    connections = build_item_graph(interactions)
    # for main_item, related_items in connections.items():
    #     print(f"{main_item}:")
    #     for item, weight in related_items.items():
    #         print(f"    - {item}: {weight}")
    #     print()

    results = recommended_items(['Laptop', 'Mouse'], connections, k=3)
    for top_item, score in results.items():
        print(f"{top_item} = {score}")
    

if __name__ == "__main__":
    main()
    print()