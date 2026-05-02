import gymnasium as gym

env = gym.make('MountainCar-v0')


def random_strategy():
    observation, reward = env.reset()

    reward_arr = []
    position_arr = []

    for _ in range(40):
        observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

        reward_arr.append(reward)
        position_arr.append(observation[0])

        if terminated or truncated:
            print('random_strategy Finished: ', 'position:', observation[0], "episod:", _ + 1)
            env.close()
            return reward_arr, position_arr

    env.close()
    return reward_arr, position_arr


def simple_strategy():
    observation, reward = env.reset()

    reward_arr = []
    position_arr = []
    v = observation[1]

    for _ in range(40):
        action = take_action_simple_strategy(v)

        observation, reward, terminated, truncated, info = env.step(action)

        reward_arr.append(reward)
        position_arr.append(observation[0])

        v = observation[1]

        if terminated or truncated:
            print('simple_strategy Finished: ', 'position:', observation[0], "episod:", _ + 1)
            env.close()
            return reward_arr, position_arr

    env.close()
    return reward_arr, position_arr


def take_action_simple_strategy(velocity):
    if velocity < 0:
        return 0
    else:
        return 2
    

def semi_random():
    observation, reward = env.reset()

    reward_arr = []
    position_arr = []
    v = observation[1]

    reward_arr.append(reward)
    position_arr.append(observation[0])
    
    for _ in range(40):

        if v > 0.02:
            observation, reward, terminated, truncated, info = env.step(2)
        elif v < -0.02:
            observation, reward, terminated, truncated, info = env.step(0)
        else:
            observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

        reward_arr.append(reward)
        position_arr.append(observation[0])

        v = observation[1]

        if terminated or truncated:
            print('semi_random strategy Finished: ', 'position:', observation[0], "episod:", _ + 1)
            env.close()
            return reward_arr, position_arr

    env.close()
    return reward_arr, position_arr





if __name__ == "__main__":
    #random_reward_arr, random_position_arr = random_strategy()
    #simple_reward_arr, simple_position_arr = simple_strategy()
    semi_random()




