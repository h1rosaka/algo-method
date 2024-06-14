# WA
import numpy as np

N = int(input())

locations = [[] for _ in range(N)]
for i in range(N):
    locations[i] = list(map(int, input().split()))
    


distance = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):

        base_x = locations[i][0]
        base_y = locations[i][1]

        target_x = locations[j][0]
        target_y = locations[j][0]

        current_distance = ((base_x - target_x)**2 + (base_y - target_y)**2)**(1/2)

        distance[i][j] = current_distance



min_dist = (1000*2 + 1000*2)**(1/2)
dist_from_origin = [0 for _ in range(N)]
for i in range(N):
    dist_from_origin[i] = (locations[i][0]**2 + locations[i][1]**2)**(1/2)
    if dist_from_origin[i] < min_dist:
        first_location = locations[i]
        first_location_id = i
        min_dist = dist_from_origin[i]



went = [0 for _ in range(N)]
current_location = first_location
went[first_location_id] = 1
current_location_id = first_location_id
total_distance = 0
total_distance += dist_from_origin[first_location_id]


went_cnt = 1

while went_cnt < N:
    min_dist = (1000*2 + 1000*2)**(1/2)
    # find most close place not went yet
    for i in range(N):
        if went[i] == 1:
            continue
        dist = distance[current_location_id][i]
        if dist < min_dist:
            next_location_id = i
            min_dist = dist
    # move
    total_distance += distance[current_location_id][next_location_id]
    went[next_location_id] = 1
    went_cnt += 1
    current_location_id = next_location_id

# dist to origin
total_distance += dist_from_origin[current_location_id]

print(total_distance)