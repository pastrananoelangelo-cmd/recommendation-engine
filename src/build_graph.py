def build_item_graph(interactions):
    main_item = {}
    for user, items in interactions.items():
        for i in range(0, len(items)):
            if items[i] not in main_item:
                main_item[items[i]] = {}

            for j in range(0, i):
                if items[i] == items[j]:
                    continue

                if items[j] not in main_item[items[i]]:
                    main_item[items[i]][items[j]] = 1
                    main_item[items[j]][items[i]] = 1
                else:
                    main_item[items[i]][items[j]] += 1
                    main_item[items[j]][items[i]] += 1

    return main_item


def compute_popularity(interactions):
    popularity = {}

    for user, items in interactions.items():
        for item in set(items):
            if item not in popularity:
                popularity[item] = 0
            popularity[item] += 1
    
    return popularity


def normalize_graph(connections):
    normalized_connections = {}
    
    for main_item, related_items in connections.items():
        normalized_connections[main_item] = {}
        denominator = 0

        for item, weight in related_items.items():
            denominator += weight
        
        for item, weight in related_items.items():
            normalized_connections[main_item][item] = weight / denominator
    
    return normalized_connections