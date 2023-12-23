from flask import Flask
import random

app = Flask(__name__)

chihuahua_facts = [
    "Chihuahuas are one of the smallest dog breeds.",
    "They were named after the Mexican state of Chihuahua.",
    "Chihuahuas have one of the longest lifespans of any dog breed, often living up to 15 years or more.",
    "They come in a wide variety of colors, from solid black to solid white, spotted, or in a variety of other patterns.",
    "Chihuahuas can be either smooth-coat or long-coat.",
    "Despite their small size, Chihuahuas often have a feisty and loyal personality.",
    "They were once believed to have healing powers and were used in religious rituals by ancient civilizations."
]

@app.route('/woof')
def dog():
    fact = random.choice(chihuahua_facts)
    return f"""
    <div style='text-align: center;'>
        <h1>Woof! 🐕</h1>
        <p><h2>Did you know?</h2></p>
        <p>{fact}</p>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=False)
