import random
import pickle
import time


class Tombola():
    def __init__(self, luckyness_maximus=2, autosave=True):
        self.lots = {}
        self.claims = {}
        self.gamblers = set()
        self.luckyness_maximus = luckyness_maximus
        self.autosave = autosave

    def __repr__(self):
        r = '{} GAMBLERS GAMBLING\n'.format(len(self.gamblers))
        if len(self.lots.keys()) > 0:
            r += 'LOTS\n'
            for lot in self.lots.keys():
                r += '\t{}\n'.format(lot)
        else:
            r += 'NO LOTS DEFINED\n'
        if len(self.claims.keys()) > 0:
            r += 'CLAIMS\n'
            for lot in self.claims.keys():
                r += '\t{} -> {}\n'.format(lot, self.claims[lot])
        else:
            r += 'NO LOTS CLAIMED\n'
        if 'name' in self.__dict__.keys():
            r += 'SAVED AS\n\t{}'.format(self.name)
        else:
            r += 'STATE NOT SAVED'
        return str(r)

    def _is_lucky(self, gambler):
        return list(
            self.claims.values()
        ).count(gambler) > self.luckyness_maximus - 1

    def save(self, name):
        self.name = name
        with open('.'.join([name, 'pkl']), 'wb') as f:
            pickle.dump(self.__dict__, f)

    def load(self, name):
        with open('.'.join([name, 'pkl']), 'rb') as f:
            self.__dict__ = pickle.load(f)

    def create_lot(self, name):
        self.lots.update({
            name: []
        })

    def update_lot(self, lot_name, gambler):
        try:
            if gambler.tombola != self:
                print('ERROR: invalid gambler')
                return
            self.lots[lot_name].append(gambler.name)
            self.gamblers.add(gambler.name)
            if hasattr(self, 'name') and self.autosave:
                self.save(self.name)
        except KeyError:
            print('ERROR: lot "{}" does not exist'.format(lot_name))

    def draw_lot(self, lot_name, suspense=5):
        if lot_name in self.claims.keys():
            print('ERROR: lot {} has been claimed by {}'.format(
                lot_name, self.claims[lot_name]))
            return
        try:
            random.shuffle(self.lots[lot_name])
            winner = None
            while winner is None:
                try:
                    winner = self.lots[lot_name].pop()
                except IndexError:
                    print('ERROR: either no gamblers or too much luck')
                    return
                if self._is_lucky(winner):
                    self.lots[lot_name] = [
                        gambler for gambler in self.lots[lot_name]
                        if gambler != winner
                    ]
                    self.gamblers.remove(winner)
                    winner = None
        except KeyError:
            print('ERROR: lot "{}" does not exist'.format(lot_name))
            return

        self.claims.update({lot_name: winner})
        del(self.lots[lot_name])

        for t in range(suspense, 0, -1):
            print('#' * t * 10)
            time.sleep(0.5)
        print('\n!! {} !!\n'.format(winner))
        for t in range(suspense + 1):
            print('#' * t * 10)

        if hasattr(self, 'name') and self.autosave:
            self.save(self.name)


class Gambler():
    def __init__(self, name, n_tickets, tombola, force=False):
        if not hasattr(tombola, 'gamblers'):
            print('ERROR: invalid tombola')
            return
        if name in tombola.gamblers and not force:
            print(
                'ERROR: gambler "{}" is already registered. Force?'.format(
                    name))
        self.tombola = tombola
        self.name = name
        self.tickets_remaining = n_tickets

    def place_tickets(self, lot_name, n=1):
        if n > self.tickets_remaining:
            print(
                'ERROR: not enough remaining tickets\n' +
                '{} tickets remain'.format(self.tickets_remaining))
            return
        try:
            for _ in range(n):
                self.tombola.update_lot(lot_name, self)
            self.tickets_remaining -= n
            print('{} tickets remain'.format(self.tickets_remaining))
        except KeyError:
            print('ERROR: lot "{}" does not exist'.format(lot_name))
