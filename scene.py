from engine import Scene, ChallengeScene, LootScene


 
# FAIL STATES
 

fail_caught_gate = Scene(
    "You make it thirty paces before something heavy hits the back of your knees. The cobblestones come up fast. Two guards pin you before you can roll over. One of them wrenches your arms behind your back. The other calls for the captain.\n\nYou don't see the castle again. Not from the inside, anyway.\n\n--- CAUGHT ---",
    ["Start over"]
)

fail_guards_tunnel = Scene(
    "The noise was boots. Six of them, three guards, coming around the bend with torches and polearms. The tunnel is too narrow to run. Too narrow to fight. The first one grabs you by the collar before you even finish turning around.\n\n--- CAUGHT ---",
    ["Start over"]
)

fail_wall_spotted = Scene(
    "The torch sweeps down. You're pressed flat against the stone, fingers white on a crack in the masonry. The light finds you anyway.\n\n\"Climber on the east wall!\"\n\nAn arrow punches into the stone two inches from your hand. You drop. The river catches you—cold, fast, and deep enough to pull you under before you find the bank.\n\n--- DROWNED ---",
    ["Start over"]
)

fail_force_vault = Scene(
    "The third hit echoes down the corridor like a bell. You hear it come back to you, and then you hear it keep going—up through the stone, into the floors above.\n\nBoots. Lots of them. Getting closer.\n\nYou turn to run. The corridor behind you is already lit with torchlight.\n\n--- CAUGHT ---",
    ["Start over"]
)

fail_gate_escape_heavy = Scene(
    "You make it to the gate at a half-jog. The bag drags on your shoulder, the gold shifting with every step. The guard sees you before you see him. You try to run.\n\nYou can't. Not with this weight.\n\nHe doesn't even draw his weapon. Just steps in front of you and waits.\n\n--- CAUGHT ---",
    ["Start over"]
)

fail_wall_escape_heavy = Scene(
    "You hook your fingers into the first gap in the stone and pull. The bag swings. The gold inside shifts and the strap cuts into your shoulder. You get one arm over the top of the wall before the weight drags you back down.\n\nYou land on your back. The bag splits. Coins scatter across the flagstones, ringing off the stone in the dark.\n\nThe guards find you sitting in a pile of your own loot.\n\n--- CAUGHT ---",
    ["Start over"]
)


 
# ENDINGS
 

end_gold = Scene(
    "Dawn hasn't broken yet when you reach the treeline. Your pockets are heavy. Mira. A lot of it—enough to disappear for a year, maybe two. No name attached. No trail.\n\nYou don't look back at the castle. There's nothing there for you anymore.\n\n--- ESCAPED WITH THE GOLD ---",
    ["Start over"]
)

end_docs = Scene(
    "The documents sit inside your shirt, pressed flat against your ribs. Trade agreements. Noble seals. A map with locations marked in red ink that hasn't dried yet.\n\nGold buys a year. Information buys leverage. And leverage—that buys whatever you want.\n\nYou disappear into the treeline before the sun comes up.\n\n--- ESCAPED WITH THE DOCUMENTS ---",
    ["Start over"]
)

end_all_drainage = Scene(
    "The drainage tunnel is tighter than you remember. The bag catches on every edge, every rusted bolt. You drag it through standing water that soaks through to your knees. It takes twice as long as it should.\n\nBut you come out the other side with everything. Gold in the bag. Documents in your shirt. Dagger in your belt. Wet, stinking, and rich.\n\nThe river carries the smell away. The treeline swallows the rest.\n\n--- ESCAPED WITH EVERYTHING ---",
    ["Start over"]
)

end_gate_bluff = Scene(
    "The night guard is half-asleep. You walk past him with your chin up and your hands steady. He doesn't even look at your face.\n\nThe road out of the castle is quiet. The moon is behind the clouds. By the time anyone checks the vault, you'll be three towns away.\n\n--- ESCAPED ---",
    ["Start over"]
)

end_wall_escape = Scene(
    "The wall is shorter on this side. You find a foothold, then another. Your arms burn but the top comes fast. You swing a leg over and drop into the grass on the other side.\n\nThe river is fifty paces ahead. Beyond it, the treeline. Beyond that—wherever you want.\n\n--- ESCAPED ---",
    ["Start over"]
)

end_drainage_escape = Scene(
    "The drainage grate is right where you left it. You squeeze through, boots hitting the shallow water on the other side. The river is cold and knee-deep. You wade downstream until the castle is a dark shape against the sky behind you.\n\nThe bag is light on your shoulder. Your pockets are full. That's enough.\n\n--- ESCAPED ---",
    ["Start over"]
)


 
# ESCAPE SEQUENCES
 

escape_light = Scene(
    "The corridor behind you is still dark. Still quiet. But that won't last—someone checks the vault eventually. You need to move.\n\nThree ways out. The drainage tunnel on the river side. The main gate. Or straight over the wall.",
    [
        "Back through the drainage tunnel",
        "Walk out the gate",
        "Over the wall"
    ]
)

escape_heavy = Scene(
    "The bag bites into your shoulder. Gold is heavier than it looks. Every step clinks, and you catch yourself adjusting the strap every few paces.\n\nThree ways out. The drainage tunnel. The gate. Over the wall. But you're slow now. Whatever you pick, speed isn't on your side.",
    [
        "Back through the drainage tunnel",
        "Walk out the gate",
        "Over the wall"
    ]
)


 
# VAULT
 

vault_interior = Scene(
    "The vault is smaller than you expected. One table, one iron chest, and a rack of sealed documents on the far wall. A thin layer of dust on everything except the chest. Someone's been here recently.\n\nYou don't have much time.",
    [
        "Open the chest",
        "Take the documents",
        "Take everything you can carry"
    ]
)

pick_lock = Scene(
    "You kneel in front of the door. The lock is old—heavy iron, four tumblers. Your picks find the first one fast. The second takes longer. The third sticks.\n\nYou close your eyes. Feel the tension. There.\n\nThe fourth clicks into place and the bolt slides back. The door swings inward without a sound.",
    [
        "Enter the vault"
    ]
)

find_key = Scene(
    "You run your fingers along the wall beside the door. Behind the lantern hook—nothing. Under the loose stone at knee height—a key. Iron, heavy, coated in dust.\n\nIt turns in the lock on the first try. The bolt slides and the door opens.",
    [
        "Enter the vault"
    ]
)

vault_door = Scene(
    "The glow is a single lantern, hung on a hook beside a heavy iron door. Old lock. Solid. No guards down here—they trust the iron and the stone.\n\nThe door has no handle on the outside. Just the lock and a pull-ring.",
    [
        "Pick the lock",
        "Look for a key nearby",
        "Force it open"
    ]
)


 
# BASEMENT (CONVERGENCE POINT)
 

supply_room = Scene(
    "The side passage opens into a storage room. Crates of salt. Dried meat on hooks. A rack of torches, most of them spent. Nothing useful—but through the back wall, you can see another corridor. Faint light at the far end.",
    [
        "Follow the light"
    ]
)

basement_hall = Scene(
    "Stone corridor. No torches, but a faint glow somewhere ahead. The walls down here are rougher than the floors above—older stone, older mortar. This part of the castle was here first.\n\nThe air is cold. Your breath doesn't quite fog, but it's close.",
    [
        "Follow the glow",
        "Check the side passages first"
    ]
)


 
# INSIDE THE CASTLE (BLUFF PATHS)
 

kitchen_path = Scene(
    "The kitchen is chaos. Steam, shouting, the clang of iron pots. Nobody looks at you twice. A servant brushes past with a tray of bread. You spot a narrow staircase in the back corner, leading down.\n\nThe smell of roasting meat follows you for the first dozen steps. Then it's just damp stone.",
    [
        "Head down the stairs"
    ]
)

courtyard_path = Scene(
    "The main hall is wide and cold. Tapestries on the walls. A fireplace large enough to stand in, unlit. Two corridors branch off—one toward the barracks, the other deeper into the keep.\n\nA servant passes. You ask about the castellan's office. She points left without stopping. You go right.\n\nThe staircase down is behind a door that doesn't lock.",
    [
        "Head down the stairs"
    ]
)

shove_path = Scene(
    "You knock him sideways and sprint through the gate. Shouts behind you—two voices, then three. The courtyard is wide and open. Bad ground for running.\n\nTo your left, a doorway. To your right, the inner keep. The keep is further but has more places to hide. The doorway is close but you don't know what's on the other side.",
    [
        "Duck into the doorway",
        "Keep running toward the inner keep"
    ]
)

shove_doorway = Scene(
    "You throw yourself through the doorway and pull the door shut. A storage closet. Brooms, buckets, the sharp smell of lye. You press your back against the door and hold your breath.\n\nBoots pass outside. One pair, then another. Shouting, but moving away from you.\n\nYou wait. One minute. Two. Five.\n\nThe shouting dies. You crack the door. The courtyard is empty. A staircase across the yard leads down.",
    [
        "Cross the courtyard and head down"
    ]
)


 
# RIVER PATH
 

grate = Scene(
    "The grate comes away in pieces. Rust and river water have done most of the work for you. You squeeze through sideways—it scrapes your shoulders, catches on your belt—and drop into a drainage tunnel.\n\nStanding water to your ankles. The smell is exactly what you'd expect. The tunnel slopes upward and forks. Left, you hear noise—voices, maybe boots. Right, silence.",
    [
        "Go left, toward the noise",
        "Go right, toward the silence"
    ]
)

wall_climb = Scene(
    "You find a foothold. Then another. The stone is slick with river spray but the mortar gaps are deep enough for fingers. You're halfway up when a loose stone shifts under your boot.\n\nIt falls. Hits the water below. Loud.\n\nA torch appears on the wall above. You flatten yourself against the stone.",
    [
        "Freeze and wait",
        "Drop back down and try the grate"
    ]
)

wall_freeze = Scene(
    "You don't move. Don't breathe. The torch sweeps left, then right. A long pause. Then the guard mutters something and the light pulls back.\n\nYou wait another thirty seconds before moving. The rest of the climb is quiet. You swing over the top and drop into a narrow walkway along the inner wall.\n\nA service hatch in the floor leads down into darkness.",
    [
        "Drop through the hatch"
    ]
)

river = Scene(
    "The river side of the castle has no gate. The wall is shorter here—maybe twelve, fifteen feet—and old drainage grates jut out above the waterline. One of them is rusted through, the bars bent outward.\n\nThe wall itself has cracks. Enough for fingers and boot-tips, if you trust your grip.",
    [
        "Climb through the broken grate",
        "Scale the wall"
    ]
)


 
# NIGHTFALL
 

nightfall = Scene(
    "You wait. The sun drops behind the ridge. Torches go up on the walls, but fewer than you expected. The night rotation is thin—four guards on the wall, one at the gate. The gate guard sits on a stool and yawns.\n\nThe darkness is good cover. You have two options.",
    [
        "Approach the gate",
        "Circle to the river side"
    ]
)

nightfall_gate = Scene(
    "The gate guard is half-asleep. His chin dips, catches, dips again. A lantern burns low beside him. You step out of the treeline.\n\nHe jerks awake when you're ten paces out. \"Who goes—\" He squints. You can see him deciding whether you're worth the effort.\n\n\"Delivery,\" you say. \"Late shipment. The steward's expecting it.\"",
    [
        "\"Wine for the captain's table. Got held up on the road.\"",
        "\"Message from the magistrate. It's urgent.\""
    ]
)


 
# BLUFF
 

wine_bluff = Scene(
    "The guard stares at you. Then at the road behind you. Then back at you.\n\n\"Where's the cart?\"\n\n\"Stolen. Bandits on the north road. I carried what I could.\" You hold up empty hands. \"The steward can verify.\"\n\nHe steps aside. \"Kitchen entrance. Left corridor. And don't let the steward catch you without paperwork.\"",
    [
        "Head for the kitchen"
    ]
)

message_bluff = Scene(
    "The guard straightens. Magistrate business is above his rank and he knows it. He waves you through without checking your hands, your pockets, or your face.\n\nThe courtyard opens up in front of you—wide, torchlit, quieter than you expected.",
    [
        "Cross the courtyard and find a way downstairs"
    ]
)

bluff = Scene(
    "You brush yourself off and walk to the gate. Shoulders back. Steady pace. The guard watches you approach. He's young—maybe twenty—with a short spear and a bored expression that sharpens when you get close.\n\n\"State your business.\"",
    [
        "\"Wine for the captain's table.\"",
        "\"Message from the magistrate. Urgent.\"",
        "Shove past him and run"
    ]
)


 
# APPROACH (START)
 

approach = Scene(
    "The castle sits on a ridge above the river. Three towers, an outer wall, one gate. Torchlight flickers along the battlements. The gate is guarded—one man visible, probably more behind the wall.\n\nYou crouch in the treeline and study it. The stone is old but maintained. No siege damage. No easy way in from the front.\n\nThe river curves around the eastern side. The wall is shorter there.",
    [
        "Walk up to the gate and bluff your way in",
        "Circle around to the river side",
        "Wait until nightfall"
    ]
)


 
# WIRING
 

# approach
approach.add_next(1, bluff)
approach.add_next(2, river)
approach.add_next(3, nightfall)

# bluff
bluff.add_next(1, wine_bluff)
bluff.add_next(2, message_bluff)
bluff.add_next(3, shove_path)

# bluff results
wine_bluff.add_next(1, kitchen_path)
message_bluff.add_next(1, courtyard_path)
shove_path.add_next(1, shove_doorway)
shove_path.add_next(2, fail_caught_gate)

# indoor paths to basement
kitchen_path.add_next(1, basement_hall)
courtyard_path.add_next(1, basement_hall)
shove_doorway.add_next(1, basement_hall)

# nightfall
nightfall.add_next(1, nightfall_gate)
nightfall.add_next(2, river)

# nightfall gate bluffs
nightfall_gate.add_next(1, wine_bluff)
nightfall_gate.add_next(2, message_bluff)

# river
river.add_next(1, grate)
river.add_next(2, wall_climb)

# grate
grate.add_next(1, fail_guards_tunnel)
grate.add_next(2, basement_hall)

# wall climb
wall_climb.add_next(1, wall_freeze)
wall_climb.add_next(2, grate)

# wall freeze to basement
wall_freeze.add_next(1, basement_hall)

# basement
basement_hall.add_next(1, vault_door)
basement_hall.add_next(2, supply_room)

# supply room leads to vault
supply_room.add_next(1, vault_door)

# vault door
vault_door.add_next(1, pick_lock)
vault_door.add_next(2, find_key)
vault_door.add_next(3, fail_force_vault)

# lock/key to vault interior
pick_lock.add_next(1, vault_interior)
find_key.add_next(1, vault_interior)

# vault choices
vault_interior.add_next(1, escape_light)
vault_interior.add_next(2, escape_light)
vault_interior.add_next(3, escape_heavy)

# escape light (gold or docs)
escape_light.add_next(1, end_drainage_escape)
escape_light.add_next(2, end_gate_bluff)
escape_light.add_next(3, end_wall_escape)

# escape heavy (took everything)
escape_heavy.add_next(1, end_all_drainage)
escape_heavy.add_next(2, fail_gate_escape_heavy)
escape_heavy.add_next(3, fail_wall_escape_heavy)

# all fail states and endings loop back to approach
fail_caught_gate.add_next(1, approach)
fail_guards_tunnel.add_next(1, approach)
fail_wall_spotted.add_next(1, approach)
fail_force_vault.add_next(1, approach)
fail_gate_escape_heavy.add_next(1, approach)
fail_wall_escape_heavy.add_next(1, approach)
end_gold.add_next(1, approach)
end_docs.add_next(1, approach)
end_all_drainage.add_next(1, approach)
end_gate_bluff.add_next(1, approach)
end_wall_escape.add_next(1, approach)
end_drainage_escape.add_next(1, approach)
