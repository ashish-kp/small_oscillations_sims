GlowScript 3.2 VPython
greep = graph(fast = True, xmin = -21, xmax = 21, ymin = -16, ymax = 32, height = 700, width = 700)
f1 = gdots(color = color.red, radius = 0.2)
f2 = gdots(color = color.blue, radius = 0.2)


theta_1 = 0.7
theta_2 = pi / 2

theta_1_dot = 0
theta_2_dot = 0

theta_1_ddot = 0
theta_2_ddot = 0

l1 = 10
l2 = 10

m1 = simple_sphere(radius = 1, color = color.red, pos = vec(0, 0, 0))
m2 = simple_sphere(radius = 1, color = color.blue, pos = vec(0, -5, 0))

rod1 = cylinder(radius = 0.1, axis = vec(0, -1, 0), pos = vec(0, 5, 0), length = l1)
rod2 = cylinder(radius = 0.1, axis = vec(0, -1, 0), pos = vec(0, 0, 0), length = l2)

m1.mass = 1
m2.mass = 1
g = 9.8

dt = 0.01

t = 0

while True:
    rate(300)
    theta_1_ddot = -((m2.mass * l2) / ((m1.mass + m2.mass) * l1)) * ((cos(theta_1 - theta_2) * theta_2_ddot) + (sin(theta_1 - theta_2) * theta_2_dot**2)) - (g * sin(theta_1) / l1)
    theta_2_ddot = (l1 * sin(theta_1 - theta_2) * theta_1_dot**2 / l2) - (l1 * cos(theta_1 - theta_2) * theta_1_ddot / l2) - (g * sin(theta_2) / l2)
    theta_1_dot += theta_1_ddot * dt
    theta_2_dot += theta_2_ddot * dt
    theta_1 += theta_1_dot * dt
    theta_2 += theta_2_dot * dt
    rod1.axis = l1 * vec(sin(theta_1), -cos(theta_1), 0)
    rod2.axis = l2 * vec(sin(theta_2), -cos(theta_2), 0)
    m1.pos = rod1.axis - vec(0, -5, 0)
    rod2.pos = m1.pos
    m2.pos = m1.pos + (l2 * vec(sin(theta_2), -cos(theta_2), 0))
#    f1.plot(m1.pos.x, m1.pos.y) #Uncomment these two lines to see the graph
#    f2.plot(m2.pos.x, m2.pos.y)
    if theta_1_dot > 3:
        t = 0
        theta_1_dot = 0
        theta_2 = 0
    t += dt
