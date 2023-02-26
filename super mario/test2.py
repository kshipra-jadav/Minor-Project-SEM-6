from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

class JoypadSpaceWrapper(JoypadSpace):
  def step(self, action):
    obs, reward, done, info = self.env.step(self._action_map[action])
    return obs, reward, done or info.get('life') == 0, info

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpaceWrapper(env, SIMPLE_MOVEMENT)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()