from flask import Flask

app = Flask (__name__)

def add_card_to_file(card):

  f = open("card_database.txt", "a+")
  f.write(card.name + " ," + card.description + "\n")
  f.close()

def read_cards_from_file():
  f = open("card_database.txt", "r")
  cards = f.read()
  f.close()
  return cards


class Card(object):

  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.tapped = False

  def tap(self):
    self.tapped = True

  def is_tapped(self):
    return self.tapped

@app.route("/")
def hello():
  return "Hello, world!"

@app.route("/add_card/<name>/<description>")
def add_card(name, description):
  card = Card(name, description)
  cards.append(card)
  add_card_to_file(card)
  return "your card " + name + " has been added"

@app.route("/get_cards")
def get_cards():
  return read_cards_from_file()

if __name__ == "__main__":

  app.run(host="0.0.0.0")
