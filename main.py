
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
        print(viz)
        for next_node,simbol in self.edges.get(curr_node,[]):
              if next_node in viz:
                 continue
              print(f"de la {curr_node} la {next_node} prin {simbol}")
              print(self.edges[curr_node])
              self.dfs(next_node,viz)

    def dfs2(self,curr_node,cuv,ok = 1,viz= {}):
        viz[curr_node] = True
        print(viz)
        print(cuv)
        while len(cuv) - 1 > 0 :
            i = 0 
            for next_node,simbol in self.edges.get(curr_node,[]):
                i+=1 
                print(self.edges[curr_node])

                if simbol == cuv[0]:
                    print(f"Am gasit litera, trecem mai departe,mergem prin {next_node}")
                    cuv = cuv[1:]
                    if len(cuv) == 1:
                        print("Am gasit cuvantul, am terminat.")
                        break
                    self.dfs2(next_node,cuv)
                    break    
                if i == len(self.edges[curr_node]) and simbol != cuv[0]:
                   print("Cuvantul nu poate fi acceptat") 
                   break
            break 
                    
g = Graph()
f = open("input.txt")
t = f.readline()
t = t.split()
nr_stari,nr_drumuri = int(t[0]),int(t[1])
print (f"Numarul de stari : {nr_stari}\nNumarul de drumuri : {nr_drumuri}\n")
i = 0
for i in range(nr_drumuri+1):
    linie = f.readline()
    aux = linie.split()
    g.add_edge(int(aux[0]), int(aux[1]), aux[2])
    
g.print()
print()
g.dfs(0)

stare_initiala = f.readline()
pre_stare_finala = f.readline()
aux = pre_stare_finala.split()
stare_finala = aux[1]
nr_teste = f.readline()


for linie in f:
    cuv = linie 
    print(f"Cuvantul este :{cuv}")
    print(f"Numarul de teste {nr_teste} ")
    print(f"Cuvantul initial: {cuv}")
    g.dfs2(0,cuv)





