from engine import Scene

# --- castle heist ---

approach = Scene(
    "The castle sits on a ridge above the river. Three towers, outer wall, one gate. The gate is guarded. You crouch in the treeline and consider your options.",
    [
        "Walk up to the gate and bluff your way in",
        "Circle around to the river side and look for a way up",
        "Wait until nightfall"
    ]
)

bluff = Scene(
    "You dust yourself off and walk to the gate like you belong there. The guard squints at you. 'Delivery,' you say. He looks you up and down. 'Delivery of what?'",
    [
        "'Wine for the captain's table.'",
        "'Message from the magistrate. Urgent.'",
        "Shove past him and run"
    ]
)

river = Scene(
    "The river side of the castle has no gate, but the wall is shorter here. Old drainage grates jut out above the waterline. One of them is rusted through.",
    [
        "Climb through the broken grate",
        "Scale the wall directly"
    ]
)

nightfall = Scene(
    "You wait. Hours pass. The sun drops behind the ridge and the torches go up on the walls. Fewer guards on the night rotation. The gate guard yawns.",
    [
        "Approach the gate now",
        "Circle to the river side under cover of dark"
    ]
)

# bluff branches
wine_bluff = Scene(
    "The guard stares. Then he steps aside. 'Kitchen entrance, left corridor. Don't let the steward catch you without a cart.' You're in.",
    [
        "Head for the kitchen and look for a way downstairs",
        "Slip into the first hallway you see"
    ]
)

message_bluff = Scene(
    "The guard waves you through without a second look. Magistrate business is above his pay grade. You pass through the courtyard into the main hall.",
    [
        "Ask a servant where the castellan's office is",
        "Find a staircase heading down"
    ]
)

shove = Scene(
    "You knock him sideways and sprint through the gate. Shouts behind you. You have seconds before the whole garrison knows you're here.",
    [
        "Duck into the nearest doorway",
        "Keep running toward the inner keep"
    ]
)

# river branch
grate = Scene(
    "You squeeze through the rusted grate into a drainage tunnel. It stinks. The tunnel slopes upward and forks — left toward noise, right toward silence.",
    [
        "Go left, toward the noise",
        "Go right, toward the silence"
    ]
)

wall_climb = Scene(
    "You get halfway up before a loose stone gives. You catch yourself, but the stone hits the water below. Loud. A torch appears on the wall above. 'Who's there?'",
    [
        "Freeze and hope the dark hides you",
        "Drop back down and try the grate instead"
    ]
)

# convergence — multiple paths lead here
basement_hall = Scene(
    "You're in a stone corridor below the castle. Cold air. No torches, but you can see a faint glow ahead. The walls are older down here — this part of the castle predates the rest.",
    [
        "Follow the glow",
        "Check the side passages first"
    ]
)

vault_door = Scene(
    "The glow is a lantern hung beside a heavy iron door. The lock is old but solid. No guards — they trust the lock.",
    [
        "Pick the lock",
        "Look for a key nearby",
        "Force it"
    ]
)

# vault outcomes
pick_lock = Scene(
    "It takes a while. Your hands are steady. The last tumbler clicks and the door swings inward. The vault is small — one table, one chest, and a rack of sealed documents.",
    [
        "Open the chest",
        "Grab the documents",
        "Take everything you can carry"
    ]
)

find_key = Scene(
    "You check behind the lantern. Under a loose stone in the wall, a key. Of course. You turn it in the lock and the door opens without complaint.",
    [
        "Open the chest",
        "Grab the documents",
        "Take everything you can carry"
    ]
)

force_it = Scene(
    "You slam your shoulder into the door. It doesn't move. You try again. Something cracks — your shoulder, not the door. This isn't working.",
    [
        "Try picking the lock instead",
        "Look for a key"
    ]
)

# endgame
take_chest = Scene(
    "Gold coins. Not a fortune, but enough. You fill your pockets and your bag. Heavy now.",
    [
        "Find your way out"
    ]
)

take_docs = Scene(
    "Letters with noble seals. Trade agreements. A map with locations marked in red. This is worth more than gold to the right buyer.",
    [
        "Find your way out"
    ]
)

take_all = Scene(
    "You stuff documents in your shirt, gold in your bag, and a jeweled dagger from the bottom of the chest in your belt. Greedy, but thorough.",
    [
        "Find your way out"
    ]
)

# escape is None — ends the game
escape = None


# --- wiring ---

# approach
approach.add_next(1, bluff)
approach.add_next(2, river)
approach.add_next(3, nightfall)

# bluff
bluff.add_next(1, wine_bluff)
bluff.add_next(2, message_bluff)
bluff.add_next(3, shove)

# nightfall loops back into existing branches
nightfall.add_next(1, bluff)
nightfall.add_next(2, river)

# river
river.add_next(1, grate)
river.add_next(2, wall_climb)

# wall_climb
wall_climb.add_next(1, basement_hall)  # freeze works
wall_climb.add_next(2, grate)

# all indoor paths converge on basement_hall
wine_bluff.add_next(1, basement_hall)
wine_bluff.add_next(2, basement_hall)
message_bluff.add_next(1, basement_hall)
message_bluff.add_next(2, basement_hall)
shove.add_next(1, basement_hall)
shove.add_next(2, basement_hall)
grate.add_next(1, basement_hall)
grate.add_next(2, basement_hall)

# basement to vault
basement_hall.add_next(1, vault_door)
basement_hall.add_next(2, vault_door)

# vault door
vault_door.add_next(1, pick_lock)
vault_door.add_next(2, find_key)
vault_door.add_next(3, force_it)

# force_it loops back
force_it.add_next(1, pick_lock)
force_it.add_next(2, find_key)

# loot choices
pick_lock.add_next(1, take_chest)
pick_lock.add_next(2, take_docs)
pick_lock.add_next(3, take_all)
find_key.add_next(1, take_chest)
find_key.add_next(2, take_docs)
find_key.add_next(3, take_all)

# escape — None ends the loop
take_chest.add_next(1, escape)
take_docs.add_next(1, escape)
take_all.add_next(1, escape)