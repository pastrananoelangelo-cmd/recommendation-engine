from data_loader import load_interactions
from build_graph import build_item_graph
from build_graph import normalize_graph
from build_graph import compute_popularity
from recommender import user_item_weights
from recommender import recommended_items


def generate_reason(contributions):
    items = sorted(contributions.items(), key=lambda x: x[1], reverse=True)

    if not items:
        return "No contributing factors."

    if len(items) == 1:
        return f"This is mainly influenced by {items[0][0]} usage."

    top_item, top_weight = items[0]
    second_item, second_weight = items[1]

    diff = top_weight - second_weight

    # Case 1: balanced influence
    if diff < 0.1:
        return f"This is influenced equally by {top_item} and {second_item} usage patterns."

    # Case 2: dominant + secondary
    return (
        f"This is mainly influenced by {top_item} usage, "
        f"with additional influence from {second_item}."
    )


def main():
    filename = "data/interactions.csv"
    user_owns = ['Laptop', 'Mouse']

    interactions = load_interactions(filename=filename)
    # print("Interactions:")
    # for user, items in interactions.items():
    #     print(f"{user}: ")
    #     for item in items:
    #         print(" -", item)
    #     print()
    
    connections = build_item_graph(interactions)
    # print("Connections:")
    # for main_item, related_items in connections.items():
    #     print(f"{main_item}:")
    #     for item, weight in related_items.items():
    #         print(f"    - {item}: {weight}")
    #     print()

    normalized = normalize_graph(connections)
    # print("Normalized:")
    # for main_item, related_items in normalized.items():
    #     print(f"{main_item}:")
    #     for item, weight in related_items.items():
    #         print(f"    - {item}: {weight}")
    #     print()

    user_weight = user_item_weights(user_owns)
    # print("User Item Weights:")
    # for item, weight in user_weight.items():
    #     print(f"{item}: {weight}")
    # print()

    popularity = compute_popularity(interactions)
    # print("Polularity:")
    # for item, weight in popularity.items():
    #     print(f"{item}: {weight}")
    # print()

    results, contribution = recommended_items(user_owns, normalized, user_weight, popularity, k=3)
    # print("Results:")
    # for top_item, score in results.items():
    #     print(f"{top_item} = {score}")
    #     for contributors, scores in contribution[top_item].items():
    #         print(f"    - {contributors}: {scores}")
    #     print()
    # print()

    # Show results: Human Friendly.
    print("Results:")
    for top_item, score in results.items():
        print(f"Recommended: {top_item}")
        
        reason = generate_reason(contribution[top_item])
        print(f"Why: {reason}")

        print("Evidence: ")
        for contributors, scores in contribution[top_item].items():
            print(f"    - {contributors}: {scores * 100:.2f}")
        print(f"Score: {score}")
        print()
    

if __name__ == "__main__":
    main()