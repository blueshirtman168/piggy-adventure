import os
import json
import streamlit as st

# ---------------------- CONFIG ----------------------
st.set_page_config(
    page_title="🐷 Piggy Pig’s Buffet Adventure",
    page_icon="🐷",
    layout="centered"
)

# Paths
IMG_DIR = os.path.join(os.path.dirname(__file__), "images")
SCENES_PATH = os.path.join(os.path.dirname(__file__), "scenes.json")

# Traits and dish mapping
TRAITS = ["adventurous", "comfort", "playful", "reflective"]

DISH_BY_DOMINANT = {
    "adventurous": "bolognese",
    "comfort": "carbonara",
    "playful": "indomie",
    "reflective": "ochazuke"
}

PAIR_TO_DISH = {
    tuple(sorted(["adventurous", "reflective"])): "aglio",
    tuple(sorted(["comfort", "reflective"])): "baked_fusilli",
    tuple(sorted(["comfort", "adventurous"])): "curry",
    tuple(sorted(["playful", "reflective"])): "japchae"
}

DISH_TEXT = {
    "carbonara": ("Feast: Carbonara", "A farmhouse supper that hugs you from the inside—silky, cozy, and celebratory."),
    "bolognese": ("Feast: Bolognese", "Seaside stories simmered into something hearty and bold."),
    "aglio": ("Feast: Aglio e Olio", "Bright, simple, and brave—the wanderer’s delight."),
    "baked_fusilli": ("Feast: Baked Fusilli", "Bubbling, golden comfort, baked with togetherness."),
    "indomie": ("Feast: Indomie with Egg", "Playful bowls under starry skies; joy that can’t sit still."),
    "ochazuke": ("Feast: Ochazuke", "Quiet warmth poured over the day—gentle, steady, soothing."),
    "curry": ("Feast: Japanese Curry Rice", "Snow-day heartiness—sturdy, friendly, and steaming."),
    "japchae": ("Feast: Japchae", "Lantern-lit colors, a festival on a plate.")
}

# ---------------------- HELPERS ----------------------

def img_path(filename: str) -> str:
    return os.path.join(IMG_DIR, filename)

def apply_traits(delta: dict):
    for k, v in (delta or {}).items():
        st.session_state["traits"][k] = st.session_state["traits"].get(k, 0) + v

def reveal_dish():
    scores = st.session_state["traits"]
    ranked = sorted(TRAITS, key=lambda t: scores.get(t, 0), reverse=True)
    top = scores.get(ranked[0], 0)

    if top == 0:
        dish_key = "carbonara"  # default
    else:
        top_traits = [t for t in ranked if scores.get(t, 0) == top]
        if len(top_traits) == 1:
            dish_key = DISH_BY_DOMINANT[top_traits[0]]
        else:
            key = tuple(sorted(top_traits[:2]))
            dish_key = PAIR_TO_DISH.get(key, DISH_BY_DOMINANT[ranked[0]])

    st.session_state["dish"] = dish_key
    st.session_state["scene"] = "END"

# ---------------------- SCENES ----------------------

# If you want to store scenes externally, load them here:
if os.path.exists(SCENES_PATH):
    SCENES = json.load(open(SCENES_PATH))
else:
    # Minimal inline structure
    SCENES = {
        "start": {
            "title": "A Pig Sets Out",
            "img": "start.png",
            "text": "Piggy Pig wakes one bright morning with an adventurous heart — today she will explore the wonders of Aotearoa (New Zealand)! Which way should she trot first?",
            "choices": [
                {"label": "🌾 Toward the golden farmlands", "next": "farm1", "traits": {"comfort": 1}},
                {"label": "🌊 Toward the sea breeze", "next": "coast1", "traits": {"adventurous": 1}},
                {"label": "🌲 Into the deep forest valley", "next": "forest1", "traits": {"reflective": 1}},
                {"label": "🍎 Past the orchards and gardens", "next": "orch1", "traits": {"comfort": 1}}
            ]
        },
        "final_prep": {
            "title": "Closing Moments",
            "img": "final_prep.png",
            "text": "After all her travels, Piggy Pig finally arrives at a mountain hut. It’s time for the feast reveal.",
            "choices": [
                {"label": "✨ Reveal Feast", "next": "REVEAL", "traits": {}}
            ]
        }
    }

# ---------------------- STATE ----------------------

if "scene" not in st.session_state:
    st.session_state.scene = "start"
    st.session_state.traits = {}
    st.session_state.flags = {}
    st.session_state.history = []
    st.session_state.step = 1

# ---------------------- RENDER ----------------------

st.title("🐷 Piggy Pig’s Buffet Adventure")
st.caption("An interactive story where choices shape the feast.")

if st.session_state.scene == "REVEAL":
    reveal_dish()

if st.session_state.scene == "END":
    dish_key = st.session_state["dish"]
    title, desc = DISH_TEXT[dish_key]
    st.header(title)
    st.image(img_path(dish_key + ".png"), use_column_width=True)
    st.write(desc)
    st.write("And of course, every dish is brought to life with Piggy’s favorite touch: sautéed mushrooms & onions 🍄🧅")

    if st.button("🔁 Play Again", type="primary"):
        st.session_state.clear()
        st.rerun()

else:
    sc = SCENES.get(st.session_state.scene, SCENES["start"])
    st.header(sc["title"])

    if "img" in sc:
        st.image(img_path(sc["img"]), use_column_width=True)

    st.write(sc["text"])

    cols = st.columns(len(sc["choices"]))
    for i, choice in enumerate(sc["choices"]):
        with cols[i % len(cols)]:
            if st.button(choice["label"], use_container_width=True):
                apply_traits(choice.get("traits"))
                st.session_state.history.append({
                    "scene": st.session_state.scene,
                    "choice": choice["label"],
                    "traits": choice.get("traits", {})
                })
                st.session_state.scene = choice["next"]
                st.session_state.step += 1

                if st.session_state.step >= 10 and st.session_state.scene not in ("final_prep", "REVEAL", "END"):
                    st.session_state.scene = "final_prep"
                st.rerun()
