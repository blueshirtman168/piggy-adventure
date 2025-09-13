
import os, json
import streamlit as st

st.set_page_config(page_title="Piggy Pig — Dynamic Buffet Adventure", page_icon="🐷", layout="centered")


DISH_BY_DOMINANT = {
    "adventurous": "bolognese",
    "comfort": "carbonara",
    "playful": "indomie",
    "reflective": "ochazuke",
}

PAIR_TO_DISH = {
    tuple(sorted(["adventurous","reflective"])): "aglio",
    tuple(sorted(["comfort","reflective"])): "baked_fusilli",
    tuple(sorted(["comfort","adventurous"])): "curry",
    tuple(sorted(["playful","reflective"])): "japchae",
}


TRAITS = ["adventurous","comfort","playful","reflective"]

def img_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), "images", filename)

SCENES = {'start': {'title': '🌅 Dawn Over Aotearoa', 'img': 'start.png', 'text': 'The first light spills across hills, sea, forest, and snow. Piggy Pig twitches her ears, ready to roam. Where will her hooves take her first?', 'choices': [{'label': '🌾 Swaying wheat of Waikato', 'next': 'farm_meadow', 'traits': {'comfort': 1}}, {'label': '🏖 Shells along a Coromandel beach', 'next': 'coast_shells', 'traits': {'adventurous': 1}}, {'label': '🌲 Misty Fiordland track', 'next': 'forest_track', 'traits': {'reflective': 1}}, {'label': '🏔 Lantern on an alpine path', 'next': 'alpine_lantern', 'traits': {'playful': 1}}]}, 'farm_meadow': {'title': 'Waikato Meadow Whispers', 'img': 'farm_meadow.png', 'text': 'Golden heads of wheat brush Piggy’s flanks; larks spiral up singing. A curious calf leans on the fence, and distant bells clink.', 'choices': [{'label': 'Chase the calf in gentle circles', 'next': 'barn_ribbons', 'traits': {'playful': 1}}, {'label': 'Nuzzle the calf toward the barn', 'next': 'barn_hay', 'traits': {'comfort': 1}}, {'label': 'Stand still and breathe the warm air', 'next': 'storm_rolls', 'traits': {'reflective': 1}}]}, 'barn_ribbons': {'title': 'Ribbons & Giggling', 'img': 'barn_ribbons.png', 'text': 'Children burst in with paper crowns; Piggy’s ears are quickly ribboned. Someone draws stars on her snout with chalk.', 'choices': [{'label': 'Twirl and show off your new crown', 'next': 'storm_rolls', 'traits': {'playful': 1}}, {'label': 'Guide the shy calf toward soft straw', 'next': 'barn_hay', 'traits': {'comfort': 1}}]}, 'barn_hay': {'title': 'Hay Fort Kingdom', 'img': 'barn_hay.png', 'text': 'Hay bales become castles, tunnels, and thrones. Dust glitters in slants of light; the barn smells like sunshine and time.', 'choices': [{'label': 'Burrow into the cozy straw', 'next': 'porch_light', 'traits': {'comfort': 1}}, {'label': 'Sneak to the loft and peek at the fields', 'next': 'storm_rolls', 'traits': {'reflective': 1}}]}, 'storm_rolls': {'title': 'Bruised Sky, Silver Rain', 'img': 'storm_rolls.png', 'text': 'Thunder mutters over the hills; rain strings hang from the rafters. Cows low; a gate bangs. The farmer’s wife waves from the house.', 'choices': [{'label': 'Dash outside, stomp joyous puddles', 'next': 'porch_light', 'traits': {'playful': 1}}, {'label': 'Herd the calves deeper into shelter', 'next': 'porch_light', 'traits': {'comfort': 1}}, {'label': 'Watch lightning from the loft window', 'next': 'porch_light', 'traits': {'reflective': 1}}]}, 'porch_light': {'title': 'Warm Porch Beacon', 'img': 'porch_light.png', 'text': 'Lantern glow spills onto wet boards; steam fogs the windows. Inside: laughter, blankets, and clinking plates.', 'choices': [{'label': 'Trot inside and curl by the fire', 'next': 'fireside_stories', 'traits': {'comfort': 1}}, {'label': 'Peer around the kitchen, nose twitching', 'next': 'kitchen_mischief', 'traits': {'playful': 1}}, {'label': 'Listen to rain on the roof awhile', 'next': 'fireside_stories', 'traits': {'reflective': 1}}]}, 'fireside_stories': {'title': 'Fireside Stories', 'img': 'fireside_stories.png', 'text': 'Maps and photos spread across the table. The children argue about the best place in New Zealand for a grand adventure.', 'choices': [{'label': 'Point a hoof at the coast map', 'next': 'coast_shells', 'traits': {'adventurous': 1}}, {'label': 'Point a hoof at the forest map', 'next': 'forest_track', 'traits': {'reflective': 1}}, {'label': 'Yawn dramatically and flop over', 'next': 'kitchen_mischief', 'traits': {'playful': 1}}]}, 'kitchen_mischief': {'title': 'Kitchen Mischief', 'img': 'kitchen_mischief.png', 'text': 'Piggy finds jars, baskets, and a loyal family dog. Flour dusts the air like snow as she sniffs a little too enthusiastically.', 'choices': [{'label': 'Make flour ‘hoofprints’ on the tiles', 'next': 'children_camp', 'traits': {'playful': 1}}, {'label': 'Let the dog lick flour off your snout', 'next': 'children_camp', 'traits': {'comfort': 1}}, {'label': 'Stand still, savoring the kitchen warmth', 'next': 'children_camp', 'traits': {'reflective': 1}}]}, 'coast_shells': {'title': 'Shells & Shanties', 'img': 'coast_shells.png', 'text': 'Shy crabs skitter, gulls swoop. A fisherman hums while mending nets; stormclouds brew far out at sea.', 'choices': [{'label': 'Race the tide and splash the foam', 'next': 'storm_hut', 'traits': {'adventurous': 1}}, {'label': 'Collect spiral shells for a necklace', 'next': 'storm_hut', 'traits': {'playful': 1}}, {'label': 'Sit beside the fisherman and listen', 'next': 'storm_hut', 'traits': {'reflective': 1}}]}, 'storm_hut': {'title': 'Shack in the Squall', 'img': 'storm_hut.png', 'text': 'Wind slaps the walls; a tiny window rattles. Inside, card players cheer as lanterns flicker.', 'choices': [{'label': 'Join the card table with a proud oink', 'next': 'cliff_chase', 'traits': {'playful': 1}}, {'label': 'Curl up under the bench till it eases', 'next': 'bonfire_village', 'traits': {'comfort': 1}}, {'label': 'Watch the horizon through rain', 'next': 'cliff_chase', 'traits': {'adventurous': 1}}]}, 'cliff_chase': {'title': 'Kea on the Cliffs', 'img': 'cliff_chase.png', 'text': 'A cheeky kea steals a red ribbon and flaps toward the headland; the sky tears open with light.', 'choices': [{'label': 'Chase the kea laughing', 'next': 'bonfire_village', 'traits': {'playful': 1}}, {'label': 'Turn back before the drop-offs', 'next': 'bonfire_village', 'traits': {'reflective': 1}}]}, 'bonfire_village': {'title': 'Lanterns & Bonfire', 'img': 'bonfire_village.png', 'text': 'The squall passes. Villagers sing around a bonfire, lanterns strung like moons.', 'choices': [{'label': 'Dance clumsily with the crowd', 'next': 'forest_track', 'traits': {'playful': 1}}, {'label': 'Sit and watch sparks rise into night', 'next': 'forest_track', 'traits': {'reflective': 1}}, {'label': 'Wander toward the dark treeline', 'next': 'forest_track', 'traits': {'adventurous': 1}}]}, 'forest_track': {'title': 'Fernsong Track', 'img': 'forest_track.png', 'text': 'A cool hush under silver ferns; water chatters somewhere ahead. Glowworms might be hiding in damp hollows.', 'choices': [{'label': 'Follow the chatter to a waterfall', 'next': 'glow_cave', 'traits': {'reflective': 1}}, {'label': 'Scramble up a mossy slope', 'next': 'glow_cave', 'traits': {'adventurous': 1}}, {'label': 'Hum and trot in rhythm with the forest', 'next': 'glow_cave', 'traits': {'playful': 1}}]}, 'glow_cave': {'title': 'Glowworm Grotto', 'img': 'glow_cave.png', 'text': 'The ceiling becomes a star sea; a gentle draft smells like stone and rain. In one shadow, a watchful presence.', 'choices': [{'label': 'Bow to the unseen guardian', 'next': 'wanderers_camp', 'traits': {'reflective': 1}}, {'label': 'Snort bravely and explore deeper', 'next': 'wanderers_camp', 'traits': {'adventurous': 1}}, {'label': 'Spin slowly beneath the glow', 'next': 'wanderers_camp', 'traits': {'playful': 1}}]}, 'wanderers_camp': {'title': 'Wanderers’ Circle', 'img': 'wanderers_camp.png', 'text': 'Travelers share songs by a small fire. Someone strums a guitar; a fox-like shadow stays at the treeline, listening.', 'choices': [{'label': 'Settle in and swap stories', 'next': 'alpine_lantern', 'traits': {'comfort': 1}}, {'label': 'Ask for directions to a mountain hut', 'next': 'alpine_lantern', 'traits': {'adventurous': 1}}, {'label': 'Sit quietly to watch the sparks', 'next': 'alpine_lantern', 'traits': {'reflective': 1}}]}, 'alpine_lantern': {'title': 'Lantern on the Ridge', 'img': 'alpine_lantern.png', 'text': 'The air thins. A warm window glows ahead; snowflakes tease Piggy’s eyelashes.', 'choices': [{'label': 'Trot straight to the hut for warmth', 'next': 'hut_hearth', 'traits': {'comfort': 1}}, {'label': 'Climb a little higher to see the stars', 'next': 'hut_hearth', 'traits': {'reflective': 1}}, {'label': 'Race the wind along the ridge', 'next': 'hut_hearth', 'traits': {'adventurous': 1}}]}, 'hut_hearth': {'title': 'Hearth & Maps', 'img': 'hut_hearth.png', 'text': 'Hikers stamp snow from boots; a kettle sings. Old topo maps paper the walls like treasure.', 'choices': [{'label': 'Curl near the stove and sigh', 'next': 'closing_moments', 'traits': {'comfort': 2}}, {'label': 'Point at a daring route on the map', 'next': 'closing_moments', 'traits': {'adventurous': 2}}, {'label': 'Trace a river with your hoof, thoughtful', 'next': 'closing_moments', 'traits': {'reflective': 2}}, {'label': 'Boop a hiker’s glove and oink', 'next': 'closing_moments', 'traits': {'playful': 2}}]}, 'closing_moments': {'title': 'Closing Moments', 'img': 'closing_moments.png', 'text': 'Night settles softly. Wherever Piggy roamed—fields, coasts, forests, or snow—the day has gathered into warm company and quiet pride. It’s time to see what kind of feast this journey has called forth.', 'choices': [{'label': '✨ Reveal Piggy’s feast', 'next': 'REVEAL', 'traits': {}}]}}

DISH_TEXT = {'carbonara': ('🎉 Feast: Carbonara', 'A farmhouse supper that hugs you from the inside—silky, cozy, and celebratory.'), 'bolognese': ('🎉 Feast: Bolognese', 'Seaside stories simmered into something hearty and bold.'), 'aglio': ('🎉 Feast: Aglio e Olio', 'Bright, simple, and brave—the wanderer’s delight.'), 'baked_fusilli': ('🎉 Feast: Baked Fusilli', 'Bubbling, golden comfort, baked with togetherness.'), 'indomie': ('🎉 Feast: Indomie with Egg', 'Playful bowls under starry skies; joy that can’t sit still.'), 'ochazuke': ('🎉 Feast: Ochazuke', 'Quiet warmth poured over the day—gentle, steady, soothing.'), 'curry': ('🎉 Feast: Japanese Curry Rice', 'Snow-day heartiness—sturdy, friendly, and steaming.'), 'japchae': ('🎉 Feast: Japchae', 'Lantern-lit colors, a festival on a plate.')}

def add_traits(d):
    for k,v in d.items():
        st.session_state["traits"][k] = st.session_state["traits"].get(k,0) + v

def reveal_dish():
    scores = st.session_state["traits"]
    ranked = sorted(TRAITS, key=lambda t: scores.get(t,0), reverse=True)
    top = scores.get(ranked[0],0)
    top_traits = [t for t in ranked if scores.get(t,0) == top and top>0]
    if len(top_traits) == 1:
        dish_key = DISH_BY_DOMINANT[top_traits[0]]
    else:
        key = tuple(sorted(top_traits[:2]))
        dish_key = PAIR_TO_DISH.get(key)
        if not dish_key:
            dish_key = DISH_BY_DOMINANT[ranked[0]]
    st.session_state["dish"] = dish_key
    st.session_state["scene"] = "END"

if "scene" not in st.session_state:
    st.session_state.scene = "start"
    st.session_state.step = 1
    st.session_state.traits = {}
    st.session_state.history = []

st.title("🐷 Piggy Pig’s Dynamic Buffet Adventure")
st.caption("Your choices shape Piggy’s feast. No spoilers — the ending dish is determined by your journey’s *personality*.")
st.caption(f"Step {st.session_state['step']} · Traits so far: " + ", ".join([f"{k}={st.session_state['traits'].get(k,0)}" for k in TRAITS]))

if st.session_state.scene == "REVEAL":
    reveal_dish()

if st.session_state.scene == "END":
    dish_key = st.session_state["dish"]
    title, desc = DISH_TEXT[dish_key]
    st.header(title)
    st.image(img_path(dish_key + ".png"), use_column_width=True)
    st.write(desc)
    st.write("— and yes, tonight’s feast highlights your favorite notes: sautéed mushrooms & onions. 🍄🧅")
    if st.button("🔁 Play Again", type="primary"):
        st.session_state.clear()
        st.rerun()
else:
    sc = SCENES[st.session_state.scene]
    st.header(sc["title"])
    st.image(img_path(st.session_state.scene + ".png"), use_column_width=True)
    st.write(sc["text"])

    cols = st.columns(len(sc["choices"]))
    for i, choice in enumerate(sc["choices"]):
        with cols[i % len(cols)]:
            if st.button(choice["label"], use_container_width=True):
                for k,v in choice.get("traits", {}).items():
                    st.session_state["traits"][k] = st.session_state["traits"].get(k,0) + v
                st.session_state.history.append({"scene": st.session_state.scene, "choice": choice["label"], "traits": choice.get("traits", {})})
                st.session_state.scene = choice["next"]
                st.session_state.step += 1
                if st.session_state.step > 10:
                    st.session_state.scene = "REVEAL"
                st.rerun()
