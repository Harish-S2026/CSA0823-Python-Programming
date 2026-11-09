import random
import time

timetable = {
    "12601": {"name": "Chennai Express", "stops": [("Chennai", "06:00", "06:10"), ("Vijayawada", "12:00", "12:05"), ("Howrah", "22:00", "22:10")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}},
    "12602": {"name": "Coastal Express", "stops": [("Chennai", "07:00", "07:15"), ("Nellore", "10:00", "10:05"), ("Vijayawada", "13:00", "13:10")], "days": {"Mon", "Wed", "Fri"}},
    "12603": {"name": "Southern Mail", "stops": [("Bengaluru", "05:00", "05:10"), ("Chennai", "09:00", "09:20"), ("Gudur", "11:00", "11:05")], "days": {"Tue", "Thu", "Sat"}},
    "12604": {"name": "Hill Passenger", "stops": [("Chennai", "08:00", "08:20"), ("Katpadi", "11:00", "11:05"), ("Bengaluru", "14:00", "14:10")], "days": {"Sun", "Tue", "Thu"}},
    "12605": {"name": "Eastern Link", "stops": [("Coimbatore", "04:00", "04:10"), ("Chennai", "10:00", "10:15"), ("Vijayawada", "16:00", "16:05")], "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}}
}

def build_index(data):
    index = {}
    for train, details in data.items():
        for station, arrival, departure in details["stops"]:
            index.setdefault(station, []).append(train)
    return index

def query_station(data, station, day):
    matches = []
    for train, details in data.items():
        if day in details["days"]:
            for stop, arrival, departure in details["stops"]:
                if stop == station:
                    matches.append((departure, train, details["name"]))
    return sorted(matches, key=lambda item: item[0])

def query_with_index(data, index, station, day):
    matches = []
    for train in index.get(station, []):
        details = data[train]
        if day in details["days"]:
            departure = next(departure for stop, arrival, departure in details["stops"] if stop == station)
            matches.append((departure, train, details["name"]))
    return sorted(matches, key=lambda item: item[0])

def generate_timetable(train_count):
    data = {}
    stations = ["Chennai", "Vijayawada", "Bengaluru", "Nellore", "Gudur", "Katpadi"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for number in range(train_count):
        chosen = random.sample(stations, 4)
        stops = [(station, f"{6 + i:02d}:00", f"{6 + i:02d}:05") for i, station in enumerate(chosen)]
        data[str(number)] = {"name": "Train " + str(number), "stops": stops, "days": set(random.sample(days, 5))}
    return data

if __name__ == "__main__":
    index = build_index(timetable)
    print("Chennai on Monday:", query_station(timetable, "Chennai", "Mon"))
    print("Indexed query:", query_with_index(timetable, index, "Chennai", "Mon"))
    print("Unknown station:", query_station(timetable, "Unknown", "Mon"))
    print("Not running day:", query_station(timetable, "Chennai", "Sun"))
    print("Third stop departure:", timetable["12601"]["stops"][2][2])
    random.seed(8)
    for size in (100, 1000, 10000):
        data = generate_timetable(size)
        start = time.perf_counter()
        query_station(data, "Chennai", "Mon")
        scan_time = time.perf_counter() - start
        idx = build_index(data)
        start = time.perf_counter()
        query_with_index(data, idx, "Chennai", "Mon")
        indexed_time = time.perf_counter() - start
        print("Benchmark", size, scan_time, indexed_time)
