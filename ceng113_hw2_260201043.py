f = open("provinces.txt")
provinces_dict = {}
for elem in f:          #provinces, latitude, longitude datas
    province, latitude, longitude = elem.split(",")[0],elem.split(",")[1],elem.split(",")[2].split("\n")[0]
    provinces_dict[province] = [float(latitude),float(longitude)]
f.close()
travel_speed_dict = {"CAR": 90, "MOTORCYCLE": 80, "BICYCLE": 25}
departure = input("Departure province:\n").upper()
while departure not in provinces_dict:      # control departure province
    print("Province not found!")
    possible_province = []
    for keys in provinces_dict.keys():
        if keys.startswith(departure):
            possible_province.append(keys)
    if len(possible_province) == 1:
        pos_province = possible_province[0]
        print("Possible province:"+pos_province)
    elif len(possible_province) > 1:
        possible_province = sorted(possible_province)
        suggest = ""
        for x in possible_province:
            suggest = suggest + x + ","
        print("Possible provinces:"+suggest[:-1])
    departure = input("Departure province:\n").upper()
arrival = input("Arrival province:\n").upper()
while arrival not in provinces_dict or arrival == departure:     #control arrival province
    if arrival == departure:
        print("Enter a different province!")
    else:
        print("Province not found!")
        possible_province = []
        for keys in provinces_dict.keys():
            if keys.startswith(arrival):
                possible_province.append(keys)
        if len(possible_province) == 1:
            pos_province = possible_province[0]
            print("Possible province:"+pos_province)
        elif len(possible_province) > 1:
            possible_province = sorted(possible_province)
            suggest = ""
            for x in possible_province:
                suggest = suggest + x + ","
            print("Possible provinces:"+suggest[:-1])
    arrival = input("Arrival province:\n").upper()
travel_type = input("Enter travel type:\n").upper()
while travel_type not in travel_speed_dict:     # control travel type
    travel_type = input("Enter travel type:\n").upper()
x1 = provinces_dict[departure][0]
x2 = provinces_dict[arrival][0]
y1 = provinces_dict[departure][1]
y2  =provinces_dict[arrival][1]
dx = x2 - x1
dy = y2 - y1
distance = ((dx*dx)+(dy*dy))**(0.5)
distance_km = distance * 100
time = distance_km/travel_speed_dict[travel_type]
hours = int(time)
minutes = int((time-hours) * 60)
places_dict = {}        #recommend places
for key,value in provinces_dict.items():
    if key == departure:
        continue
    x2, y2 = float(value[0]),float(value[1])
    dx = x2 - x1
    dy = y2 - y1
    distance =  ((dx*dx)+(dy*dy))**(0.5)
    places_dict[distance] = key
recommend_places = sorted(list(places_dict.keys()))[:3]
recommend_list = []
recommend  = ""
for place in recommend_places:
    recommend_list.append(places_dict[place])
for i in sorted(recommend_list):
    recommend = recommend + i + ","
print("\nI am calculating the distance between {} and {} ...\n".format(departure,arrival))
print("Distance: {:.2f} km".format(distance_km))
print("Approximate travel time with {}: {} hours {} minutes".format(travel_type,hours,minutes))
print("Recommended places close to {}:{}".format(departure,recommend[:-1]))