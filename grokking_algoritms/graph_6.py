from collections import deque


def person_is_seller(name):
    return name[-1] == 'go'


graph = {}
graph['you'] = ["alice", "bob", "claire"]
graph['bob'] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue = deque()


def find(search_queue):
    if search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + "is seller")
            return True
        else:
            search_queue += graph[person]
        return find(search_queue)
    else:
        return None


search_queue += graph["you"]
print(find(search_queue))
