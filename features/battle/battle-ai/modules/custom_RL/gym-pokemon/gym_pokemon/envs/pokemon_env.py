import gym
from gym import error, spaces, utils
from gym.utils import seeding
import json
import time

class PokemonEnv(gym.Env):
	metadata = {'render.modes':['human']}
	
	#up to 4 moves and 5 pokemon switches
	action_space = spaces.Discrete(n=9)
	#for now, observation_space will not be implemented
	observation_space = spaces.Discrete(n=1)
	rlDataJson = "/home/alex/Pokemon-Showdown-Node-Bot/features/battle/battle-ai/modules/rldata.json"

	def __init__(self):
		#opens the json file for reading, converting into a dictionary
		dataFile = open(self.rlDataJson,"r")
		self.state = json.loads(dataFile.read())
		



	def step(self, action):
		#open the json file to write action into file
		dataFile = open(self.rlDataJson, "w")
		#because dictionary is immutable, instead make new dictionary
		self.state = {
			'battleDecisions': self.state["battleDecisions"],
			'battleData': self.state["battleData"],
			'actionReturned': True,
			'pythonStarted': self.state["pythonStarted"],
			'action': action
		}
		#dump the dictionary into the opened file
		json.dump(self.state, dataFile)
		dataFile.close()
		#wait for 'actionReturned' to be false again
		time.sleep(3)
		while(True):
			#need to wait sometime here to prevent overload
			#if actionReturned is back to false, exit the loop
			dataFile = open(self.rlDataJson, "r")
			self.state = json.loads(dataFile.read())
			dataFile.close()
			if(not self.state["actionReturned"]):
				break
		return [self.state, self.getReward(), False, None]

		"""
        The agent takes a step in the environment.

        Parameters
        ----------
        action : int

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                an environment-specific object representing your observation of
                the environment.
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """


	def reset(self):
		dataFile = open(self.rlDataJson,"r")
		self.state = json.loads(dataFile.read())
		return [self.state, self.getReward(), False, None]
		"""
		should do nothing as the the environment is reset externally
		could be instead used to split one battle into separate episodes
		or to return the current state without stepping
		"""


	def render(self, mode = 'human', close = False):
		pass

	def getReward(self):
		#should evaluate reward based on current state
		return 1

