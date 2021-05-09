import os

os.system('cls')

# getting this file's folder path
root_path = os.path.dirname(os.path.abspath(__file__))

read_vcf_input = input('Enter the vcf file\'s name(default: contacts.vcf): ')
if not read_vcf_input.lower().strip():
    read_vcf_input = 'contacts.vcf'
read_vcf = open(read_vcf_input)

read_vcf_name = read_vcf_input.split('.vcf')[-2]
write_vcf_name = f'{read_vcf_name}_reversed.vcf'
write_vcf = open(write_vcf_name, 'w')


print('---------------------------------------')

for line in read_vcf:
    if line.startswith('N:'):
        parts = line.split(';')
        last_name = parts[0] = parts[0].lstrip('N:')
        first_name = parts[1]
        middle_name = parts[2]
        prefix = parts[3]
        suffix = parts[4] = parts[4].rstrip('\n')
        if first_name and last_name:
            reversed_ = f'N:{first_name};{last_name};{middle_name};{prefix};{suffix}\n'
            write_vcf.write(reversed_)
        else:
            write_vcf.write(line)
        print(last_name)
    else:
        write_vcf.write(line)

write_vcf.close()
print('DONE!\nGood Luck :)')
