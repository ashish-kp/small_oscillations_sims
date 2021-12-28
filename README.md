# small_oscillations_sims

Here are the codes for certain very simplistic and ideal physical systems, which I encountered while learning about Small Oscillations. 
Hopefully, I'll write their E.O.Ms here, just for better understandability.

So, the systems are:
1. Two balls attached by a spring. (Let the first ball have a mass m1 and the second ball have a mass m2, and their position co-ordinates be x_1 and x_2, and let the spring have a spring constant k) [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/2balls1spring)

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{-k}{m_1}((x_1&space;-&space;x_{01})&space;-&space;(x_2-x_{02})))
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_2=\dfrac{-k}{m_1}((x_2&space;-&space;x_{02})&space;-&space;(x_1-x_{01})))

2. Three balls(with masses m1, m2, m3 and position coordinates x_1, x_2 and x_3 respectively) attached by two springs of different spring constants k_1 and k_2 [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/3balls2springs)

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{-k_1}{m_1}((x_1-x_{01})&space;-&space;x_2))
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_2=\dfrac{-k_1}{m_1}(x_2-(x_1-x_{01}))-\dfrac{k_2}{m_2}((x_2-x_{03})-x_3))
- ![x_3ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_3=\dfrac{-k_2}{m_3}(x_3-x_{03}-x_2))

3. A system consisting of a wall to which a spring and ball is attached, and at the end of the ball another spring and ball system is attached. [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/wall2balls2springs)

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{1}{m_1}[(k_2(x_2-x_{02})-(x_1-x_{01}))-(k_1&plus;k_2)(x_1-x_{01})])
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{1}{m_2}[((x_1-x_{01})-(x_2-x_{02}))&plus;(x_1-x_{01})])

4. Two consecutive spring and ball systems suspended from a ceiling, under the action of gravity. [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/hanging2balls2springs)

- ![y_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{y}_1&space;=&space;\dfrac{1}{m_1}[(k_1(y_1-y_{01}))&plus;(k_2(y_2-(y_1&plus;y_{02}))-(y_1-y_{01}))-(m_1&space;&plus;m_2)g])
- ![y_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{y}_2=\dfrac{-k_2}{m_2}(y_2-(y_1&plus;y_{02})-(y_1-y_{01}))-g)

5. Spring Pendulum [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/springpendulum)

- ![l_ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{l}=l\dot{\theta}^2&plus;g(1-cos\theta)-\dfrac{k}{m}(l-l_0))
- ![theta_ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{\theta}=-\dfrac{g}{l}sin\theta-\dfrac{\dot{l}\dot{\theta}}{l})

6. Two simple pendulums coupled through a spring, attached to the masses. [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/coupledpendulums)

- ![theta1_ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{\theta}_1=-\dfrac{g}{l_1}&space;sin\theta_1-\dfrac{k}{m_1}cos\theta_1(sin\theta_1-\dfrac{l_2}{l_1}sin\theta_2)])
- ![theta2_ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{\theta}_2=-m_2&space;\dfrac{g}{l_2}sin\theta_2&space;-&space;\dfrac{k}{m_2}cos\theta_2(sin\theta_2-\dfrac{l_1}{l_2}sin\theta_1))

7. Double Pendulum [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/onlysmalloscillations/program/doublependulum)

While double pendulum needs a seperate section for it's own, as of yet, it shall be a part of this repo. The double pendulum is the go-to example when people think of chaos and randomness.
