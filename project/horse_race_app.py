from project.helpers.validators import ValidData, CreateHorse
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        valid_horses = ["Appaloosa", "Thoroughbred"]
        if horse_type in valid_horses:
            ValidData.if_horse_already_there(horse_name, self.horses)
            horse = CreateHorse.create_horse(horse_type, horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        ValidData.if_jockey_already_there(jockey_name, self.jockeys)
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        ValidData.if_race_already_there(race_type, self.horse_races)
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = ValidData.if_jockey_not_there(jockey_name, self.jockeys)
        horse = ValidData.get_horse_if_not_taken(horse_type, self.horses)

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = ValidData.check_if_race_dont_exist(race_type, self.horse_races)
        jockey = ValidData.if_jockey_not_there(jockey_name, self.jockeys)

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = ValidData.check_if_race_dont_exist(race_type, self.horse_races)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_of_the_race = ValidData.find_winner_by_fastest_horse(self.jockeys)
        return (
            f"The winner of the {race_type} race, with a speed of {winner_of_the_race.horse.speed}km/h is {winner_of_the_race.name}! Winner's horse: {winner_of_the_race.horse.name}.")
