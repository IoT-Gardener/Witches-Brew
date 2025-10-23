
import itertools
import random
import time
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie

# Set the page title and icon and set layout to "wide" to minimise margains
st.set_page_config(page_title="Witches Brew 2025", page_icon=":sorceress:", layout="wide")

def main():
    head_l, head_r = st.columns((1.5,1), vertical_alignment="center")
    with head_l:
        st.subheader("The season of wild magic")
        st.title("Witches Brew 2025")
    with head_r:
        st_lottie("https://lottie.host/29f7c074-e7f9-46df-a493-4e41e644f5af/SPGVq055SI.json")
    st.write("---")

    with st.expander("How it works", expanded=True):
        st.subheader("How it works!")
        st.markdown("""This year's theme is wild magic! And the way things will work is simple!
            \nBelow you will find a number of roll tables, simply roll some dice to pick your spirit(s), mixer(s), garnish and splash of wild magic
            \nThen mix em all together and enjoy!!
            \nIf you are unhappy with the results, feel free to cast a spell from the spell list to change it up a little!
            \nTo cast a spell, simply take a number of shots equal to the mana cost and resolve the effect.
            \nIf this all seems like a bit much and just want to make a rum and coke, go for it. You do you boo :heart:
        """)
    with st.expander("The roll table!", expanded=True):
        data = {
            "Alcohol_1": ['Keylime Pie Gin', 'Rhubarb Gin', 'Custom Gin', 'Mead', 'Khalua', "Bailey's", 'Buckfast', 'Port', 'Spiced Rum', 'Prosecco', 'Blue Curacao', 'Chocolate Cream Liquer', 'Peach Brandy', 'Opihir Gin', 'Gin', 'Chocolate Orange Gin Liquer'],
            "Alcohol_2": ['Keylime Pie Gin', 'Rhubarb Gin', 'Custom Gin', 'Mead', 'Khalua', "Bailey's", 'Buckfast', 'Port', 'Spiced Rum', 'Prosecco', 'Blue Curacao', 'Chocolate Cream Liquer', 'Peach Brandy', 'Opihir Gin', 'Gin', 'Chocolate Orange Gin Liquer'],
            "Mixer_1": ['Sloe Simple Syrup', 'Ginger Beer (Non-alcoholic)', 'Pepsi (reg)', 'Pepsi (max)', 'Lemonade', 'Tonic', 'Orange Juice', 'Grenadine'],
            "Mixer_2": ['Sloe Simple Syrup', 'Ginger Beer (Non-alcoholic)', 'Pepsi (reg)', 'Pepsi (max)', 'Lemonade', 'Tonic', 'Orange Juice', 'Grenadine'],
            "Garnish": ['Rosemary', 'Organge Slice', 'Lemon Slice', 'Cucumber']
        }
        st.write(len(data["Alcohol_1"]))
        zipped_data = list(itertools.zip_longest(*data.values()))
        df = pd.DataFrame(zipped_data, columns=data.keys())
        df.index = range(1, len(df) + 1)
        st.table(df)

        wild_magic = {
            "Wild_Magic": [
                # The First 5: Bad Effects (Ruining the Drink)
                "Add 3 dashes of unaged Soy Sauce to the drink.",
                "Add a shot of olive or pickle brine",
                "Add 1 tsp of hot sauce.",
                "A spoonful of Marmite (or Vegemite) is dissolved into the cocktail.",
                "The drink must be muddled with chilli",
                # The Middle 10: Interesting/Neutral Effects (Altering the Experience)
                "The drinker must find and use a makeshift straw.",
                "The drink is served in a tea or coffee mug.",
                "Any citrus (lime, lemon etc) is replaced with a splash of rice vinegar.",
                "Add 3 drops of food colouring.",
                "The drinker must stir the drink with their pinky finger before the first sip.",
                "The drink loses all its chill; it must be consumed at room temperature.",
                "WILL IT BLEND?!",
                "Add a drop of vanilla extract.",
                "You must close your eyes and drink while standing on one foot.",
                "The drink is poured into a wine glass rimmed with **chili powder and brown sugar**.",
                # The Final 5: Good Effects (Actively Improving the Drink)
                "Ice is replaced with frozen berries like cranberry or pineapple.",
                "A cinnamon stick is added, which must be used as a stirrer.",
                "Add a splash of elderflower.",
                "Make it a Pornstar! Add a shot of sparkling wine.",
                "The drink is topped with flaming citrus zest."
            ]
        }
        df2 = pd.DataFrame(wild_magic)
        df2.index = range(1, len(df2) + 1)
        st.table(df2)

    if st.button("Make me a drink!"):
        with st.status("Rolling for drink...", expanded=True) as status:
            st.write("First Brew: The Spirit Rises...")
            time.sleep(2)
            st.write("Deepen the Draught: Liqueur of Shadows...")
            time.sleep(2)
            st.write("Bitter or Bright: Serpent's Syrupy Kiss...")
            time.sleep(2)
            st.write("Transmuting Water: Essence of Nightshade...")
            time.sleep(2)
            st.write("Finishing Touch: A Fruited Hex for the Brim!")
            time.sleep(2)
            st.write("Alchemical Disaster: Containing wild magic")
            time.sleep(2)
            status.update(
                label="Download complete!", state="complete", expanded=True
            )
        st.success(f'Your drink is: {random.choice(data["Alcohol_1"])}, {random.choice(data["Alcohol_2"])}, {random.choice(data["Mixer_1"])}, {random.choice(data["Mixer_2"])}, {random.choice(data["Garnish"])}')
        st.error(f'But it has been struck with: {random.choice(wild_magic["Wild_Magic"])}')

    with st.expander("Cantrips", expanded=True):
        st.subheader("Avoid death")
        st.write("Remove one or more ingredients that you are allergic to from the drink.")

    with st.expander("First Level Spells", expanded=True):
        st.subheader("Boon of the Blind Eye.")
        st.write("Reroll one die for any ingredient in the Alcohol category (Alcohol 1 or Alcohol 2).")
        st.write("---")
        st.subheader("Mixer's Gambit.")
        st.write("Reroll one die for any ingredient in the Mixer category (Mixer 1 or Mixer 2).")
        st.write("---")
        st.subheader("Transmute Garnish.")
        st.write("Replace the garnish with a simple lemon slice.")
        st.write("---")

    with st.expander("Second Level Spells", expanded=True):
        st.subheader("Liquid Levitation")
        st.write("Remove any single rolled alcohol or mixer from the drink and do not replace it.")
        st.write("---")
        st.subheader("Like a Virgin...")
        st.write("Roll again on both the Mixer_1 and Mixer_2 table and replace both forms of Alcohol with the rolled results.")
        st.write("---")
        st.subheader("Fortify the First Spirit")
        st.write("Rather than adding Alcohol_2 to the drink, add a second measure of Alcohol_1.")
        st.write("---")

    with st.expander("Third Level Spells", expanded=True):
        st.subheader("Greater Baja Blast")
        st.write("Replace your cocktail with a delicious mountain dew... (and then hide from the wizard council.")
        st.write("---")


if __name__ == "__main__":
    main()