"""Flight paths code kata."""


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.

    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.
    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = (math.sin(0.5 * delta_phi)**2 +
         math.cos(phi1) * math.cos(phi2) *
         math.sin(0.5 * delta_lam)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def d_shortest_path(self, start, end):
    """Find the shortest path using Dijkstra's algorithm."""
    if start not in self.nodes() or end not in self.nodes():
        raise KeyError('Graph does not contain one or both nodes.')
    current_node = start
    visited = {}
    unvisited = {node: float("inf") for node in self.nodes()}
    paths = {node: '' for node in self.nodes()}
    unvisited[current_node] = 0
    if not len(self.edges()):
        raise KeyError('No edges in this graph.')
    edges = {(edge[0], edge[1]): edge[2] for edge in self.edges()}
    while end not in visited or min(unvisited.values()) == float("inf"):
        origin = current_node
        for node in unvisited:
            if (current_node, node) in edges:
                tentative_weight = (unvisited[current_node] +
                                    edges[(current_node, node)])
                if unvisited[node] > tentative_weight:
                    unvisited[node] = tentative_weight
                    paths[node] = origin
        visited[current_node] = min(unvisited.values())
        del unvisited[current_node]
        if len(unvisited):
            current_node = min(unvisited.keys(), key=unvisited.get)
        else:
            break
    if visited[end] == float("inf"):
        raise IndexError('There is no path between those nodes.')
    curr = end
    path = []
    while start not in path:
        path.insert(0, curr)
        curr = paths[curr]
    return path
