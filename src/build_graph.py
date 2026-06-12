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