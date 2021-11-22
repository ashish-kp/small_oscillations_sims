GlowScript 3.2 VPython
eq1 = -5
eq2 = 0
eq3 = 5

m1 = sphere(radius = 1, pos = vec(eq1 + 1, 0, 0), color = color.red)
m2 = sphere(radius = 1, pos = vec(eq2, 0, 0), color = color.green)
m3 = sphere(radius = 1, pos = vec(eq3, 0, 0), color = color.blue)

spring1 = helix(axis = vec(1, 0, 0), coils = 20, radius = 0.2, color = color.orange, length = abs(m1.pos.x - m2.pos.x), pos = vec(m1.pos.x, 0, 0))
spring2 = helix(axis = vec(1, 0, 0), coils = 20, radius = 0.2, color = vec(1, 0, 1), length = abs(m2.pos.x - m3.pos.x), pos = vec(m2.pos.x, 0, 0))

m1.vel = vec(0, 0, 0)
m2.vel = vec(0, 0, 0)
m3.vel = vec(0, 0, 0)
m1.acc = vec(0, 0, 0)
m2.acc = vec(0, 0, 0)
m3.acc = vec(0, 0, 0)

m1.mass = 1
m2.mass = 3
m3.mass = 2

spring1.k = 2
spring2.k = 2

dt = 0.05

t = 0

while True:
    rate(300)
    m1.acc.x = (spring1.k / m1.mass) * ((m2.pos.x) - (m1.pos.x - eq1))
    m2.acc.x = ((-spring1.k / m2.mass) * ((m2.pos.x) - (m1.pos.x - eq1))) + ((spring2.k / m2.mass) * ((m3.pos.x - (m2.pos.x + eq3)) - (m2.pos.x)))
    m3.acc.x = (-spring2.k / m3.mass) * ((m3.pos.x - m2.pos.x - eq3))
#    m3.acc.x = (-spring2.k / m3.mass) * ((m3.pos.x - (m2.pos.x + eq3)) - (m2.pos.x))
    m1.vel.x += m1.acc.x * dt
    m2.vel.x += m2.acc.x * dt
    m3.vel.x += m3.acc.x * dt
    m1.pos.x += m1.vel.x * dt
    m2.pos.x += m2.vel.x * dt
    m3.pos.x += m3.vel.x * dt
    spring1.pos.x = m1.pos.x
    spring2.pos.x = m2.pos.x
    spring1.length = abs(m1.pos.x - m2.pos.x)
    spring2.length = abs(m2.pos.x - m3.pos.x)
    t += dt
