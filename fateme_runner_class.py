from operator import attrgetter      # for taking attributes from classes
from colorama import Fore            # for print outputs in different colors


# function for sorting list of classes based on its specific attribute
def ranking(members_list, metric, count=None, rev=False):
    sorted_members_list = sorted(members_list, key=attrgetter(metric), reverse=rev)
    return sorted_members_list[:count]


# function for categorize runners with same category in a dictionary:{group:[list of objects or runners]}
def group(rn_class):
    cat = {x.category for x in rn_class}
    group_dict = {}
    for g in cat:
        group_dict[g] = [x for x in rn_class if x.category == g]
    return group_dict


# function: printing list of classes in a table, input: list of classes, output: table
def easy_print(list_class):

    max_str_len = max(len(x.name) for x in list_class)    # find maximum width for table cells

    # print heading of table:
    print(Fore.GREEN, '|', 'runner name', ' ' * (max_str_len - len('runner name')), '|',
          'runner distance', '|',
          'runner duration', '|',
          'runner speed', '|',
          'runner pace', '|',
          'runner category', ' ' * (max_str_len - len('runner category')), '|',
          'runner id', '\n')

    # print rows of table:
    for rnr in list_class:
        print(Fore.RESET, '|', rnr.name, ' ' * (max_str_len - len(rnr.name)), '|',
              rnr.distance, ' ' * (len('runner distance') - 1 - len(str(rnr.distance))), '|',
              rnr.duration, ' ' * (len('runner duration') - 1 - len(str(rnr.duration))), '|',
              rnr.speed, ' ' * (len('runner speed') - 1 - len(str(rnr.speed))), '|',
              rnr.pace, ' ' * (len('runner pace') - 1 - len(str(rnr.pace))), '|',
              rnr.category, ' ' * (max_str_len - len(rnr.category)), '|',
              rnr.runner_id)


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
           {'id': 14, 'name': 'Mohammad Jafar Moradi', 'distance': 42.195, 'duration': 137}]


# each runner a class
class Runner:
    def __init__(self, runner_id, name, distance, duration):
        self.runner_id = runner_id
        self.name = name
        self.distance = distance
        self.duration = duration
        self.speed = round(distance / (duration / 60), 3)
        self.pace = round(duration / distance, 3)

        # define category attribute based on runner's distance
        self.category = 'not finisher' if self.distance <= 10 \
            else '10k' if 10 < self.distance <= 20 \
            else 'half marathon' if 21 <= self.distance <= 41 \
            else 'marathon' if 42 <= self.distance <= 60 \
            else 'ultra'

    def __str__(self):                            # makes attributes of class printable
        return f'{self.runner_id},' \
               f' {self.name}, {self.distance},' \
               f' {self.category} {self.speed},' \
               f' {self.duration},' \
               f' {self.pace}'


# create instances from class Runner
runners_class = []
for person in runners:
    runners_class.append(Runner(person['id'], person['name'], person['distance'], person['duration']))

# Classification of runners, group_class is a dictionary
group_class = group(runners_class)

# print outputs in tables using function easy_print:
print(Fore.CYAN, 'list of all runners:\n', Fore.RESET)
easy_print(runners_class)
print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)

print(Fore.CYAN, 'sorted list of all runners in order of names:\n', Fore.RESET)
easy_print(ranking(runners_class, 'name'))
print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)

print(Fore.CYAN, f'3 faster runner in all:', Fore.RESET)
easy_print(ranking(runners_class, 'speed', 3, True))
print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)

for grp, lst in group_class.items():
    print(Fore.CYAN, f'fastest runner in {grp}:', Fore.RESET)
    easy_print(ranking(lst, "speed", 1, True))
    print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)

    print(Fore.CYAN, f'The most resilient  runner in {grp}:', Fore.RESET)
    easy_print(ranking(lst, "distance", 1, True))
    print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)

print(Fore.CYAN, 'most resilient runner in all:\n', Fore.RESET)
easy_print(ranking(runners_class, 'distance', 1, True))

print(Fore.LIGHTMAGENTA_EX, '*' * 120, '\n', Fore.RESET)
print(Fore.CYAN, 'fastest runner in all:', Fore.RESET)
easy_print(ranking(runners_class, 'speed', 1, True))
