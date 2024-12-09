class Graph:
    def __init__(self, n=0):
        __n = n
        __g = [[0 for _ in range(10)] for _ in range(10)]

    def inputGraph(self):
        self.__n = int(input("Enter the number of nodes: "))
        print("Enter the adjacency matrix: ")
        self.__g = []
        for i in range(self.__n):
            row = list(map(int, input().split()))
            self.__g.append(row)


    def displayAdjacencyMatrix(self):
        print("Adjacency Matrix:", end="")
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end="")

    def removeNode(self, node_delete):
        if (node_delete >= self.__n):
            print("Node does not exist!")
            return

        self.__g.pop(node_delete)

        for i in range(len(self.__g)):
            self.__g[i].pop(node_delete)

        self.__n = self.__n - 1

if __name__ == "__main__":
    graph = Graph()
    graph.inputGraph()
    print("\nGraph before deletion")
    graph.displayAdjacencyMatrix()
    node_delete = int(input("\nEnter the node to delete: "))
    graph.removeNode(node_delete)
    print("\nGraph after deletion")
    graph.displayAdjacencyMatrix()
