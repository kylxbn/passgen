import passgen

print('Generating.')

with open('example_passphrases.txt', 'w') as output:
    for i in range(20):
        output.write(passgen.generate() + '\n')

print('Done.')