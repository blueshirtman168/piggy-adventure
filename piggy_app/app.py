import streamlit as st

if "scene" not in st.session_state:
    st.session_state.scene = "start"

def go_to(scene):
    st.session_state.scene = scene

st.title("🐷✨ Piggy Pig’s Great NZ Feast Adventure")

SCENES = {
    "start": {
        "text": "The sun rises over New Zealand. Piggy Pig’s hooves are restless. Where does she begin?",
        "img": "start.png",
        "choices": [
            ("🌾 Waikato Hills", "wheat"),
            ("🏔 Southern Alps", "mountains"),
            ("🌊 Fiordland", "waterfall"),
            ("🏖 Coromandel Coast", "beach"),
        ]
    },
    "wheat": {
        "text": "Golden wheat sways in the breeze. What does Piggy do?",
        "img": "wheat.png",
        "choices": [
            ("Roll in the straw bales", "dairy"),
            ("Chase sparrows", "dogs"),
            ("Hide in the wheat", "children"),
        ]
    },
    "dairy": {
        "text": "Piggy meets the cows! How does she respond?",
        "img": "dairy.png",
        "choices": [
            ("Moo back loudly", "carbonara"),
            ("Play with calves", "bolognese"),
        ]
    },
    "dogs": {
        "text": "She stumbles onto a dog farm. What happens?",
        "img": "dogs.png",
        "choices": [
            ("Get herded in circles", "japchae"),
            ("Pretend to be a sheepdog", "aglio"),
        ]
    },
    "children": {
        "text": "Children find Piggy in the wheat! What do they do together?",
        "img": "children.png",
        "choices": [
            ("Chase and giggle in the fields", "indomie"),
            ("Storytime & snacks", "ochazuke"),
        ]
    },
    "mountains": {
        "text": "Piggy climbs into the Southern Alps. The air is cold.",
        "img": "mountains.png",
        "choices": [
            ("Climb glaciers", "storm"),
            ("Nap in a hut", "curry"),
            ("Follow goat tracks to valley", "indomie"),
        ]
    },
    "storm": {
        "text": "A storm hits the mountains. Where does Piggy go?",
        "img": "storm.png",
        "choices": [
            ("Hide in a barn", "baked_fusilli"),
            ("Find a magical cave", "japchae"),
        ]
    },
    "waterfall": {
        "text": "Piggy splashes in Fiordland waterfalls.",
        "img": "waterfall.png",
        "choices": [
            ("Snack in a kiwi orchard", "ochazuke"),
            ("Wander into a glowing cave", "japchae"),
            ("Follow river to dog farm", "aglio"),
        ]
    },
    "beach": {
        "text": "Piggy trots along Coromandel beaches.",
        "img": "beach.png",
        "choices": [
            ("Play with cheeky kea", "carbonara"),
            ("Chat with fisherman", "bolognese"),
            ("Meet sea taniwha", "baked_fusilli"),
        ]
    },
    "carbonara": {"text": "🥳 Feast: Carbonara! Creamy, indulgent, dairy-rich.", "img": "carbonara.png", "choices":[]},
    "bolognese": {"text": "🥳 Feast: Bolognese! Hearty, farm-to-table comfort.", "img": "bolognese.png", "choices":[]},
    "aglio": {"text": "🥳 Feast: Aglio e Olio! Simple, bold, and bright.", "img": "aglio.png", "choices":[]},
    "baked_fusilli": {"text": "🥳 Feast: Baked Fusilli! Warm and bubbly shelter food.", "img": "baked_fusilli.png", "choices":[]},
    "indomie": {"text": "🥳 Feast: Indomie with Egg! Fun, playful, childlike joy.", "img": "indomie.png", "choices":[]},
    "ochazuke": {"text": "🥳 Feast: Ochazuke! Gentle, soothing, cozy like bedtime.", "img": "ochazuke.png", "choices":[]},
    "curry": {"text": "🥳 Feast: Japanese Curry Rice! Hearty mountain comfort.", "img": "curry.png", "choices":[]},
    "japchae": {"text": "🥳 Feast: Japchae! Magical, colorful, playful noodles.", "img": "japchae.png", "choices":[]},
}

scene = SCENES[st.session_state.scene]
import os

img_path = os.path.join(os.path.dirname(__file__), "images", scene["img"])
st.image(img_path)
st.write(scene["text"])
for label, target in scene.get("choices", []):
    st.button(label, on_click=lambda t=target: go_to(t))

if not scene.get("choices"):
    if st.button("Restart Adventure"):
        go_to("start")
