import re
dna = """CGGGGCTATGCAACTGGGTCGTCACATTCCCCTTTCGATA
TTTGAGGACGTACGTACGATGCAACTCCAAAGCGGACAAA
GGATGCAACTGATGCCGTTTGACGACCTAAATCAACGGCC
AAGGATGCAACTCGACGTACGTACGAGCTGGTTCTACCTG
AATTGGTCTAAAAAGATTATAATGTCGGTCCATGCAACTT
CTGCTGTACAACTGAGATCATGCTGCATGCAACTTTCAAC
TACATGATCTTTTGATGCAACTTGGATGAGGGAATGATGC
ATGACGTACGTACGACTGACGTACCGACGCATGCAACTTC"""

def find_gc(dna):
    dna = dna.split('\n')
    liczba = 0
    seq = ''
    for x in range(0, len(dna)):
        for y in range(0, len(dna[x]) - 1):
            if dna[x][y:y+2] == "GC":
                liczba += 1
        seq +="Linia dna: " + str(x) + "  Wystapienia GC: " + str(liczba) + '\n'
        liczba = 0
    return seq

def find_g_c(dna):
    dna = dna.split('\n')
    seq = ''
    for x in range(0, len(dna)):
        indeks = 0
        m = re.search(r'(G.C|C.G)', dna[x])
        while(m != None):
            m = re.search(r'(G.C|C.G)', dna[x])
            if m!=None:
                seq += "Linia dna: " + str(x) + "  Wystapienia G*C/C*G: " + m.group() + " na pozycji " + str(m.start()) + '\n'
            else:
                seq += "Ni ma"
            indeks = m.start() +
    return seq

def find_GC_CG(dna):
    dna = dna.split('\n')
    seq = ''
    for x in range(0, len(dna)):
        liczba = re.search(r'(GC([ATGC]{1,6})CG)', dna[x])
        seq += "Linia dna: " + str(x) + "  Wystapienia GC__CG: " + str(liczba) + '\n'
    return seq

def find_cAc(dna):
    dna = dna.split('\n')
    seq = ''
    for x in range(0, len(dna)):
        liczba = re.search(r'(C(A)*C)', dna[x])
        seq += "Linia dna: " + str(x) + "  Wystapienia C{A}C: " + str(liczba) + '\n'
    return seq


if __name__ == "__main__":
    with open("wynik1.txt", 'w') as plik:
        plik.write(str(find_gc(dna)))
    with open("wynik2.txt", 'w') as plik:
        plik.write(str(find_g_c(dna)))
    with open("wynik3.txt", 'w') as plik:
        plik.write(str(find_GC_CG(dna)))
    with open("wynik4.txt", 'w') as plik:
        plik.write(str(find_cAc(dna)))

