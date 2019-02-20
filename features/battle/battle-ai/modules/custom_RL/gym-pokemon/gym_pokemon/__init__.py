from gym.envs.registration import register

register(
	id = 'Pokemon-v0',
	entry_point='gym_pokemon.envs:PokemonEnv',
)