This isn't my project but was fun to study

# META: DOMAIN-GENERATOR

## Folder Structure

```plaintext
/Users/jasonnathan/Repos/domain-generator
├── README.md
├── common_words.txt
├── generate.py
└── seen.txt

1 directory, 4 files
```
## File: README.md

```md
# Usage
`$ python generate.py`

```

## File: generate.py

```py
import random

def create_common_words():
    with open('common_words.txt', 'r') as c:
        with open('new_common_words.txt', 'w') as f:
            words = set(c.read().split('\n'))
            words = sorted(words)
            for word in words:
                f.write('{}\n'.format(word))


def get_seen_words():
    with open('seen.txt', 'r') as f:
        return set(f.read().split('\n'))

def get_common_words():
    with open('common_words.txt', 'r') as f:
        return f.read().split('\n')

def add_seen_word(word):
    with open('seen.txt', 'a') as f:
        f.write('{}\n'.format(word))


def get_random_phrases(n=300, max_size=12):
    max_fails = 500000
    words = get_common_words()
    seen = get_seen_words()
    count = 0
    fails = 0
    while count < n and fails < max_fails:
        a = random.randint(0, len(words) - 1)
        b = random.randint(0, len(words) - 1)
        phrase = '{}{}'.format(words[a], words[b]).strip()
        if len(phrase) <= max_size and len(phrase) > 4 and phrase not in seen:
            seen.add(phrase)
            add_seen_word(phrase)
            print '{}.com'.format(phrase)
            count += 1
        else:
            fails += 1

get_random_phrases(450, 8)

```

## Git Repository

```plaintext
origin	https://github.com/cgil/domain-generator.git (fetch)
origin	https://github.com/cgil/domain-generator.git (push)
```
