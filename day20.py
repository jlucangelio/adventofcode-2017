from collections import namedtuple

Vector = namedtuple("Vector", "x y z")
Particle = namedtuple("Particle", "pos v a")

def vector_from_s(s):
    cs = s.split('=')[1][1:-1]
    x, y, z = [int(c) for c in cs.split(',')]
    return Vector(x, y, z)


def move_once(part):
    new_v = Vector(part.v.x + part.a.x, part.v.y + part.a.y, part.v.z + part.a.z)
    new_pos = Vector(part.pos.x + new_v.x, part.pos.y + new_v.y, part.pos.z + new_v.z)
    return part._replace(pos=new_pos, v=new_v)


def distance(part):
    return sum([int(abs(c)) for c in part.pos])


particles = []
with open("day20.input") as f:
    for line in f.readlines():
        # p=<2366,784,-597>, v=<-12,-41,50>, a=<-5,1,-2>
        sp, sv, sa = line.strip().split(", ")

        pos = vector_from_s(sp)
        v = vector_from_s(sv)
        a = vector_from_s(sa)

        particles.append(Particle(pos, v, a))

closest_list = []
for i in range(1000):
    closest_index = 0
    closest_dist = 0
    for j, _ in enumerate(particles):
        part = move_once(particles[j])
        particles[j] = part

        if distance(particles[closest_index]) > distance(part):
            closest_index = j
            closest_dist = distance(part)

    closest_list.append((closest_index, closest_dist))

print closest_list
