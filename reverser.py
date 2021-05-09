import os

os.system('cls')

# getting this file's folder path
path = os.path.dirname(os.path.abspath(__file__))

inp = input('vcf file name(default: test.vcf): ')

file_name = inp.split('.vcf')[0]
vcf_file_name = inp
if inp == '':
    vcf_file_name = 'test.vcf'
try :
    read_file = open(f'{path}\\{vcf_file_name}')
except:
    print('file not found')
    quit()
new_file_name = f'{path}\\{file_name}_reversed.vcf'
write_line = open(new_file_name, 'w')

print('---------------------------------------')


for line in read_file:
    if line.startswith('N:'):
        parts = line.split(';')
        last_name = parts[0] = parts[0].lstrip('N:')
        first_name = parts[1]
        middle_name = parts[2]
        prefix = parts[3]
        suffix = parts[4] = parts[4].rstrip('\n')
        reversed_ = f'N:{first_name};{last_name};{middle_name};{prefix};{suffix}\n'
        write_line.write(reversed_)
    else:
        write_line.write(line)

write_line.close()
print('DONE!\nGood Luck :)')
