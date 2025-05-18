dna = input("Please type in a sequence: ")

seq_list = ['']
idx = 0
for base in dna.lower():
    if base in ['a', 'c', 't', 'g']:
        seq_list[idx] += base
    else:
        idx += 1
        seq_list.append('')

mod_list = []

for i in range(len(seq_list)):
    if not seq_list[i] == '':
        mod_list.append(seq_list[i].upper())

sorted_list = sorted(mod_list, key = len, reverse = True)

print(sorted_list)
