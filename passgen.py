import secrets

words = []
chars = 'abcdefghijklmnopqrstuvwxyz'

with open('eff_large_wordlist.txt') as wordlist:
    for line in wordlist.readlines():
        parts = line.split('\t')
        if len(parts) > 1:
            words.append(parts[1].strip())

def generate():
    phrase = [secrets.choice(words) for i in range(6)]
    phrase.insert(secrets.randbelow(6), ''.join([secrets.choice(chars) for i in range(8)]))
    return ' '.join(phrase)

if __name__ == '__main__':
    import pyperclip
    pyperclip.copy(generate())