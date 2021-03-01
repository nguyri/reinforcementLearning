import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    #env = gym.wrappers.Monitor(env, "recording", force=True)

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        env.render()
        # render seems to work on windows after installing and running vcXsrv
        # https://sourceforge.net/projects/vcxsrv/
        # or does it just work by itself?
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))

    input()
    env.close()
    env.env.close()

