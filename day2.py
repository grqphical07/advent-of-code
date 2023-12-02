import dataclasses
from typing import List

@dataclasses.dataclass
class Result:
    red: int
    blue: int
    green: int

@dataclasses.dataclass
class Game:
    id: int
    results: List[Result]

def parse_game(line: str) -> Game:
    game = Game(0, [])
    id = int(line.split(":")[0].replace("Game ", ""))
    line = line.replace(f"Game {id}: ", "").removesuffix("\n")

    results_str = line.split("; ")
    results = []
    
    for result in results_str:
        result_obj = Result(0, 0, 0)
        colours = result.split(", ")
        for colour in colours:
            amount, colour = colour.split(" ")
            if colour == "red":
                result_obj.red = int(amount)
            elif colour == "blue":
                result_obj.blue = int(amount)
            else:
                result_obj.green = int(amount)
        results.append(result_obj)

    game.id = id
    game.results = results
    return game
            


with open("data.txt", "r") as f:
    data = f.readlines()

sum = 0

for line in data:
    game = parse_game(line)
    
    greatest_red = 0
    greatest_blue = 0
    greatest_green = 0

    for result in game.results:
        if result.red > greatest_red:
            greatest_red = result.red
        
        if result.blue > greatest_blue:
            greatest_blue = result.blue
        
        if result.green > greatest_green:
            greatest_green = result.green
    
    power = greatest_blue * greatest_green * greatest_red
    sum += power

print(sum)