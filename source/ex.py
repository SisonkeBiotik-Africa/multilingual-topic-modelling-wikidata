from Bio import Entrez, Medline
from datetime import datetime

N = 100

Entrez.email = 'turkiabdelwaheb@hotmail.fr'
timebegin = datetime.now()
handle = Entrez.esearch(db="pmc", retmax=N, term='"Cough" AND "Symptom" AND "COVID-19"', sort="relevance")
records1 = Entrez.read(handle)
handle.close()
timeend = datetime.now()
runtime = timeend - timebegin
print(runtime)
NPub = int(records1["Count"])
baseline = records1["IdList"]
baseline10 = baseline[0:10]
print(baseline10)
baseline100 = baseline[0:100]
print(NPub)

with open("queries.txt", "r") as f:
    for line in f:
        timebegin = datetime.now()
        handle = Entrez.esearch(db="pmc", retmax=N, term=line[:-1], sort="relevance")
        records1 = Entrez.read(handle)
        handle.close()
        timeend = datetime.now()
        runtime = timeend - timebegin
        NPub = int(records1["Count"])
        ids = records1["IdList"]
        co10 = [x for x in ids[0:10] if (x in baseline10)]
        co100 = [x for x in ids[0:100] if (x in baseline100)]
        print(line[:-1]+";"+str(len(co10))+";"+str(len(co100))+";"+str(runtime))



