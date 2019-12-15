f = open("wire_path.txt", "r")

path1 = f.readline()
#path1 = "R8,U5,L5,D3"
path1 = path1.split(",")
path2 = f.readline()
#path2 = "U7,R6,D4,L4"
path2 = path2.split(",")

intersection_points = list()

Dx = {'L' : -1, 'R' : 1, 'U' : 0, 'D' : 0}
Dy = {'L' : 0, 'R' : 0, 'U' : 1, 'D' : -1}

def points(path):
    x = 0
    y = 0
    length = 0
    ret = {}

    for i in path:
        d = i[0]
        steps = int(i[1:])

        while steps > 0:
            x += Dx[d]
            y += Dy[d]
            length += 1
            if (x,y) not in ret:
                ret[(x,y)] = length
            steps -= 1

    return ret

points1 = points(path1)
points2 = points(path2)
p = set(points1.keys()) & set(points2.keys())
dist = min([abs(x) + abs(y) for (x,y) in p])
dist2 = min([points1[k] + points2[k] for k in p])
print(dist)
print(dist2)
