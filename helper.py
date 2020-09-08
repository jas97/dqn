import glob
import gym
from IPython.display import HTML
from IPython import display as ipythondisplay


# getting gym environment
def get_env(env_name):
    return gym.make(env_name)


# showing the video saved at ./video/ location
def show_video(directory):
    video_list = glob.glob('{}/*.mp4'.format(directory))
    print(video_list)
    if len(video_list) > 0:
        ipythondisplay.display(HTML("""
                                    <video alt="test" controls>
                                        <source src="{}" type="video/mp4">
                                    </video>
                                """.format(video_list[0])))
    else:
        print('No videos found.')

# plays and episode in environment always choosing random next action
def play_random_episode(env):
    done = False
    cnt = 0
    total_reward = 0
    while not done:
        cnt += 1
        action = env.action_space.sample()
        observation, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break
    print("number of steps: {}".format(cnt))
    print('Total reward: {}'.format(total_reward))
    env.close()
