from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class CreateHorse:
    horses = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    @staticmethod
    def create_horse(h_type: str, name: str, speed: int):
        return CreateHorse.horses[h_type](name, speed)


class ValidData:
    @staticmethod
    def if_horse_already_there(name_of_horse, collection):
        for horse in collection:
            if horse.name == name_of_horse:
                raise Exception(f"Horse {horse.name} has been already added!")

    @staticmethod
    def if_jockey_already_there(name, collection):
        for jockey in collection:
            if jockey.name == name:
                raise Exception(f"Jockey {jockey.name} has been already added!")

    @staticmethod
    def if_race_already_there(name, collection):
        for race in collection:
            if race.race_type == name:
                raise Exception(f"Race {race.race_type} has been already created!")

    @staticmethod
    def if_jockey_not_there(name, collection):
        for jockey in collection:
            if jockey.name == name:
                return jockey
        raise Exception(f"Jockey {name} could not be found!")

    @staticmethod
    def get_horse_if_not_taken(horse_type, collection):
        # for idx in range(len(collection) - 1, -1, -1):
        #     horse = collection[idx]
        #     if horse.__class__.__name__ == horse_type and not horse.is_taken:
        #         return horse
        horse = [el for el in collection if el.__class__.__name__ == horse_type]
        if horse and not horse[-1].is_taken:
            return horse[-1]
        raise Exception(f"Horse breed {horse_type} could not be found!")

    @staticmethod
    def check_if_race_dont_exist(race_type, collection):
        for race in collection:
            if race.race_type == race_type:
                return race
        raise Exception(f"Race {race_type} could not be found!")

    @staticmethod
    def find_winner_by_fastest_horse(collection):
        return sorted(collection, key=lambda x: x.horse.speed, reverse=True)[0]
