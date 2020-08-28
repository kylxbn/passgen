# passgen

A tool for generating cryptographically secure passphrases with around 107 bits (or more) of entropy, perfectly suitable for generating extremely secure passphrases while keeping it as easy to type as possible (and if you're desperate enough, to make it easy to remember, hopefully).

## What does it output?

It outputs 6 words, separated by spaces, chosen randomly (securely) from a pool of 7776 English words (from `eff_large_wordlist.txt`), together with an 8-letter word generated randomly (securely) from the letters *a-z*, inserted between the six words in a random position. Here are 5 examples:

* could devotee ligament ldfvohip casually enzyme unfiled
* tigress victory fruit gloomy twumtyss flip query
* lueeyjvq jury pacific twice divorcee scanning ecosphere
* subzero uncurious marigold purr mbzytjbk secluded raider
* excess trapped imperfect corporate payphone quuktupb debatable

## How secure is it?

Given that it produces passphrases with around 107 bits of entropy (or more), and given that your attacker can guess 100,000,000,000,000 passphrases **per second** (which is virtually impossible for anybody to do, unless it's the NSA or something trying to guess your passphrase), it would still take them a bit more than **26 billion years** of guessing the passphrase. Please note that Earth will be obliterated by the Sun as it becomes a red giant **5 billion years** from now.

## How do I run it?

You will need to install `pyperclip` first via pip or something else, then,

just call python3

```
$ python3 passgen.py
```

It will generate a password and copy it to the clipboard.

Just paste it to use it. You might want to clear or replace your clipboard content afterwards.

You can also run the included `test.py` to generate 20 passphrases into a file called `example_passphrases.txt`