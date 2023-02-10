import json
import random

items = [{"name": "Apple", "description": "A round fruit with red or green skin and white, juicy interior."},
         {"name": "Banana", "description": "A long, curves fruit with yellow or green skin and soft, sweet flesh."},
         {"name": "Carrot", "description": "A long, think, orange root vegetable with a crisp texture."},
         {"name": "Dog", "description": "A four-legged mammal with fur, wagging tail, and a friendly disposition."},
         {"name": "Egg", "description": "A oval shaped, white, or brown, oval shaped food item that comes"
                                        "from chickens."},
         {"name": "Flower", "description": "A plant with brightly coloured petals and a sweet fragrance, often "
                                           "given as a gift."},
         {"name": "Guitar", "description": "A musical instrument with six strings and a hallow body, used for "
                                            "playing a variety of music."},
         {"name": "Hat", "description": "A head covering , protection from sun or rain, or as a fashion accessory."},
         {"name": "Ice cream", "description": "A sweet, creamy frozen dessert made from milk, cream, and sugar."},
         {"name": "Jacket", "description": "A type of clothing worn on the upper body, typically"
                                           " made of a warm material."},
         {"name": "Kangaroo", "description": "A marsupial native to Australia, known for its powerful hind legs"
                                             " and tail used for hopping."},
         {"name": "Lemon", "description": "A small. round citrus fruit with sour, acidic taste and a "
                                          "bright, yellow skin."},
         {"name": "Moon", "description": "A natural satellite of the Earth, visible at night as bright, round"
                                         "object in the sky."},
         {"name": "Newspaper", "description": "A printed publication containing news, articles, and information,"
                                              "often distributed daily."},
         {"name": "Ocean", "description": "A vast body of salt water that covers more than 70% of the Earth's surface"},
         {"name": "Pen", "description": "A writing instrument with small, replaceable in cartridge, used for writing"
                                        "on paper."},
         {"name": "Quilt", "description": "A type of bedding made with two layers of fabric stitched together with "
                                          "padding in between."},
         {"name": "Raccoon", "description": "A mammal with a distinctive black and white face, know for its "
                                            "intelligence and adaptability."},
         {"name": "Sunflower", "description": "A tall, yellow-flowered plant with large, ray-like petals and a dark"
                                              "central disk."},
         {"name": "Table", "description": "A piece of furniture with a flat top and more than one legs, used for"
                                          "supporting objects or holding things."},
         {"name": "Umbrella", "description": "A portable, collapsible canopy supported on a central pole, used for"
                                             "protection from the rain or sun."},
         {"name": "Violin", "description": "A string musical instrument with four strings, held between the chin and "
                                           "shoulder and played with a bow."},
         {"name": "Watch", "description": "A small timepiece worn on the wrist or carried in a pocket, used for"
                                          "keeping track of time"},
         {"name": "Xylophone", "description": "A musical instrument consisting of a set of wooden bars that are"
                                              "stuck with a mallet produce musical tones."}]
with open("items.json", "w") as f:
    json.dump(items, f)


with open("items.json", "w") as write_file:
    json.dump(items, write_file, indent=4)


with open("items.json", "r") as f:
    items = json.load(f)

# import json
# import random

# Load the JSON file into a Python object
with open("items.json", "r") as f:
    items = json.load(f)

# Create a dictionary to store player scores
scores = {}


def write_json(player, scores):
    with open("League_table.json", "r") as file:
        League_table = json.load(file)
        item = {"name": f"{player}", "score": scores}
        League_table.append(item)
    with open("League_table.json", "w") as file:
        json.dump(League_table, file)


def read_json():
    with open("League_table.json", "r") as file:
        League_table = json.load(file)
        for item in League_table:
            print(item["name"], end="\t")
            print(item["score"])


def main():
    print("Welcome to the guessing game!")
    print("1. View league table")
    print("2. New player")
    print("3. Existing player")
    choice = input("Please select an option: ")

    if choice == "1":
        view_league_table()
    elif choice == "2":
        new_player()
    elif choice == "3":
        existing_player()
    else:
        print("Invalid choice. Please try again.")
        main()


def view_league_table():
    print("League Table:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    main()


def new_player():
    player_name = input("Please enter your player name: ")
    print("Hello " + player_name)
    scores[player_name] = 0
    play_game(player_name)


def existing_player():
    player_name = input("Please enter your player name: ")
    print("Wellcome back " + player_name)
    if player_name in scores:
        play_game(player_name)

    else:
        print("Player not found. Please try again.")
        existing_player()


def play_game(player_name):
    # Select 6 random items from the list
    random_items = random.sample(items, 6)

    # Loop through the items and ask the player to guess the name
    for item in random_items:
        description = item["description"]
        name = item["name"]
        tries = 3
        while tries > 0 and scores[player_name] < 3:
            guess = input(f"What is the name of this item?\n{description}\n")
            if guess.lower() == name.lower():
                print("Correct!")
                scores[player_name] += 1
                break
            else:
                tries -= 1
                if tries > 0:
                    print(f"Incorrect. You have {tries} tries left.")
                else:
                    print("Game over.")
                    scores[player_name] = 0
                    main()

    print("Thanks for playing! Your score is ", player_name, scores[player_name])
    write_json(player_name, scores[player_name])
    main()


main()
print(scores)
