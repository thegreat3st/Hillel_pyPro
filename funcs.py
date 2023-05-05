import pyinputplus as pyip

def nameinpfunc():
    while True:
        nameinp = pyip.inputStr("Enter a player name: ")
        if any(char.isdigit() for char in nameinp) == False:
            return nameinp
        else:
            print(ValueError)
            continue

def ageinpfunc():
    ageinp = pyip.inputNum("Enter age: ", lessThan = 50)
    return ageinp

def numberinpfunc():
    numberinp = pyip.inputNum("Enter number: ", lessThan = 100)
    return numberinp

def players_repr(players: list[dict]) -> None:
    for player in players:
        #print(f"{player['name']=}, {player['age']=}")
        print(player)

def players_add(players: list[dict], player: dict) -> list[dict]:
    while True:
        try:
            name = nameinpfunc()
            age = ageinpfunc()
            number = numberinpfunc()
            break
        except ValueError:
            print(f"{nameinpfunc} is not a name")
    player = {"name": str(name), "age": age, "number": number}
    players.append(player)
    return players

def players_del(players: list[dict]) -> list[dict]:
    name = nameinpfunc()
    print(f"You deleted {name} from a team")
    for index in range(len(players)):
        if players[index]['name'] == name:
            del players[index]
            break
    return players

def players_find_by_values(players: list[dict]) -> list[dict]:
    while True:
        opt = ["age", "number"]
        user_inp = input(f"Choose value to find player: {opt}")
        try:
            if user_inp == "age":
                age_find = ageinpfunc()
                players = [i for i in players if (i['age'] == age_find)]
                print(players)
            elif user_inp == "number":
                number_find = numberinpfunc()
                players = [i for i in players if (i['number'] == number_find)]
                print(players)
            else:
                print("Sorry, I didn't understand that") 
                continue
        except ValueError:
            print("Sorry, I didn't understand that")
            break
    return players

def players_get_by_name(players: list[dict], player: dict) -> dict | None:
    """If multiple players with same name - return the first one."""
    YesNo = ["yes", "no"]
    while True:
        name = nameinpfunc()
        if not any(v["name"] == name for v in players):
            print(f"Name {name} does not exist")
            YesNoinp = input(f"Would u like to add it? {YesNo}")
            if YesNoinp == "no":
                break
            elif YesNoinp == "yes":
                players_add(players, player)
        elif any(v["name"] == name for v in players):
            res = [i for i in players if (i["name"] == name)]
            print(res)
        elif any(v["name"] == v["name"] == name for v in players):
            print(f" Name {name} already exists")
            res = [i for i in players if (i["name"] == i["name"] == name)]
            print(res)
        break

def main():
    player = {"name": str, "age": int, "number": int}
    players = []
    options = ["repr", "add", "del", "find", "get", "exit"]
    while True:
        user_input = input(f"Choose 1 value: {options}")
        try:
            if user_input == "add":
                players_add(players, player)
            elif user_input == "del":   
                players_del(players)
            elif user_input == "find":
                players_find_by_values(players)
            elif user_input == "get":
                players_get_by_name(players, player)
            elif user_input == "repr": 
                players_repr(players)
            elif user_input == "exit":
                break
            else:
                print("Sorry, I didn't understand that") 
                continue
        except ValueError:
            print("Sorry, I didn't understand that") 
            continue

if __name__ == "__main__":
    main()