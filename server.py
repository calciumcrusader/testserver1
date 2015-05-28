from flask import Flask

app = Flask (__name__)

class Card(object):

  def __init__(self, name, description):
    self.name = name
    self.description = description

cards = []

@app.route("/")
def hello():
  return "Hello, world!"

@app.route("/add_card/<name>/<description>")
def add_card(name, description):
  card = Card(name, description)
  cards.append(card)
  return "your card " + name + " has been added"

@app.route("/get_cards")
def get_cards():
  return_string = ""
  for card in cards:
    return_string += "(" + card.name + "," + card.description + ")"
  return return_string


if __name__ == "__main__":
  app.run()
