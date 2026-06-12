def recommended_items(owned_items, connections, k):
    # Get the scores of each item.
    score = {}
    topK = {}

    for owned_item in owned_items:
        for item, weight in connections[owned_item].items():
            if item not in score:
                score[item] = 0
            score[item] += weight
    
    # Filter what the user owns.
    for owned_item in owned_items:
        if owned_item in score:
            del score[owned_item]

    # print("Scores:")
    # print(score)
    # print()

    # Sort score.
    for i in range(0, k):
        highestWeight = -1
        highestItem = ""
        checker = False
        
        for item, weight in score.items():
            if item not in topK: 
                checker = True
                if weight > highestWeight:
                    highestWeight = weight
                    highestItem = item
        
        if checker:
            topK[highestItem] = highestWeight
        else:
            break

    # print("Sorted:")
    # print(topK)
    # print()

    # Return top k items.
    return topK