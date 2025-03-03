import logging

from gym import envs
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Register openai's environments as multi agent
# This should be done before registering new environments
env_specs = [env_spec for key, env_spec in envs.registry.items() if 'gym.envs' in env_spec.entry_point]
for spec in env_specs:
    register(
        id='ma_' + spec.id,
        entry_point='ma_gym.envs.openai:MultiAgentWrapper',
        kwargs={'name': spec.id, **spec.kwargs}
    )

# add new environments : iterate over full observability
for i, observability in enumerate([False, True]):
    register(
        id='CrossOver-v' + str(i),
        entry_point='ma_gym.envs.crossover:CrossOver',
        kwargs={'full_observable': observability, 'step_cost': -0.5}
    )

    register(
        id='Checkers-v' + str(i),
        entry_point='ma_gym.envs.checkers:Checkers',
        kwargs={'full_observable': observability}
    )

    register(
        id='Switch2-v' + str(i),
        entry_point='ma_gym.envs.switch:Switch',
        kwargs={'n_agents': 2, 'full_observable': observability, 'step_cost': -0.1}
    )
    register(
        id='Switch4-v' + str(i),
        entry_point='ma_gym.envs.switch:Switch',
        kwargs={'n_agents': 4, 'full_observable': observability, 'step_cost': -0.1}
    )

    register(
        id='TrafficJunction-v' + str(i),
        entry_point='ma_gym.envs.traffic_junction:TrafficJunction',
        kwargs={'full_observable': observability}
    )

    register(
        id='Lumberjacks-v' + str(i),
        entry_point='ma_gym.envs.lumberjacks:Lumberjacks',
        kwargs={'full_observable': observability}
    )


register(
    id='Combat-v0',
    entry_point='ma_gym.envs.combat:Combat',
)
register(
    id='PongDuel-v0',
    entry_point='ma_gym.envs.pong_duel:PongDuel',
)

for game_info in [[(5, 5), 2, 1], [(7, 7), 4, 2]]:  # [(grid_shape, predator_n, prey_n),..]
    grid_shape, n_agents, n_preys = game_info
    _game_name = 'PredatorPrey{}x{}'.format(grid_shape[0], grid_shape[1])
    register(
        id='{}-v0'.format(_game_name),
        entry_point='ma_gym.envs.predator_prey:PredatorPrey',
        kwargs={
            'grid_shape': grid_shape, 'n_agents': n_agents, 'n_preys': n_preys
        }
    )
    # fully -observable ( each agent sees observation of other agents)
    register(
        id='{}-v1'.format(_game_name),
        entry_point='ma_gym.envs.predator_prey:PredatorPrey',
        kwargs={
            'grid_shape': grid_shape, 'n_agents': n_agents, 'n_preys': n_preys, 'full_observable': True
        }
    )

    # prey is initialized at random location and thereafter doesn't move
    register(
        id='{}-v2'.format(_game_name),
        entry_point='ma_gym.envs.predator_prey:PredatorPrey',
        kwargs={
            'grid_shape': grid_shape, 'n_agents': n_agents, 'n_preys': n_preys,
            'prey_move_probs': [0, 0, 0, 0, 1]
        }
    )

    # full observability + prey is initialized at random location and thereafter doesn't move
    register(
        id='{}-v3'.format(_game_name),
        entry_point='ma_gym.envs.predator_prey:PredatorPrey',
        kwargs={
            'grid_shape': grid_shape, 'n_agents': n_agents, 'n_preys': n_preys, 'full_observable': True,
            'prey_move_probs': [0, 0, 0, 0, 1]
        }
    )
