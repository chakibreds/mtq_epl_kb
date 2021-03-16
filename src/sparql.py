import rdflib

def sparql_construct(bet, file_name, verbose=False):
    if verbose:
        print("executing", file_name)
    with open(file_name,'r') as file:
        q = file.read()
        res = bet.query(q)
        if verbose:
            print(len(res),' element added to the ontologie.')
        for r in res:
            bet.add(r)