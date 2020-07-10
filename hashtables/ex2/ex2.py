#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
# make a cache
# put the tickets in with source as key, destination as value
# pick out the source == NONE
# until cache.value == none
#    query cache using last value
#    add key to master list

def reconstruct_trip(tickets, length):
    cache = {}
    route = []

    for i in tickets:
        cache[i.source] = i.destination

    next_dest = cache['NONE']

    for i in range(length):
        route.append(next_dest)
        next_dest = cache[next_dest]

    return route
