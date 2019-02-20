import gym
import gym_pokemon

env = gym.make('Pokemon-v0')
env.step(1)
print(env.state)