import gym
import random
class RandomActionWrapper(gym.ActionWrapper):
	def __init__(self, env, epsilon = 0.1):
		super(RandomActionWrapper, self).__init__(env)
		self.epsilon = epsilon

	def action(self, action):
		if random.random() < self.epsilon:
			print("Random!")
			return self.env.action_space.sample()
		return action

if __name__ == "__main__":
	env = RandomActionWrapper(gym.make("CartPole-v0"))
	total_reward = 0.0
	total_steps = 0
	obs = env.reset()

	while True:
		obs, reward, done, _ = env.step(0)
		total_reward += reward
		total_steps += 1
		if done:
			break
	print("Episodes done in %d steps, total reward of %.2f" % (total_steps, total_reward))
