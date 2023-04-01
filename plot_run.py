import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()
env_name = 'DoorKey6x6' # options: DoorKey6x6 or LavaGap5x5 or KeyCorridorS3R2
algo = 'novelD'
seed = '0'
logs_name = 'experiments/' + env_name + '/' + algo + '/' + seed + '/logs.csv'

df = pd.read_csv(logs_name)
# print(df)
# print(df['mean_episode_return'])
returns = df['mean_episode_return'].fillna(0)
frames = df['frames']
plt.plot(frames, returns)
plt.show()