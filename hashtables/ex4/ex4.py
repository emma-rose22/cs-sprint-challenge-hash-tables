#create a cache
#loop
# save positive numbers to list
# insert every neg value into the cache
#   key is the og number
#   value is neg num + (negative num * neg 2) 
#   this will make the number into its positive partner
# now we can query the cache with our pos number list
# if query == cache value:
#   add query to results list and return

def has_negatives(a):
    cache = {}
    positives = []
    result = []
    for i in a:
        if i > 0:
            positives.append(i)
        else:
            cache[i + (i * -2)] = i
    for i in positives:
        if i in cache:
            result.append(i)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
