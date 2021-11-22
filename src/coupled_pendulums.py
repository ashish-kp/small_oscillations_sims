GlowScript 3.2 VPython
greeph = graph(fast = True)
f1 = gcurve(color = color.red)
f2 = gcurve(color = color.blue)

l1 = 7
l2 = 7

ceiling = box(width = 2, height = 0.2, length = 10, pos = vec(0, 5, 0))
m1 = sphere(radius = 1, pos = vec(-4, 5 - l1, 0), color = color.red)
m2 = sphere(radius = 1, pos = vec(4, 5 - l2, 0), color = color.blue)

rope1 = cylinder(radius = 0.1, axis = vec(0, -1, 0), pos = vec(-4, 5, 0), length = l1)
rope2 = cylinder(radius = 0.1, axis = vec(0, 1, 0), pos = vec(4, 5, 0), length = l2)

spring = helix(coils = 30, radius = 0.3,pos = vec(m1.pos.x, m1.pos.y, 0) ,axis = hat(m2.pos - m1.pos), length = abs(sqrt((m1.pos.x - m2.pos.x)**2 + (m1.pos.y - m2.pos.y)**2)))

theta_1 = 0.01
theta_2 = -0.04
theta_1_dot = 0
theta_2_dot = 0

m1.vel = vec(0, 0, 0)
m2.vel = vec(0, 0, 0)
m1.acc = vec(0, 0, 0)
m2.acc = vec(0, 0, 0)

m1.mass = 2
m2.mass = 2

spring.k = .4
g = 9.8

dt = 0.05
t = 0

while True:
    rate(300)
    theta_1_ddot = ((-m1.mass * g * l1 * sin(theta_1)) - (spring.k * l1 * cos(theta_1) * (l1 * sin(theta_1) - l2 * sin(theta_2)))) / (m1.mass * l1**2)
    theta_2_ddot = ((-m2.mass * g * l2 * sin(theta_2) + (spring.k * l2 * cos(theta_2) * (l1 * sin(theta_1) - l2 * sin(theta_2))))) / (m2.mass * l2**2)
    theta_1_dot += theta_1_ddot * dt
    theta_2_dot += theta_2_ddot * dt
    theta_1 += theta_1_dot * dt
    theta_2 += theta_2_dot * dt
    m1.pos.x = l1 * sin(theta_1) - 4
    m2.pos.x = l2 * sin(theta_2) + 4
    m1.pos.y = -l1 * cos(theta_1) + 5
    m2.pos.y = -l2 * cos(theta_2) + 5
    rope1.axis = vec(m1.pos.x + 4, m1.pos.y - 5, 0)
    rope2.axis = vec(m2.pos.x - 4, m2.pos.y - 5, 0)
    spring.pos = vec(m1.pos.x, m1.pos.y, 0)
    spring.axis = (m2.pos - m1.pos)
    #f1.plot(t, theta_1)
    #f2.plot(t, theta_2)
    t += dt
