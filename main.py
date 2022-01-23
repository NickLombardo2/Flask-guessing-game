from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return "<strong><h1>Lets play a game! Guess a number between 0 and 9</h1></strong>"\
            "<img scr= 'https://media0.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid=ecf05e47ywbciny9cu13w9i3fovom11rxp6biorn97as7rst&rid=200w.webp&ct=g'/> "


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color:red'> Too high, try again!</h1>"\
        "<img src='https://media1.giphy.com/media/KCfpWuNnTcLbc3aLvZ/200w.webp?cid=ecf05e478pn45wz6cc734zm3fgpxs7jirpgd6hcfst3bxqhe&rid=200w.webp&ct=g'/>"

    elif guess < random_number:
        return "<h1 style='color:red'> Too low, try again!</h1>"\
        "<img src='https://media1.giphy.com/media/KCfpWuNnTcLbc3aLvZ/200w.webp?cid=ecf05e478pn45wz6cc734zm3fgpxs7jirpgd6hcfst3bxqhe&rid=200w.webp&ct=g'/>"
    else:
        return "<h1 style='color:green'>You found the correct number!</h1>"\
        "<img src='https://media1.giphy.com/media/Xf0kExNKrVEmh0Y1zy/200w.webp?cid=ecf05e47c815gebh26b7gioongnhwafgpozcj2uif28uxfn6&rid=200w.webp&ct=g'/>"


if__name__ == "__main__":\
    app.run(debug=True)
