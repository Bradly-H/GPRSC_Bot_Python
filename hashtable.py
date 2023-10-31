class HashTable(object):
    def __init__(self, size, mtf):
        self.move_front = mtf
        self.salt = 0x9846e4f157fe8840
        self.size = size
        self.n_hits = 0
        self.n_misses = 0
        self.n_keys = 0
        self.dictionary = {}
        self.NOT_IN_TABLE = -1
        self.NO_NEWSPEAK = -2

    def size(self):
        return self.size

    def lookup(self, oldspeak):
        # no links examined since no linked list
        return_val = self.dictionary.get(oldspeak, self.NOT_IN_TABLE)
        if return_val == self.NOT_IN_TABLE:
            self.n_misses += 1
        else:
            self.n_hits += 1
        return return_val

    def insert(self, oldspeak, newspeak=-2):
        if self.dictionary.get(oldspeak, self.NOT_IN_TABLE) == self.NOT_IN_TABLE:
            self.dictionary[oldspeak] = newspeak
        self.n_keys += 1

    def __repr__(self):
        pass

    def stats(self):
        return [self.n_keys, self.n_hits, self.n_misses]