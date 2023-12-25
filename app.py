from flask import Flask, render_template
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

chihuahua_images = [
    "/static/images/chihuahua1.png",
    "/static/images/chihuahua2.png",
    "/static/images/chihuahua3.png",
    "/static/images/chihuahua4.png",
]

@app.route('/woof')
def woof():
    image = random.choice(chihuahua_images)
    fact = random.choice(chihuahua_facts)
    return render_template("index.html", image_url=image, fact=fact)

if __name__ == '__main__':
    app.run(debug=False)
