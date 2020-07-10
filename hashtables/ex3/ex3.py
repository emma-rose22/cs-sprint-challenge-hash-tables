#iterate through lists and add to cache
#if key value == number of lists
#    append to duplicate list
# return duplicate list

def intersection(arrays):
    cache = {}
    intersection = len(arrays)
    numbers = []
    for nums in arrays:
        for i in nums:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1
                if cache[i] == intersection:
                    numbers.append(i)

    return numbers

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
