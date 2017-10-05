import json

class Cuple():
    def __init__(self, resiver, propouser):
        self.__resiver = resiver
        self.__propouser = propouser

    def __repr__(self):
        return "{} ♥ {}\n".format(self.__resiver.name, self.__propouser.name)


class Person():
    gender = ""

    def __init__(self, person_data):
        self.id = person_data["id"]
        self.name = person_data["name"]
        self.likes = person_data["likes"]
        self.__proposals = []
        self.__best_match = None
        self.__best_match_index = None
        self.__is_propousing = False

    def __repr__(self):
        return "{} - {}".format(self.name, self.gender)

    @property
    def is_propousing(self):
        return self.__is_propousing

    @property
    def areAlone(self):
        return len(self.__proposals) == 0

    @property
    def fisrt_choice(self):
        self.__is_propousing = True
        return self.likes[0]

    @property
    def proposals(self):
        return self.__proposals

    def add_propoisal(self, new_proposal):
        self.__proposals.append(new_proposal)

        match_points = self.__proposals.index(new_proposal)
        if self.__best_match == None:
            self.__best_match_index = new_proposal
            self.__best_match = 0
        elif match_points < self.__best_match:
            self.__best_match_index = new_proposal
            self.__best_match = match_points

    def porpousals_discarted(self):
        discar_propousals = self.__proposals.copy()
        if self.__best_match_index:
            del (discar_propousals[self.__best_match])
            self.__proposals = [self.__best_match_index]
        return discar_propousals

    def remove_first_choice(self):
        self.__is_propousing = False
        del (self.likes[0])

class Parser():
    @classmethod
    def open_json(cls, file_name):
        try:
            with open(file_name + '.json', 'r') as infile:
                group = json.load(infile)
        except Exception:
            return {}
        return cls.sort_dictionari(group, file_name)

    @staticmethod
    def sort_dictionari(group, file_name):
        result = {}
        for person_data in group:
            person = Person(person_data)
            person.gender = file_name
            result[person_data['id']] = person
        return result


class Matcher():
    def __init__(self, propuse_group, resive_group):
        self.__propuse_group = propuse_group
        self.__resive_group = resive_group

    def __all_have_couple(self):
        alone_people = list(filter(lambda x: x.areAlone, self.__resive_group.values()))
        return len(alone_people) == 0

    def __propouse(self):
        for propitizer in self.__propuse_group.values():
            if propitizer.is_propousing:
                continue
            resiver_index = propitizer.fisrt_choice
            self.__resive_group[resiver_index].add_propoisal(propitizer.id)

    def __discard(self):
        for resiver in self.__resive_group.values():
            discar_propousals = resiver.porpousals_discarted()
            for sad_propouser_index in discar_propousals:
                self.__propuse_group[sad_propouser_index].remove_first_choice()

    def match(self):
        while not self.__all_have_couple():
            self.__propouse()
            self.__discard()

        cuples = []
        for resiver in self.__resive_group.values():
            match_index = resiver.proposals[0]
            cuples.append(Cuple(resiver, self.__propuse_group[match_index]))

        return cuples


if __name__ == "__main__":
    propusers = Parser.open_json('male')
    resivers = Parser.open_json('female')
    matcher = Matcher(propusers, resivers)
    print(matcher.match())


# Si las Mujeres proponen
# Blackburn Serrano Brady ♥ Katy Guthrie Jackson
# Hayes Sharp Sutton ♥ Simone Booker Scott
# Frank Christian Valdez ♥ Bettie Yates Rowland
# Rivera Lowery Buckner ♥ Aida Chapman Mercado
# Watkins Bauer Whitley ♥ Linda Osborne Richard

# Si los Hombres proponen
# Allison Estrada Carr ♥ Woods Lynn Ewing
# Megan Contreras Powers ♥ Gonzalez Mcclure Johnston
# Addie Battle Terry ♥ Gutierrez Wilcox Pickett
# Bertie Herman Abbott ♥ Woods Lynn Ewing
