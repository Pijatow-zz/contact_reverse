import os

os.system('cls')

# getting this file's folder path
path = os.path.dirname(os.path.abspath(__file__))

vcf_filepath = input('vcf file name(default: test.vcf): ')
if vcf_filepath == '':
    vcf_filepath = 'old.vcf'
read_file = open(f'{path}\{vcf_filepath}')


new_file = f'{path}\\reversed.vcf'
write_line = open(new_file, 'w')

print('---------------------------------------')


for line in read_file:
    if line.startswith('FN:'):
        parts = line.split(',')
        suffix = ''
        try:
            suffix = str(',' + parts[1].rstrip('\n'))
        except IndexError:
            pass
        thing = parts[0].rstrip('\n').split(':')
        FN = thing[1]
        reversed_FN = FN
        if len(FN.split()) == 2:
            splited = FN.split()
            reversed_FN = str(splited[1] + ' ' + splited[0])
        write_line.write(f'FN:{reversed_FN}{suffix}\n')
    else:
        write_line.write(f'{line}')

write_line.close()
