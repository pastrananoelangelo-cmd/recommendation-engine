import math
import copy

def user_item_weights(user_owns):
    user_weights = {}
    
    for item in user_owns:
        user_weights[item] = 1.0
    
    return user_weights


def recommended_items(owned_items, normalized, user_weights, popularity, k):
    # Get the scores of each item.
    score = {}
    topK = {}
    contribution = {}
    contribution_filtered = {}

    for owned_item in owned_items:
        for item, weight in normalized[owned_item].items():
            if item not in score:
                score[item] = 0
            score[item] += weight * user_weights[owned_item]

            if item not in contribution:
                contribution[item] = {}
            
            if owned_item not in contribution[item]:
                contribution[item][owned_item] = weight * user_weights[owned_item]
            else:
                contribution[item][owned_item] += weight * user_weights[owned_item]

    for item in score:
        if popularity[item] != 0:
            score[item] /= math.sqrt(popularity[item])
        else:
            score[item] /= math.sqrt(1)

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

    # Retain only contribution in topK.
    for item, related_items in contribution.items():
        if item in topK:
            contribution_filtered[item] = copy.deepcopy(contribution[item])

    # Compute Importance
    for item, related_items in contribution_filtered.items():
        denominator = 0

        for item2, relevance in related_items.items():
            denominator += relevance
        
        for item2, relevance in related_items.items():
            contribution_filtered[item][item2] /= denominator

    # print("Sorted:")
    # print(topK)
    # print()

    # Return top k items and their contribution.
    return topK, contribution_filtered