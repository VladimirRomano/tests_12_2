import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            finished_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(finished_result)

    def setUp(self):
        self.Usain = Runner("Усейн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nick = Runner("Ник", 3)

    def test_usain_nick(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        res1 = tournament.start()
        TournamentTest.all_results.append(res1)
        self.assertEqual(list(res1.values())[-1], self.Nick)

    def test_andrey_nick(self):
        tournament2 = Tournament(90, self.Andrey, self.Nick)
        res2 = tournament2.start()
        TournamentTest.all_results.append(res2)
        self.assertEqual(list(res2.values())[-1], self.Nick)

    def test_usain_andrey_nick(self):
        tournament3 = Tournament(90, self.Andrey, self.Usain, self.Nick)
        res3 = tournament3.start()
        TournamentTest.all_results.append(res3)
        self.assertEqual(list(res3.values())[-1], self.Nick)


if __name__ == '__main__':
    unittest.main()