from decimal import Decimal
import pandas as pd
import heapq
import speech_recognition as sr

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        if length <= 0:
            raise ValueError("Distance must be a positive integer")
        edge = Edge(to_node, length)
        if from_node.label not in self.edges:
            self.edges[from_node.label] = {}
        self.edges[from_node.label][to_node.label] = edge

def dijkstra(graph, source):
    dist = {node: Decimal('Infinity') for node in graph.nodes}
    prev = {node: None for node in graph.nodes}
    dist[source] = 0

    priority_queue = [(0, source)]  # (distance, node)
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > dist[u]:
            continue

        if u.label in graph.edges:
            for neighbor_label, edge in graph.edges[u.label].items():
                v = edge.to_node
                alt = dist[u] + edge.length
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(priority_queue, (alt, v))

    return dist, prev

def to_array(prev, from_node):
    route = []
    current = from_node
    while current:
        route.append(current.label)
        current = prev[current]
    route.reverse()
    return route

def recognize_speech(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            print("Could not understand. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return None

# Initialize graph and nodes
graph = Graph()
dict_of_nodes = {}

# Input method selection
input_type = int(input("Do you want to add places manually or through a file?\n"
                       "Press 1 for manual entry\n"
                       "Press 2 for adding a CSV file\n"))
if input_type == 2:
    path = input("Enter path of the CSV file: ")
    df = pd.read_csv(path)
    list_of_places = list(df['source']) + list(df['dest'])
    for place in set(list_of_places):
        node = Node(place)
        dict_of_nodes[place] = node
        graph.add_node(node)

    for _, row in df.iterrows():
        graph.add_edge(dict_of_nodes[row['source']], dict_of_nodes[row['dest']], int(row['dist']))
        graph.add_edge(dict_of_nodes[row['dest']], dict_of_nodes[row['source']], int(row['dist']))
elif input_type == 1:
    while True:
        place = input("Enter a place (type 'exit' when done): ")
        if place.lower() == "exit":
            break
        node = Node(place)
        dict_of_nodes[place] = node
        graph.add_node(node)

    while True:
        place1 = input("Enter the first place (type 'exit' when done): ")
        if place1.lower() == "exit":
            break
        place2 = input("Enter the second place: ")
        distance = int(input("Enter the distance between them: "))
        graph.add_edge(dict_of_nodes[place1], dict_of_nodes[place2], distance)
        graph.add_edge(dict_of_nodes[place2], dict_of_nodes[place1], distance)

# Main loop for user interaction
while True:
    source = None
    dest = None
    for attempt in range(3):
        source = recognize_speech("Speak your source location:")
        if source in dict_of_nodes:
            break
        else:
            print(f"'{source}' is not a valid location. Please try again.")

    if not source:
        print("Failed to recognize the source location after multiple attempts. Exiting.")
        break

    for attempt in range(3):
        dest = recognize_speech("Speak your destination location:")
        if dest in dict_of_nodes:
            break
        else:
            print(f"'{dest}' is not a valid location. Please try again.")

    if not dest:
        print("Failed to recognize the destination location after multiple attempts. Exiting.")
        break

    print(f"The source and destination are: {source} -> {dest}")
    dist, prev = dijkstra(graph, dict_of_nodes[source])
    if dict_of_nodes[dest] not in dist or dist[dict_of_nodes[dest]] == Decimal('Infinity'):
        print(f"No path found from {source} to {dest}.")
    else:
        print(f"The quickest path from {source} to {dest} is {to_array(prev, dict_of_nodes[dest])} "
              f"with a distance of {dist[dict_of_nodes[dest]]}.")

    repeat = input("Do you want to run again? (y/n): ").lower()
    if repeat == 'n':
        break
