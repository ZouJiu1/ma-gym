# ma-gym
Multi Agent Environments for OpenAI gym

## Installation
```bash
cd ma-gym
python setup.py install # use 'develop' instead of 'install' if developing the package
```

## Usage:
```python
import gym
import ma_gym

env = gym.make('CrossOver-v0')
done_n = [False for _ in range(env.n_agents)]
ep_reward = 0

obs_n = env.reset()
while not all(done_n):
    env.render()
    obs_n, reward_n, done_n, info = env.step(env.action_space.sample())
    ep_reward += sum(reward_n)
env.close()
```

Please refer to [Wiki](https://github.com/koulanurag/ma-gym/wiki) for complete usage details

## Environments:
- CrossOver
- Fetch
- Checkers
- PredatorPrey
- Combat
- Traffic Junction

Please refer to [Wiki](https://github.com/koulanurag/ma-gym/wiki) for more details

![CrossOver](static/gif/CrossOver.gif)
![PredatorPrey](static/gif/PredatorPrey5x5.gif)
