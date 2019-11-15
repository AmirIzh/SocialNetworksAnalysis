import pandas as pd

out_edges_dict = {}
in_edges_dict = {}
pages_rank_dict = {}

def load_graph(path):
    df = pd.read_csv(path, header = None)
    for row in df.iterrows():
        source = str(row[1][0])
        dest = str(row[1][1])

        #initialize the out_edges and in_edges dicts:
        if not out_edges_dict.get(source):
            out_edges_dict[source] = [dest]
        else:
            out_edges_dict[source].append(dest)

        if not in_edges_dict.get(dest):
            in_edges_dict[dest] = [source]
        else:
            in_edges_dict[dest].append(source)

        #initialize pages_rank_dict:
        if not pages_rank_dict.get(source):
            pages_rank_dict[source] = 0
        if not pages_rank_dict.get(dest):
            pages_rank_dict[dest] = 0

def main():
    load_graph("C:\\Users\\amiri\\Desktop\\myGraph.csv")

if __name__ == '__main__':
    main()



