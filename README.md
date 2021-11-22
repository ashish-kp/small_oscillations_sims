# small_oscillations_sims

Here are the codes for certain very simplistic and ideal physical systems, which I encountered while learning about Small Oscillations. 
Hopefully, I'll write their E.O.Ms here, just for better understandability.

So, the systems are:
1. Two balls attached by a spring. (Let the first ball have a mass m1 and the second ball have a mass m2, and their position co-ordinates be x_1 and x_2, and let the spring have a spring constant k)

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{-k}{m_1}((x_1&space;-&space;x_{01})&space;-&space;(x_2-x_{02})))
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_2=\dfrac{-k}{m_1}((x_2&space;-&space;x_{02})&space;-&space;(x_1-x_{01})))

2. Three balls(with masses m1, m2, m3 and position coordinates x_1, x_2 and x_3 respectively) attached by two springs of different spring constants k_1 and k_2

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{-k_1}{m_1}((x_1-x_{01})&space;-&space;x_2))
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_2=\dfrac{-k_1}{m_1}(x_2-(x_1-x_{01}))-\dfrac{k_2}{m_2}((x_2-x_{03})-x_3))
- ![x_3ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_3=\dfrac{-k_2}{m_3}(x_3-x_{03}-x_2))

3. A system consisting of a wall to which a spring and ball is attached, and at the end of the ball another spring and ball system is attached.

- ![x_1ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{1}{m_1}[(k_2(x_2-x_{02})-(x_1-x_{01}))-(k_1&plus;k_2)(x_1-x_{01})])
- ![x_2ddoteqn](https://latex.codecogs.com/gif.latex?\ddot{x}_1=\dfrac{1}{m_2}[((x_1-x_{01})-(x_2-x_{02}))&plus;(x_1-x_{01})])

4. Two consecutive spring and ball systems suspended from a ceiling, under the action of gravity.

-[y_1ddoteqn]()
