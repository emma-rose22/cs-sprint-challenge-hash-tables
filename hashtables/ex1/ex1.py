def get_indices_of_item_weights(weights, length, limit):
    #create a cache 
    # put everything in the cache, weight as key and index as value
    # for each weight
    #   query cache another weight == limit - weight1
    #   if they match:
    #      pick the bigger number to append index first, then second
    #   return results
    # 

    cache = {}
    answer = None
    for i in weights:
        cache[i] =  weights.index(i)
    for weight in cache.keys():
        difference = limit - weight
        if difference in cache:
            print('d', difference)
            print('w', weight)
            if difference >= weight:
                answer = [weights.index(difference), weights.index(weight)]
            if weight >= difference:
                answer = [weights.index(weight), weights.index(difference)]
    return answer

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)

#this test answer is failing, but it is following the rules
# and printing the larger variable first, smaller second
# the test is failing because for some reason it is expecing 
# the 0 to be at the first index and 7 at the second.
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)