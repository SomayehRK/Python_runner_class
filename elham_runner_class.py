from operator import attrgetter

runners = [{'name': 'Kilian Jornet', 'distance': 46, 'duration': 283},
           {'name': 'Akbar Naghdi', 'distance': 120, 'duration': 720},
           {'name': 'Negar sammak Nejad', 'distance': 171, 'duration': 2760},
           {'name': 'Mandana Nouri', 'distance': 21.0975, 'duration': 118},
           {'name': 'Eliud Kipchoge ', 'distance': 42.195, 'duration': 119},
           {'name': 'Julius PASKOV', 'distance': 86.3, 'duration': 870},
           {'name': 'Anabela RENDA', 'distance': 25.7, 'duration': 195},
           {'name': 'Alexis SEVENNEC', 'distance': 24.1, 'duration': 140},
           {'name': 'Joyciline Jepkosgei', 'distance': 10, 'duration': 28},
           {'name': 'Rhonex Kipruto', 'distance': 10, 'duration': 26},
           {'name': 'Vincent Kibet', 'distance': 10, 'duration': 27},
           {'name': 'Senbere Teferi', 'distance': 10, 'duration': 30.2},
           {'name': 'Payam Dibaj', 'distance': 30, 'duration': 152},
           {'name': 'Sepideh Nouri', 'distance': 27, 'duration': 142},
           {'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]


class Runner:
    def __init__(self, name, distance, duration, id):
        self.name = name
        self.distance = distance
        self.duration = duration
        self.id = id
        self.speed = round(distance / (duration / 60), 3)
        self.pace = round((duration / distance), 3)

    def categorize(self):
        self.category = 'not finisher' if self.distance < 10 \
            else '10k' if 10 <= self.distance <= 20 \
            else 'half marathon' if 21 <= self.distance <= 41 \
            else 'marathon' if 42 <= self.distance <= 60 \
            else 'ultra'
        return self.category

    def __str__(self):
        return f'{self.id},{self.name}, {self.distance}, {self.categorize()}, {self.speed}, {self.duration}, {self.pace}'


def ranking(members_list, metric, count=None):
    members_list = sorted(members_list, key=attrgetter(metric), reverse=True)
    return members_list[:count]


def sort_name(members_list, metric):
    members_list = sorted(members_list, key=attrgetter(metric))
    return members_list[:]


def bestrunner_category(members_list, metric, name_category, count=None):
    members_category = list(map(lambda x: x if x.categorize() == name_category else 1, members_list))
    obj_list=[]
    for i in members_category:
        if i!=1:
            obj_list.append(i)
    members_list = sorted(obj_list, key=attrgetter(metric), reverse=True)
    if members_list!=[]:
        print(f'{name_category}--->name:{members_list[0].name},speed:{members_list[0].speed}')


id = 0
runners_class = []
name = []
for person in runners:
    if person['name'] in name:
        print(f' You can not register twice')
    else:
        runners_class.append(Runner(person['name'], person['distance'], person['duration'], id))
        id += 1
        name.append(person['name'])

print('print name all runners:')
for i in runners_class:
    print(i.__str__())

print('print name sorted:')
name_sort_runners = sort_name(runners_class, 'name')
for i in name_sort_runners:
    print(f'name:{i.__str__()}')

print('print The first three in speed:')
rank_speed = ranking(runners_class, 'speed', 3)
for i in rank_speed:
    print(f'name runner most speed:{i.name}, speed:{i.speed}')

print('print The first in distance:')
rank_dis = ranking(runners_class, 'distance', 1)
for i in rank_dis:
    print(f'name runner most distance:{i.name}, distance:{i.distance}')

print('print fastest runner:')
rank_dis = ranking(runners_class, 'speed', 1)
for i in rank_dis:
    print(f'name runner most speed:{i.name}, speed:{i.distance}')

print('print best runner category in speed:')
bestrunner_category(runners_class, 'speed', 'not finisher', 1)
bestrunner_category(runners_class, 'speed', '10k', 1)
bestrunner_category(runners_class, 'speed', 'half marathon', 1)
bestrunner_category(runners_class, 'speed', 'marathon', 1)
bestrunner_category(runners_class, 'speed', 'ultra', 1)


