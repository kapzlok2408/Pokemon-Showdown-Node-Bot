import gym
import gym_pokemon
import random

if __name__ == "__main__":
	env = gym.make("Pokemon-v0")
	total_reward = 0.0
	total_steps = 0
	obs = env.reset()

	while True:
		action = random.randint(-1,8)
		obs, reward, done, _ = env.step(action)
		total_reward += reward
		total_steps += 1
		print("Currently %d steps, total reward of %.2f" % (total_steps, total_reward))
		if done:
			break
