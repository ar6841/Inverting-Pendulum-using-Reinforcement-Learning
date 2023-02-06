# Inverting-Pendulum-using-Reinforcement-Learning

Simulation of pendulum trying to balance itself in an inverted position.

The optimum control policy is found using Q-learning with an epsilon greedy policy.





https://user-images.githubusercontent.com/96152967/216857971-7efe3fd9-a714-4ef3-a595-caff0712cbbf.mp4





## Simulation setup

The pendulum is in a configuration as shown below:

![image](https://user-images.githubusercontent.com/96152967/216853308-3bdda7c6-c78b-41cf-922a-e5c636c7ded1.png)

Let the state vector of the pendulum $x$ be given by:

$$
x=\left(\begin{array}{l}
\theta \\
\omega
\end{array}\right)
$$

Where $\theta$ and $\omega$ are the angle from the vertical and angular velocity of the pendulum respectively. 


We want to minimize the following discounted cost function 

$$
\sum_{i=0}^{\infty} \alpha^i g\left(x_i, u_i\right)
$$

Where, 

$$
g\left(x_i, u_i\right)=(\theta-\pi)^2+0.01 \cdot \dot{\theta}_i^2+0.0001 \cdot u_i^2 \quad \text { and } \quad \alpha=0.99
$$

## Results
The results vary upon changing the learning parametes. In this example:
$$
\begin{gathered}
\epsilon=0.00001, \text { learning rate }=1 \\
u \in\{-4,0,4\}
\end{gathered}
$$

Where $\epsilon$ is the epsilon greedy parameter (how much randomness we want while learning) and $u$ is the possible controls vector

The following graph shows the episode number (x axis) vs episode cost (y axis):

![image](https://user-images.githubusercontent.com/96152967/216853227-d7bf2a14-e56a-4f78-a8f5-52d8833f3b66.png)

The state vector during the optimal control sequence:

![image](https://user-images.githubusercontent.com/96152967/216853237-ec2020f0-d5dc-4f30-b767-caaad65455cf.png)

The value function for each (velocity, pendulum angle):

![image](https://user-images.githubusercontent.com/96152967/216853260-7c3cfcbb-4348-45f8-a0ce-3e3c0a5fb507.png)

The policy found for each (velocity, pendulum angle):

![image](https://user-images.githubusercontent.com/96152967/216853272-8d378197-8ccc-4219-8008-20d5caf2f266.png)
