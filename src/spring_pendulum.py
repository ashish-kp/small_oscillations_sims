GlowScript 3.2 VPython

l = 10
eql = 7
theta = 0.5
theta_dot = 0.0
l_dot = 0

ceiling = box(width = 4, height = 0.2, length = 4, pos = vec(0, 3, 0))
m = sphere(radius = 2, color = color.blue, pos = vec(0, -l, 0))
spring = helix(coils = 40, axis = vec(0, -1, 0), pos = vec(0, ceiling.pos.y, 0), radius = 0.4)
#length = abs(m.pos.y - ceiling.pos.y)

m.acc = vec(0, 0, 0)
m.vel = vec(0, 0, 0)

m.mass = 5
spring.k = 1

g = 9.8

dt = 0.03
t = 0

while True:
    rate(300)
    l_ddot = (l * theta_dot**2) + (g * (1 - cos(theta))) - (spring.k * (l - eql) / m.mass)
    theta_ddot = ((-g / l) * sin(theta)) - (l_dot * theta_dot / l)
    l_dot += l_ddot * dt
    theta_dot += theta_ddot * dt
    l += l_dot * dt
    theta += theta_dot * dt
    spring.pos = vec(0, ceiling.pos.y, 0)
    spring.axis = l * vec(sin(theta), -cos(theta), 0)
    m.pos = spring.axis + vec(0, (m.radius / 2), 0)
#    print(l)
    t += dt
