import math

# get the path of the projectile without wind
def noWindPath(pos, speed, angle, time, gravity):
    v0 = speed[0] * math.cos(angle)
    w0 = speed[1] * math.sin(angle)
    xt = v0 * time + pos[0]
    yt = (-1 / 2) * gravity * math.pow(gravity, 2) + w0 * time + pos[1]
    currentPos = [xt, yt]
    return currentPos

def windPath(pos, speed, angle, time, gravity):