def solution(park, routes):

    len_x = len(park[0])
    len_y = len(park)
    
    for i in range(len_y):
        if park[i].find('S') != -1 : 
            location_x = park[i].index('S')
            location_y = i
        

    for route in routes:
        direction, distance_str = route.split()
        distance = int(distance_str)

        if direction == 'E':
            if location_x + distance < len_x:
                for i in range(location_x+1, location_x + distance+1):
                    if park[location_y][i] == 'X':
                        break
                else:
                    location_x += distance

        elif direction == 'N':
            if location_y - distance >= 0:
                for i in range(location_y-1, location_y - distance -1, -1):
                    if park[i][location_x] == 'X':
                        break
                else:
                    location_y -= distance

        elif direction == 'S':
            if location_y + distance < len_y:
                for i in range(location_y+1, location_y + distance+1):
                    if park[i][location_x] == 'X':
                        break
                else:
                    location_y += distance

        elif direction == 'W':
            if location_x - distance >= 0:
                for i in range(location_x-1, location_x - distance-1, -1):
                    if park[location_y][i] == 'X':
                        break
                else:
                    location_x -= distance

    answer = [location_y, location_x]
    return answer