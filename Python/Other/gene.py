import re,time

start_time = time.time()

path = '/Users/redhead/Desktop/Projects/Python/Other/123.txt'

with open(path, 'r') as file:
    dna = file.read()

mrna = dna.upper().translate(str.maketrans('CGAT', 'GCUA'))
trna = mrna.translate(str.maketrans('GCUA', 'CGAU'))
anticodons = re.findall(r'\S\S\S',trna)

template = {'A':    ['GCU', 'GCC', 'GCA', 'GCG'],
            'L':	['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
            'R':	['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
            'K':	['AAA', 'AAG'],
            'N':	['AAU', 'AAC'],	
            'M':	['AUG'],
            'D':	['GAU', 'GAC'],	
            'F':	['UUU', 'UUC'],
            'C':	['UGU', 'UGC'],	
            'P':    ['CCU', 'CCC', 'CCA', 'CCG'],
            'Q':	['CAA', 'CAG'],	
            'S':	['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
            'E':	['GAA', 'GAG'],	
            'T':	['ACU', 'ACC', 'ACA', 'ACG'],
            'G':	['GGU', 'GGC', 'GGA', 'GGG'],	
            'W':	['UGG'],
            'H':	['CAU', 'CAC'],	
            'Y':	['UAU', 'UAC'],
            'I':	['AUU', 'AUC', 'AUA'],	
            'V':	['GUU', 'GUC', 'GUA', 'GUG']}

aminoacids = []

for anticodon in anticodons:
    for aminoacid, codons in template.items():
        for codon in codons:
            if anticodon in codon:
                aminoacids.append(aminoacid)

protein = ''.join(aminoacids)       

print('\nTranslated amino acid sequence is:\n')
print(f'{protein}\n')
print("--- %s seconds ---" % (time.time() - start_time))
    