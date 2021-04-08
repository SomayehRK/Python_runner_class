from operator import attrgetter

runners = [{'id': 0, 'name': 'Kilian Jornet', 'distance': 46, 'duration': 283},
          {'id': 1, 'name': 'Akbar Naghdi', 'distance': 120, 'duration': 720},
          {'id': 2, 'name': 'Negar sammak Nejad', 'distance': 171, 'duration': 2760},
          {'id': 3, 'name': 'Mandana Nouri', 'distance': 21.0975, 'duration': 118},
          {'id': 4, 'name': 'Eliud Kipchoge ', 'distance': 42.195, 'duration': 119},
          {'id': 5, 'name': 'Julius PASKOV', 'distance': 86.3, 'duration': 870},
          {'id': 6, 'name': 'Anabela RENDA', 'distance': 25.7, 'duration': 195},
          {'id': 7, 'name': 'Alexis SEVENNEC', 'distance': 24.1, 'duration': 140},
          {'id': 8, 'name': 'Joyciline Jepkosgei', 'distance': 10, 'duration': 28},
          {'id': 9, 'name': 'Rhonex Kipruto', 'distance': 10, 'duration': 26},
          {'id': 10, 'name': 'Vincent Kibet', 'distance': 10, 'duration': 27},
          {'id': 11, 'name': 'Senbere Teferi', 'distance': 10, 'duration': 30.2},
          {'id': 12, 'name': 'Payam Dibaj', 'distance': 30, 'duration': 152},
          {'id': 13, 'name': 'Sepideh Nouri', 'distance': 27, 'duration': 142},
          {'id': 14, 'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137},
           {'id': 14, 'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]


class Runner:
    def __init__(self, ID, name, distance, duration):
        self.ID = ID
        self.name = name
        self.distance = distance
        self.duration = duration
        self.speed = round(distance / (duration / 60), 3)
        self.pace = round((duration / distance), 3)

    def classify(self):
        self.Class = 'not finisher' if self.distance < 10 \
            else '10k' if 10 <= self.distance <= 20 \
            else 'half marathon' if 21 <= self.distance <= 41 \
            else 'marathon' if 42 <= self.distance <= 60 \
            else 'ultra'

        return self.Class

    def __str__(self):
        return f'{self.ID}:name: {self.name}, distance:{self.distance}, Class:{self.classify()},' \
               f' speed:{self.speed}, pace:{self.duration}, {self.pace}'


def ranking(members_list, metric, descending, count=None):
    members_list = sorted(members_list, key=attrgetter(metric), reverse=descending)
    return members_list[:count]


def categorizing(members_list):
    categorized_runner = {}
    category = {x.classify() for x in members_list}
    for group in category:
        categorized_runner[group] = [x for x in members_list if x.Class == group]
        sort_runner = ranking(categorized_runner[group], 'speed', True, 3)
        print(f'\nThe three fastest runners in the {group} group:')
        for n in sort_runner:
            print(f'{n.ID}: {n.name} with speed = {n.speed}')


runners_class = []
for person in runners:
    if person['name'] not in runners_class:
        runners_class.append(Runner(person['id'], person['name'], person['distance'], person['duration']))
    else:
        print('you can not register.')
for i in runners_class:
    print(i.__str__())

print('\nNames of runners in alphabetical order: ')
sorted_runners = ranking(runners_class, 'name', descending=False)
for runner in sorted_runners:
    print(runner.ID , ': ',runner.name)

rank_speed = ranking(runners_class, 'speed', True, 3)
print('\nthree faster runners:')
for i in rank_speed:
    print(f'{i.ID}: {i.name} with speed = {i.speed}')
print(f'\nThe fastest runner in the whole race is: {rank_speed[0].name} with speed = {rank_speed[0].speed}')

categorizing(runners_class)

rank_dis = ranking(runners_class, 'distance', True)
print(f'\nRunner with the longest distance is : {rank_dis[0].name} with distance = {rank_dis[0].distance}')


