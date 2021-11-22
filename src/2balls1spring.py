GlowScript 3.2 VPython

eq1 = -5
eq2 = 5

m1 = sphere(pos = vec(eq1 - 1, 0, 0), radius = 1, color = color.red)
m2 = sphere(pos = vec(eq2 + 1, 0, 0), radius = 1, color = color.blue)

spring = helix(axis = vec(1, 0, 0), length = 9, pos = vec(-4.5, 0, 0), radius = 0.2, coils = 20)

m1.mass = 1
m2.mass = 3
m1.acc = vec(0, 0, 0)
m2.acc = vec(0, 0, 0)
m1.vel = vec(0, 0, 0)
m2.vel = vec(0, 0, 0)

spring.k = 1

dt = 0.1
t = 0

while True:
  rate(300)
  m1.acc.x = -spring.k * ((m1.pos.x - eq1) - (m2.pos.x - eq2)) / m1.mass
  m2.acc.x = spring.k * ((m1.pos.x - eq1) - (m2.pos.x - eq2)) / m2.mass
  m1.vel.x += m1.acc.x * dt
  m2.vel.x += m2.acc.x * dt
  m1.pos.x += m1.vel.x * dt
  m2.pos.x += m2.vel.x * dt
  spring.length = abs(m1.pos.x - m2.pos.x)
  spring.pos = vec(-spring.length / 2, 0, 0)
  t += dt
