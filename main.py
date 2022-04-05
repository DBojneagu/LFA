class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, simbol):
        if from_node in self.edges:

            self.edges[from_node].append((to_node, simbol))

        else:

            self.edges[from_node] = [(to_node, simbol)]

    def dfs2(self, curr_node, cuv, L, lista_nr_noduri, L2, str_finala):

        while len(cuv) > 0:
            i = 0
            for next_node, simbol in self.edges.get(curr_node, []):
                i += 1
                if simbol == cuv[0]:
                    L.append(next_node)
                    L2.append(lista_nr_noduri[next_node])
                    cuv = cuv[1:]
                    if len(cuv) == 0 and next_node in str_finala:
                        print("DA")
                        print("".join(L2))
                        print("Traseu: ", *L)
                        break
                    if len(cuv) == 0 and next_node not in  str_finala:
                        print("NU")
                        break
                    self.dfs2(next_node, cuv, L, lista_nr_noduri, L2, str_finala)
                    break
                if i == len(self.edges[curr_node]) and simbol != cuv[0]:
                    print("NU")
                    break
            break


g = Graph()
f = open("input.txt")
t = f.readline()
t = t.split()
nr_stari, nr_drumuri = int(t[0]), int(t[1])
b = f.readline()

lista_nr_noduri = b.split()

for i in range(nr_drumuri):
    linie = f.readline()
    aux = linie.split()
    g.add_edge(int(aux[0]), int(aux[1]), aux[2])

stare_initiala = f.readline()
pre_stare_finala = f.readline()
aux = pre_stare_finala.split()

stari_finale = []
for cif in aux:
    stari_finale.append(int(cif))
stari_finale = stari_finale[1:]

nr_teste = f.readline()

for linie in f:
    cuv = linie.strip()
    L = []
    L2 = []
    L.append(int(stare_initiala))
    L2.append(lista_nr_noduri[int(stare_initiala)])
    g.dfs2(0, cuv, L, lista_nr_noduri, L2, stari_finale)