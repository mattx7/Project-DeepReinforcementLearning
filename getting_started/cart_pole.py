"""
https://gym.openai.com/docs/

Observations
If we ever want to do better than take random actions at each step, it’d probably be good to actually know what our actions are doing to the environment.

The environment’s step function returns exactly what we need. In fact, step returns four values. These are:

* observation (object): an environment-specific object representing your observation of the environment. For example, pixel data from a camera, joint angles and joint velocities of a robot, or the board state in a board game.
* reward (float): amount of reward achieved by the previous action. The scale varies between environments, but the goal is always to increase your total reward.
* done (boolean): whether it’s time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and done being True indicates the episode has terminated. (For example, perhaps the pole tipped too far, or you lost your last life.)
* info (dict): diagnostic information useful for debugging. It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment’s last state change). However, official evaluations of your agent are not allowed to use this for learning.
"""
import gym

env = gym.make('CartPole-v0')


def main():
    for i_episode in range(20):
        observation = env.reset()

        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break


if __name__ == "__main__":
    main()
