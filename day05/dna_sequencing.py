import sys

dna = sys.argv[1] # this is the entered sequence

seq_list = ['']
idx = 0
for base in dna.lower():
    if base == 'x':
        idx += 1
        seq_list.append('')
    else:
        seq_list[idx] += base
        

mod_list = []

for i in range(len(seq_list)):
    if not seq_list[i] == '':
        mod_list.append(seq_list[i].upper())

sorted_list = sorted(mod_list, key = len, reverse = True)

print(sorted_list)
