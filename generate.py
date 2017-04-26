import random

def create_common_words():
    with open('common_words.txt', 'r') as c:
        with open('new_common_words.txt', 'w') as f:
            words = set(c.read().split('\n'))
            words = sorted(words)
            for word in words:
                f.write('{}\n'.format(word))


def get_random_phrases(n=300, max_size=12):
    with open('common_words.txt', 'r') as f:
        words = f.read().split('\n')
        count = 0
        while count < n:
            a = random.randint(0, len(words) - 1)
            b = random.randint(0, len(words) - 1)
            phrase = '{}{}.com'.format(words[a], words[b])
            if len(phrase) <= max_size:
                print phrase
                count += 1

get_random_phrases(450, 11)
