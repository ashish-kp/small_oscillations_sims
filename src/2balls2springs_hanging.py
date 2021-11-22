GlowScript 3.2 VPython
greeph = graph(fast = True)
f1 = gdots(color = color.red, radius = 0.1)
f2 = gdots(color = color.blue, radius = 0.1)

eq1 = 0
eq2 = -5


ceiling = box(width = 3, height = 0.2, length = 2, pos = vec(0, 5, 0))
m1 = sphere(radius = 1, pos = vec(0, eq1 - 1, 0), color = color.red)
m2 = sphere(radius = 1, pos = vec(0, eq2, 0), color = color.blue)

spring1 = helix(radius = 0.2, coils = 20, length = abs(ceiling.pos.y - m1.pos.y), axis = vec(0, -1, 0), pos = vec(0, ceiling.pos.y, 0), color = color.orange)
spring2 = helix(radius = 0.2, coils = 20, length = abs(m1.pos.y - m2.pos.y), axis = vec(0, -1, 0), pos = vec(0, m1.pos.y, 0), color = color.green)

m1.vel = vec(0, 0, 0)
m2.vel = vec(0, 0, 0)
m1.acc = vec(0, 0, 0)
m2.acc = vec(0, 0, 0)

m1.mass = 1
m2.mass = 1

spring1.k = 20
spring2.k = 15

g = 9.8

dt = 0.01
t = 0

while True:
    rate(300)
#    m1.acc.y = (((-spring1.k * (m1.pos.y - eq1)) + (spring2.k * ((m2.pos.y - eq2) - (m1.pos.y - eq1)))) / (m1.mass)) - g
    m1.acc.y = (((-spring1.k * (m1.pos.y - eq1)) + (spring2.k * ((m2.pos.y - (m1.pos.y + eq2)) - (m1.pos.y - eq1)))) / (m1.mass)) - ((m1.mass + m2.mass) / m1.mass) * g
#    m2.acc.y = ((-spring2.k * ((m2.pos.y - eq2) - (m1.pos.y - eq1))) / (m2.mass)) - g
#    m2.acc.y = ((-spring2.k * ((m2.pos.y - (m1.pos.y + eq2)) - (m1.pos.y - eq1))) / (m2.mass)) - g
    m2.acc.y = ((-spring2.k * ((m2.pos.y - eq2) - (2 * m1.pos.y - eq1))) / (m2.mass)) - g
    m1.vel.y += m1.acc.y * dt
    m2.vel.y += m2.acc.y * dt
    m1.pos.y += m1.vel.y * dt
    m2.pos.y += m2.vel.y * dt
    spring1.pos.y = ceiling.pos.y
    spring2.pos.y = m1.pos.y
    spring1.length = abs(ceiling.pos.y - m1.pos.y)
    spring2.length = abs(m1.pos.y - m2.pos.y)
    f1.plot(t, m1.pos.y)
    f2.plot(t, m2.pos.y)
    t += dt
    
    
