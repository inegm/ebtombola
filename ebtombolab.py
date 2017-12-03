import random


class Tombolab():
    def __init__(self, luckyness_maximus=2):
        self.lots = {}
        self.claims = {}
        self.gamblers = []
        self.luckyness_maximus = luckyness_maximus

    def _is_lucky(self, gambler):
        return list(
            self.claims.values()
        ).count(gambler) > self.luckyness_maximus

    def create_lot(self, name):
        self.lots.update({
            name: []
        })

    def update_lot(self, lot_name, gambler):
        try:
            self.lots[lot_name].append(gambler)
        except KeyError:
            raise KeyError('lot "{}" does not exist'.format(lot_name))

    def draw_lot(self, lot_name):
        if lot_name in self.claims.keys():
            raise ValueError('lot {} has been claimed by {}'.format(
                lot_name, self.claims[lot_name]))
        try:
            random.shuffle(self.lots[lot_name])
            winner = None
            while winner is None:
                try:
                    winner = self.lots[lot_name].pop()
                except IndexError:
                    print('either no gamblers or too much luck')
                if self._is_lucky(winner):
                    winner = None
        except KeyError:
            raise KeyError('lot "{}" does not exist'.format(lot_name))

        self.claims.update({lot_name: winner})

        return winner


class Gambler():
    def __init__(self, name, n_tickets, tombolab, force=False):
        if name in tombolab.gamblers and not force:
            raise ValueError(
                'gambler "{}" is already registered. Force ?'.format(name))
        self.tombolab = tombolab
        self.name = name
        self.tickets_remaining = n_tickets

    def place_tickets(self, lot_name, n=1):
        if n > self.tickets_remaining:
            print('not enough remaining tickets\n{} tickets remain'.format(
                self.tickets_remaining))
            return
        try:
            for _ in range(n):
                self.tombolab.update_lot(lot_name, self.name)
            self.tickets_remaining -= n
            print('{} ticket(s) remain'.format(self.tickets_remaining))
        except KeyError:
            raise KeyError('lot "{}" does not exist'.format(lot_name))
