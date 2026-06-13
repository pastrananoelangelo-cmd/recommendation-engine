from data_loader import load_interactions
from build_graph import build_item_graph
from build_graph import normalize_graph
from build_graph import compute_popularity
from recommender import user_item_weights
from recommender import recommended_items

def main():
    filename = "data/interactions.csv"
    user_owns = ['Laptop']

    interactions = load_interactions(filename=filename)
    # for user, items in interactions.items():
    #     print(f"{user}: ")
    #     for item in items:
    #         print(" -", item)
    #     print()
    
    connections = build_item_graph(interactions)
    # for main_item, related_items in connections.items():
    #     print(f"{main_item}:")
    #     for item, weight in related_items.items():
    #         print(f"    - {item}: {weight}")
    #     print()

    normalized = normalize_graph(connections)
    # for main_item, related_items in normalized.items():
    #     print(f"{main_item}:")
    #     for item, weight in related_items.items():
    #         print(f"    - {item}: {weight}")
    #     print()

    user_weight = user_item_weights(user_owns)

    popularity = compute_popularity(interactions)

    results = recommended_items(user_owns, normalized, user_weight, popularity, k=3)
    for top_item, score in results.items():
        print(f"{top_item} = {score}")
    

if __name__ == "__main__":
    main()
    print()