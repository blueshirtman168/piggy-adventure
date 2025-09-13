
import os
import streamlit as st

st.set_page_config(page_title="Piggy Pig’s Great NZ Feast Adventure", page_icon="🐷", layout="centered")

def img_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), "images", filename)

def render_scene(key: str):
    scene = SCENES[key]
    st.header(scene["title"])
    st.image(img_path(scene["img"]), use_column_width=True)
    st.write(scene["text"])
    cols = st.columns(len(scene["choices"])) if scene["choices"] else [st.container()]
    for i, (label, nxt) in enumerate(scene["choices"]):
        with cols[i % len(cols)]:
            if st.button(label, use_container_width=True):
                st.session_state["scene"] = nxt
                st.session_state["step"] += 1
                st.rerun()
    if not scene["choices"]:
        if st.button("🔁 Restart Adventure", type="primary"):
            st.session_state.clear()
            st.rerun()

if "scene" not in st.session_state:
    st.session_state.scene = "start"
    st.session_state.step = 1

st.title("🐷✨ Piggy Pig’s Great NZ Feast Adventure")
st.caption("A whimsical, spoiler-free, 10-step branching story through Aotearoa.")
st.caption(f"Step {st.session_state['step']}")

SCENES = {
    "start": {
        "title":"🌅 The Beginning",
        "img":"start.png",
        "text":"The sun rises over New Zealand. Piggy Pig’s hooves are restless. Where shall she begin?",
        "choices":[
            ("🌾 Waikato Fields","carb1"),
            ("🏖 Coromandel Coast","bolo1"),
            ("🌲 Fiordland Forest","agl1"),
            ("🏔 Southern Alps","bake1"),
            ("🎈 Children’s Laughter (Fields)","indo1"),
            ("🥝 Kiwifruit Orchard","ocha1"),
            ("🏮 Lantern on a Mountain Path","cur1"),
            ("🐕 Sheepdog Paddocks","jap1"),
        ],
    },
    # Carbonara 10 steps -> carbonara
    "carb1":{"title":"Waikato Fields","img":"carb1.png","text":"Piggy trots through rolling hills and tall grass.","choices":[("Head toward the distant barn","carb2"),("Follow the cowbells","carb2")]},
    "carb2":{"title":"Cow Herd","img":"carb2.png","text":"A herd blocks the path. They stare, curious.","choices":[("Sneak under a fence","carb3"),("Wait politely","carb3")]},
    "carb3":{"title":"Dairy Lane","img":"carb3.png","text":"A quiet lane leads to a dairy barn, lanterns flicker inside.","choices":[("Trot to the barn","carb4")]},
    "carb4":{"title":"Barn Doors","img":"carb4.png","text":"Warm air and hay; calves sniff and nuzzle Piggy.","choices":[("Play hide-and-seek","carb5"),("Watch from a hay bale","carb5")]},
    "carb5":{"title":"Visitors Arrive","img":"carb5.png","text":"Children arrive, laughter echoing under the rafters.","choices":[("Join a game of tag","carb6"),("Show a piggy twirl","carb6")]},
    "carb6":{"title":"Storm Rolls In","img":"carb6.png","text":"Thunder rumbles. Rain drums the roof.","choices":[("Close the doors together","carb7"),("Fetch lanterns","carb7")]},
    "carb7":{"title":"Kitchen Light","img":"carb7.png","text":"Everyone gathers in a cozy farmhouse kitchen.","choices":[("Sit by the hearth","carb8")]},
    "carb8":{"title":"Stories & Smiles","img":"carb8.png","text":"Tales of the day are shared while rain taps the windows.","choices":[("Stay and listen","carb9")]},
    "carb9":{"title":"A Warm Welcome","img":"carb9.png","text":"Plates and cutlery clink cheerfully.","choices":[("Take your seat at the table","carb10")]},
    "carb10":{"title":"The Feast Appears","img":"carb10.png","text":"Steam rises as a comforting meal is served.","choices":[("Reveal the feast","carbonara")]},
    "carbonara":{"title":"🎉 Feast: Carbonara","img":"carbonara.png","text":"Creamy, cozy, and celebratory. A farmhouse supper.","choices":[]},
    # Bolognese path
    "bolo1":{"title":"Beach Morning","img":"bolo1.png","text":"Waves glitter. Piggy follows seashells along the sand.","choices":[("Explore a dune hut","bolo2"),("Build a sandcastle","bolo2")]},
    "bolo2":{"title":"Clouds Gather","img":"bolo2.png","text":"Wind picks up; rain runs across the beach.","choices":[("Dash to the hut","bolo3"),("Hide under driftwood","bolo3")]},
    "bolo3":{"title":"Shelter","img":"bolo3.png","text":"Fishermen laugh over cards; a place to dry off.","choices":[("Watch the game","bolo4"),("Shuffle the deck","bolo4")]},
    "bolo4":{"title":"Sudden Visitor","img":"bolo4.png","text":"A cheeky bird swoops in through the window!","choices":[("Chase outside","bolo5"),("Follow the tracks","bolo5")]},
    "bolo5":{"title":"Cliff Path","img":"bolo5.png","text":"Up the bluffs, wind in your ears.","choices":[("Keep climbing","bolo6"),("Circle the headland","bolo6")]},
    "bolo6":{"title":"Lookout","img":"bolo6.png","text":"Villagers wave from a cliff garden as the storm clears.","choices":[("Trot to the garden","bolo7")]},
    "bolo7":{"title":"Gathering Place","img":"bolo7.png","text":"A fire crackles; friends gather close.","choices":[("Warm your trotters","bolo8")]},
    "bolo8":{"title":"Shared Laughter","img":"bolo8.png","text":"Stories ripple like waves.","choices":[("Stay for supper","bolo9")]},
    "bolo9":{"title":"Table Under Lanterns","img":"bolo9.png","text":"Lanterns sway; bowls and plates appear.","choices":[("Take your seat","bolo10")]},
    "bolo10":{"title":"The Feast Appears","img":"bolo10.png","text":"A hearty village supper is served.","choices":[("Reveal the feast","bolognese")]},
    "bolognese":{"title":"🎉 Feast: Bolognese","img":"bolognese.png","text":"Rustic, generous, and full of seaside stories.","choices":[]},
    # Aglio
    "agl1":{"title":"Forest Trail","img":"agl1.png","text":"Fern fronds brush Piggy’s sides.","choices":[("Follow the water sound","agl2"),("Climb a mossy slope","agl2")]},
    "agl2":{"title":"Waterfall Mist","img":"agl2.png","text":"Sunlight turns spray to sparkles.","choices":[("Investigate a shimmering cave","agl3")]},
    "agl3":{"title":"Shimmering Cave","img":"agl3.png","text":"Glowworms paint the ceiling with stars.","choices":[("Bow to the unseen guardian","agl4"),("Whisper a thank you","agl4")]},
    "agl4":{"title":"River Whisper","img":"agl4.png","text":"A gentle current leads deeper into the valley.","choices":[("Walk beside the stream","agl5"),("Hop stone to stone","agl5")]},
    "agl5":{"title":"Forest Clearing","img":"agl5.png","text":"Campfires flicker among travelers.","choices":[("Approach the wanderers","agl6")]},
    "agl6":{"title":"New Friends","img":"agl6.png","text":"Smiles and welcomes; a place by the fire.","choices":[("Share road tales","agl7")]},
    "agl7":{"title":"Evening Calm","img":"agl7.png","text":"Crickets sing; stars gather overhead.","choices":[("Stay the night","agl8")]},
    "agl8":{"title":"Gentle Dawn","img":"agl8.png","text":"Morning like a soft blanket.","choices":[("Join the circle for breakfast","agl9")]},
    "agl9":{"title":"Circle of Friends","img":"agl9.png","text":"Plates and bowls are passed with care.","choices":[("Accept the morning feast","agl10")]},
    "agl10":{"title":"The Feast Appears","img":"agl10.png","text":"Simple, bright, and joyful.","choices":[("Reveal the feast","aglio_end")]},
    "aglio_end":{"title":"🎉 Feast: Aglio e Olio","img":"aglio_end.png","text":"Bright, friendly, and made to share.","choices":[]},
    # Baked Fusilli
    "bake1":{"title":"Alpine Ridge","img":"bake1.png","text":"Snow crunches; air sparkles.","choices":[("Head toward the hut’s glow","bake2"),("Watch the peaks","bake2")]},
    "bake2":{"title":"Hut Door","img":"bake2.png","text":"Warm light spills onto the snow.","choices":[("Step inside","bake3")]},
    "bake3":{"title":"Fire & Friends","img":"bake3.png","text":"Hikers smile; space by the hearth awaits.","choices":[("Settle by the fire","bake4")]},
    "bake4":{"title":"Storm Song","img":"bake4.png","text":"Wind howls; shutters rattle in rhythm.","choices":[("Help secure shutters","bake5"),("Stack wood neatly","bake5")]},
    "bake5":{"title":"Team Spirit","img":"bake5.png","text":"Warmth returns; laughter bounces.","choices":[("Share a story","bake6")]},
    "bake6":{"title":"Lantern Glow","img":"bake6.png","text":"Lanterns swing gently as night deepens.","choices":[("Stay by the hearth","bake7")]},
    "bake7":{"title":"Oven Wakes","img":"bake7.png","text":"An old oven opens with a cheer.","choices":[("Peek inside","bake8")]},
    "bake8":{"title":"Savory Air","img":"bake8.png","text":"Comfort fills the hut.","choices":[("Gather at the table","bake9")]},
    "bake9":{"title":"Friends Together","img":"bake9.png","text":"Plates line up. Smiles all around.","choices":[("Count down to supper","bake10")]},
    "bake10":{"title":"The Feast Appears","img":"bake10.png","text":"Bubbling, golden, and joyful.","choices":[("Reveal the feast","baked_fusilli")]},
    "baked_fusilli":{"title":"🎉 Feast: Baked Fusilli","img":"baked_fusilli.png","text":"Shelter, warmth, and shared comfort.","choices":[]},
    # Indomie
    "indo1":{"title":"Field Frolic","img":"indo1.png","text":"Children’s laughter twirls in the air.","choices":[("Chase kites","indo2"),("Roll in soft hay","indo2")]},
    "indo2":{"title":"Ribbon Tail","img":"indo2.png","text":"A crown of flowers and a ribboned tail!","choices":[("Race to the windbreak","indo3"),("Hide behind hay bales","indo3")]},
    "indo3":{"title":"Hide & Seek","img":"indo3.png","text":"Giggles erupt as Piggy is ‘found’.","choices":[("Play tag until dusk","indo4")]},
    "indo4":{"title":"Firefly Evening","img":"indo4.png","text":"Tiny lights drift through the field.","choices":[("Start a little camp","indo5"),("Tell silly stories","indo5")]},
    "indo5":{"title":"Camp Circle","img":"indo5.png","text":"Blankets spread, stars peek out.","choices":[("Sing a song","indo6")]},
    "indo6":{"title":"Snack Time","img":"indo6.png","text":"Backpacks unzip; everyone’s hungry.","choices":[("Gather around the pot","indo7")]},
    "indo7":{"title":"Bubbly Anticipation","img":"indo7.png","text":"Steam rises; cheerful chatter.","choices":[("Get your bowl ready","indo8")]},
    "indo8":{"title":"Under the Stars","img":"indo8.png","text":"Warm bowls, cozy hands, happy hearts.","choices":[("Line up for supper","indo9")]},
    "indo9":{"title":"Piggy’s Turn","img":"indo9.png","text":"A cheer goes up for Piggy!","choices":[("Bow dramatically","indo10")]},
    "indo10":{"title":"The Feast Appears","img":"indo10.png","text":"A playful supper for playful friends.","choices":[("Reveal the feast","indomie")]},
    "indomie":{"title":"🎉 Feast: Indomie with Egg","img":"indomie.png","text":"Playful, nostalgic, perfect under the stars.","choices":[]},
    # Ochazuke
    "ocha1":{"title":"Orchard Path","img":"ocha1.png","text":"Leaves whisper; fruit hangs like lanterns.","choices":[("Wave to the gardener","ocha2"),("Sit quietly under a vine","ocha2")]},
    "ocha2":{"title":"Warm Welcome","img":"ocha2.png","text":"A kind elder smiles and beckons.","choices":[("Trot over","ocha3")]},
    "ocha3":{"title":"Tea Porch","img":"ocha3.png","text":"Porch steps creak softly; a kettle waits.","choices":[("Rest your hooves","ocha4")]},
    "ocha4":{"title":"Soft Rain","img":"ocha4.png","text":"Raindrops patter on leaves; the world hushes.","choices":[("Listen to the rain","ocha5")]},
    "ocha5":{"title":"Tatami Room","img":"ocha5.png","text":"Shoji screens glow with gentle light.","choices":[("Settle on a cushion","ocha6")]},
    "ocha6":{"title":"Quiet Company","img":"ocha6.png","text":"Stories shared in soft voices.","choices":[("Breathe in the warmth","ocha7")]},
    "ocha7":{"title":"Evening Stillness","img":"ocha7.png","text":"A calm settles deep in your chest.","choices":[("Stay a little longer","ocha8")]},
    "ocha8":{"title":"Night Lantern","img":"ocha8.png","text":"A lantern is lit; shadows dance.","choices":[("Accept a humble supper","ocha9")]},
    "ocha9":{"title":"Gentle Table","img":"ocha9.png","text":"Simple place settings invite you to rest.","choices":[("Open your heart to the meal","ocha10")]},
    "ocha10":{"title":"The Feast Appears","img":"ocha10.png","text":"Soothing and warm, like a lullaby.","choices":[("Reveal the feast","ochazuke")]},
    "ochazuke":{"title":"🎉 Feast: Ochazuke","img":"ochazuke.png","text":"Quiet comfort while rain whispers.","choices":[]},
    # Curry
    "cur1":{"title":"Lantern on the Path","img":"cur1.png","text":"Snowflakes swirl around a tiny lantern.","choices":[("Follow the light","cur2"),("Climb higher","cur2")]},
    "cur2":{"title":"Hut in Snow","img":"cur2.png","text":"Warm silhouettes move behind frosted windows.","choices":[("Knock softly","cur3")]},
    "cur3":{"title":"Welcome Inside","img":"cur3.png","text":"Smiles and blankets; your cheeks thaw.","choices":[("Curl up by the fire","cur4")]},
    "cur4":{"title":"Shared Stories","img":"cur4.png","text":"Maps unfold; adventures retold.","choices":[("Point to a favorite route","cur5")]},
    "cur5":{"title":"Lantern Circle","img":"cur5.png","text":"A circle of light gathers friends close.","choices":[("Stay with the group","cur6")]},
    "cur6":{"title":"Snow Slows","img":"cur6.png","text":"Outside turns quiet and thick with white.","choices":[("Watch the window","cur7")]},
    "cur7":{"title":"Hearthside Humming","img":"cur7.png","text":"Someone hums a tune as embers glow.","choices":[("Hum along","cur8")]},
    "cur8":{"title":"Big Pot","img":"cur8.png","text":"A large pot bubbles gently over the fire.","choices":[("Gather your friends","cur9")]},
    "cur9":{"title":"Bowls Ready","img":"cur9.png","text":"Bowls and spoons line up neatly.","choices":[("Stand by for supper","cur10")]},
    "cur10":{"title":"The Feast Appears","img":"cur10.png","text":"Hearty and comforting after snow.","choices":[("Reveal the feast","curry")]},
    "curry":{"title":"🎉 Feast: Japanese Curry Rice","img":"curry.png","text":"Warmth that reaches your toes.","choices":[]},
    # Japchae
    "jap1":{"title":"Sheepdog Paddocks","img":"jap1.png","text":"Friendly barks and wagging tails.","choices":[("Play chase","jap2"),("Hide-and-seek by the fence","jap2")]},
    "jap2":{"title":"Hill Pursuit","img":"jap2.png","text":"Up the slope, laughter in the air.","choices":[("Sprint to the ridge","jap3"),("Dive behind a tussock","jap3")]},
    "jap3":{"title":"Hidden Hollow","img":"jap3.png","text":"A hollow log and a secret tunnel...","choices":[("Crawl inside","jap4")]},
    "jap4":{"title":"Secret Cave","img":"jap4.png","text":"Walls shimmer with faint colors.","choices":[("Go deeper","jap5")]},
    "jap5":{"title":"Crystal Hall","img":"jap5.png","text":"Rainbow crystals glow softly.","choices":[("Listen to the cave hum","jap6")]},
    "jap6":{"title":"Lantern Insects","img":"jap6.png","text":"Fireflies swirl like tiny lanterns.","choices":[("Spin slowly with the lights","jap7")]},
    "jap7":{"title":"Cave Guardian","img":"jap7.png","text":"A fox spirit bows with a smile.","choices":[("Bow back","jap8")]},
    "jap8":{"title":"Invitation","img":"jap8.png","text":"A warm invitation to stay a while.","choices":[("Accept with gratitude","jap9")]},
    "jap9":{"title":"Gathered Circle","img":"jap9.png","text":"A circle forms around a glowing pan.","choices":[("Hold your breath for the reveal","jap10")]},
    "jap10":{"title":"The Feast Appears","img":"jap10.png","text":"Colorful and lively, like the cave lights.","choices":[("Reveal the feast","japchae")]},
    "japchae":{"title":"🎉 Feast: Japchae","img":"japchae.png","text":"A festival of color under the earth’s lanterns.","choices":[]},
}

render_scene(st.session_state["scene"])
