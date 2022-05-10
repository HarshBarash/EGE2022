array = ['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']
states_needed = set(array)
stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}
stations_array = []
while states_needed:
    bast_station = None
    states_covered = set()
    for station, state_for_station in stations.items():
        # print(station,state_for_station)
        covered = state_for_station & states_needed

        if len(covered) > len(states_covered):
            bast_station = station
            states_covered = covered
    states_needed = states_needed - states_covered
    # print(states_needed)

    stations_array.append(bast_station)  # station

print(stations_array)
