# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # go through the list
    # if the last characters match 
    # add filepath to results and return 
    # ^^ without a hashtable 

    #make a cache
    # I could add the file and length as a key value pair in dictionary
    # and then use that to search through each file path
    # for i in queries
    #    if i[-key:] == value:
    #    results.append(i)

    cache = {}
    result = []

    # for i in queries:
    #     cache[i] = len(i)

    # #print(list(cache.keys()))

    # for i in files:
    #     for x in cache.values():
    #         if i[-x:] in cache:
    #             result.append(i)

    # return list(set(result))

    # make a cache
    # if file not in cache:
    #     if file[-len(qury):] == query:
    #      add to cache
    length = []
    for i in queries:
        length.append(len(i))

    length = list(set(length))
    
    for x in files:
        if x not in cache:
            for i in length:
                if x[-i:] in queries:
                    cache[x[-i:]] = x
        else:
            if x[-i:] in queries:
                cache[x[-i:]] = x

    return list(cache.values())

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
