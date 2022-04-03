
class Graph:
    def __init__(self):
        self.edges = {}
    def add_edge(self,from_node,to_node,simbol):
        if from_node in self.edges:
            self.edges[from_node].append((to_node,simbol))
        else:
            self.edges[from_node] = [(from_node,simbol)]

    def print(self):
        for node in self.edges:
            for to_node in self.edges[node]:
                print(f"de la {node} la {to_node}")

    def dfs(self,curr_node,viz= {}):
        viz[curr_node] = True
        for next_node,simbol in self.edges.get(curr_node,[]):
              if next_node in viz:
                 continue
              print(f"de la {curr_node} la {next_node} prin {simbol}")
              self.dfs(next_node,viz)

g = Graph()
f = open("input.txt")
t = f.readline()
t = t.split()
nr_stari,nr_drumuri = t[0],t[1]
print (f"Numarul de stari : {nr_stari}\nNumarul de drumuri : {nr_drumuri}\n")

for linie in f:

    aux = linie.split()
    g.add_edge(int(aux[0]), int(aux[1]), aux[2])

g.print()
print()
g.dfs(1)



