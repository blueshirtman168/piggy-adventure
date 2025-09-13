
import os, json
import streamlit as st

st.set_page_config(page_title="Piggy Pig - Painterly Buffet Adventure", page_icon="🐷", layout="centered")

DISH_BY_DOMINANT = {"adventurous":"bolognese","comfort":"carbonara","playful":"indomie","reflective":"ochazuke"}
PAIR_TO_DISH = {tuple(sorted(["adventurous","reflective"])):"aglio",
                tuple(sorted(["comfort","reflective"])):"baked_fusilli",
                tuple(sorted(["comfort","adventurous"])):"curry",
                tuple(sorted(["playful","reflective"])):"japchae"}
TRAITS = ["adventurous","comfort","playful","reflective"]

def img_path(name): return os.path.join(os.path.dirname(__file__), "images", name)

def load_scenes():
    p = os.path.join(os.path.dirname(__file__), "scenes.json")
    return json.load(open(p, encoding="utf-8"))

SCENES = load_scenes()

DISH_TEXT = {
 "carbonara": ("Feast: Carbonara","A farmhouse supper that hugs you from the inside - silky, cozy, and celebratory."),
 "bolognese": ("Feast: Bolognese","Seaside stories simmered into something hearty and bold."),
 "aglio": ("Feast: Aglio e Olio","Bright, simple, and brave - the wanderer's delight."),
 "baked_fusilli": ("Feast: Baked Fusilli","Bubbling, golden comfort, baked with togetherness."),
 "indomie": ("Feast: Indomie with Egg","Playful bowls under starry skies; joy that cannot sit still."),
 "ochazuke": ("Feast: Ochazuke","Quiet warmth poured over the day - gentle, steady, soothing."),
 "curry": ("Feast: Japanese Curry Rice","Snow-day heartiness - sturdy, friendly, and steaming."),
 "japchae": ("Feast: Japchae","Lantern-lit colors, a festival on a plate."),
}

def apply_traits(d):
    for k,v in (d or {}).items():
        st.session_state["traits"][k] = st.session_state["traits"].get(k,0) + v

def set_flags(flags):
    for f in (flags or []):
        st.session_state["flags"][f] = True

def clear_flags(flags):
    for f in (flags or []):
        if f in st.session_state["flags"]:
            del st.session_state["flags"][f]

def reveal_dish():
    scores = st.session_state["traits"]
    ranked = sorted(TRAITS, key=lambda t: scores.get(t,0), reverse=True)
    top = scores.get(ranked[0],0)
    top_traits = [t for t in ranked if scores.get(t,0) == top and top>0]
    if len(top_traits) == 1:
        dish_key = DISH_BY_DOMINANT[top_traits[0]]
    else:
        key = tuple(sorted(top_traits[:2]))
        dish_key = PAIR_TO_DISH.get(key) or DISH_BY_DOMINANT[ranked[0]]
    st.session_state["dish"] = dish_key
    st.session_state["scene"] = "END"

# Init
if "scene" not in st.session_state:
    st.session_state.scene = "farm1"
    st.session_state.step = 1
    st.session_state.traits = {}
    st.session_state.flags = {}
    st.session_state.history = []

st.title("Piggy Pig's Painterly Buffet Adventure")
st.caption("Choices ripple forward. Traits shape the feast. Flags make the story remember you.")
st.caption(f"Step {st.session_state['step']} - Traits: " + ", ".join([f"{k}={st.session_state['traits'].get(k,0)}" for k in TRAITS]))

if st.session_state.scene == "REVEAL":
    reveal_dish()

if st.session_state.scene == "END":
    dish_key = st.session_state["dish"]
    title, desc = DISH_TEXT[dish_key]
    st.header(title)
    st.image(img_path(dish_key + ".png"), use_column_width=True)
    st.write(desc)
    st.write("And yes, tonight's feast highlights sauteed mushrooms & onions. 🍄🧅")
    if st.button("Play Again", type="primary"):
        st.session_state.clear(); st.rerun()
else:
    sc = SCENES[st.session_state.scene]
    st.header(sc["title"])
    st.image(img_path(st.session_state['scene'] + ".png"), use_column_width=True)

    text = sc["text"]
    for f, add in (sc.get("flags_text") or {}).items():
        if st.session_state["flags"].get(f): text += "\\n\\n" + add
    st.write(text)

    cols = st.columns(len(sc["choices"]))
    for i, ch in enumerate(sc["choices"]):
        with cols[i % len(cols)]:
            if st.button(ch["label"], use_container_width=True):
                apply_traits(ch.get("traits"))
                set_flags(ch.get("set_flags"))
                clear_flags(ch.get("clear_flags"))
                st.session_state.history.append({"scene": st.session_state.scene, "choice": ch["label"], "traits": ch.get("traits", {}), "set": ch.get("set_flags", []), "clear": ch.get("clear_flags", [])})
                st.session_state.scene = ch["next"]
                st.session_state.step += 1
                if st.session_state.step >= 10 and st.session_state.scene not in ("final_prep","REVEAL","END"):
                    st.session_state.scene = "final_prep"
                st.rerun()
