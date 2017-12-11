# EasternBloc Tombola super-hyper-lot-drawing-machine

you'll need Python3 installed to use the machine

1. open a console
2. type `python3`
3. use the machine

try these things

    from ebtombola import *

    tombo = Tombola()

    tombo.create_lot('soundy')

    tombo.create_lot('blinky')

    g = Gambler('greg', 4, tombo)

    g.place_tickets('soundy', 2)

    g.place_tickets('blinky', 2)

    g = Gambler('martin', 4, tombo)

    g.place_tickets('soundy', 4)

    tombo.draw_lot('soundy')

    tombo.draw_lot('blinky')

    tombo.claims
