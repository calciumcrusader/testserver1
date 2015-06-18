from flask import Flask
from flask import render_template
from flask import request


app = Flask (__name__)

class CardDatabase(object):

  def search(self,card):
    pass
  def delete(self,card):
    pass
  def add(self,card):
      f = open("card_database.txt", "a+")
      f.write(card.name + " ," + card.description + "\n")
      f.close()

  def show(self):
      f = open("card_database.txt", "r")
      cards = f.readlines()
      first_card_string = cards[0].split(",")
      first_card = Card(first_card_string[0],first_card_string[1])
      card_list = []
      for card_string in cards:
          card_tuple = card_string.split(",")
          card = Card(card_tuple[0],card_tuple[1])
          card_list.append(card)
      f.close()
      return card_list

card_db = CardDatabase()

@app.route("/add_card_to_file")
def add_card_to_file():
  name = request.args.get("name")
  description = request.args.get("description")
  card = Card(name,description)
  f = card_db.add(card)
  return "Your new card " + name + " was added as well as the description " + description




class Card(object):

  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.tapped = False

  def tap(self):
    self.tapped = True

  def is_tapped(self):
    return self.tapped

  def __str__(self):
    return self.name + " " + self.description

  def __repr__(self):
    return self.__str__()

@app.route("/")
def hello():
  return render_template('index.html',)


@app.route("/add_card")
def add_card_2():
  return render_template('index.html')

def add_card():
  name = request.args.get ("name")
  description = request.args.get ("description")
  card = Card(name, description)

  add_card_to_file(card)
  return "your card " + name + " has been added"

@app.route("/get_cards")
def get_cards():
  return str(card_db.show())

if __name__ == "__main__":
  app.debug = True
  app.run(host="0.0.0.0")
