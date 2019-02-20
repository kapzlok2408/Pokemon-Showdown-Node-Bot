import gym

if __name__ == "__main__":
	env = gym.make("CartPole-v0")
	env = gym.wrappers.Monitor(env, "monitor")
	total_reward = 0.0
	total_steps = 0
	obs = env.reset()

	while True:
		action = env.action_space.sample()
		obs, reward, done, _ = env.step(action)
		env.render()
		total_reward += reward
		total_steps += 1
		if done:
			break
	print("Episodes done in %d steps, total reward of %.2f" % (total_steps, total_reward))
