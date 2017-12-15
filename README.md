# EasternBloc Tombola super-hyper-lot-drawing-machine

you'll need Python3 installed to use the machine

1. open a terminal window and navigate to the source code's directory
2. type `python3`
3. import the module by typing `from ebtombola import *`
4. use the machine

## try these things

### creating a tombola and adding lots

create a tombola: `tombola = Tombola()` (you only need to do this once!)

create a new lot: `tombola.create_lot('blinky')` (where blinky is the name of your new lot! wrapped in 's)

### creating gamblers and placing bets on lots

create a gambler: `gambler = Gambler('aname', 10, tombola)`, where:

- aname is the name of the gambler (it has to be unique) wrapped in 's,
- 10 is the number of tickets they purchased,
- tombola is the `tombola` instance you created above.

place a gambler's tickets: `gambler.place_tickets('blinky', 4)`, where:

- blinky is the name of the lot the gambler is betting on, wrapped in 's,
- 4 is the number of tickets they are placing

if a gambler decides to buy new tickets after having already placed tickets earlier, you'll have to skip the duplicates validation step by adding a `force` parameter like this: `gambler = Gambler('aname', 5, tombola, force=True)`. You can then proceed to place the tickets as you did the first time.

### drawing lots

draw lots and find a winner: `tombola.draw_lot('blinky')`

### saving and loading the tombola's state

you can save the state of a tombola by typing `tombola.save('aname')` (where aname is the name you want to save it under)

you can load a previously saved tombola by typing `tombola.load('aname')` (where aname is the name you gave the saved state earlier)

by default, Tombola instances are set to autosave each time there is a change in their state *after* they've been saved at least once. To change this default autosaving behavior so that saving needs to be done manually: `tombola.autosave = False`

### other things

you can always check on the state of a Tombola by simply typing `tombola`

you can see the lots and the gamblers that have bet on each: `tombola.lots`

you can see the claims (winners) by typing `tombola.claims`

you can see which gamblers have yet to claim a prize with `tombola.gamblers`

you can find out what lots have not been bet on by using `tombola.leftover_lots()`

by default, gamblers can win a maximum of 2 lots. To change this number to 3 for example, use `tombola.luckyness_maximus = 3`

if the default lot drawing suspense level of 5 is too much to handle, you can change it with `tombola.draw_lot('blinky', suspense=3)`
