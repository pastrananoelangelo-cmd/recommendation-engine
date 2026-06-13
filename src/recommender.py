import math

def user_item_weights(user_owns):
    user_weights = {}
    
    for item in user_owns:
        user_weights[item] = 1.0
    
    return user_weights


def recommended_items(owned_items, normalized, user_weights, popularity, k):
    # Get the scores of each item.
    score = {}
    topK = {}

    for owned_item in owned_items:
        for item, weight in normalized[owned_item].items():
            if item not in score:
                score[item] = 0
            score[item] += weight * user_weights[owned_item]
    
    for item in score:
        score[item] /= math.sqrt(popularity[item])

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