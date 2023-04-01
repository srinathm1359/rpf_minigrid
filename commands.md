## Run experiments on MiniGrid

### Train NovelD on DoorKey6x6
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-DoorKey-5x5-v0 --total_frames 200000 --intrinsic_reward_coef 0.1 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train IMPALA on DoorKey6x6
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-DoorKey-6x6-v0 --total_frames 500000 --intrinsic_reward_coef 0 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train NovelD on LavaGap
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-LavaGapS5-v0 --total_frames 500000 --intrinsic_reward_coef 0.1 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train IMPALA on LavaGap
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-LavaGapS5-v0 --total_frames 500000 --intrinsic_reward_coef 0 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train NovelD on KeyCorridor
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-KeyCorridorS3R2-v0 --total_frames 10000000 --intrinsic_reward_coef 0.1 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train IMPALA on KeyCorridor
```
OMP_NUM_THREADS=1 python main.py --env MiniGrid-KeyCorridorS3R2-v0 --total_frames 10000000 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train NovelD on Unlock
```
OMP_NUM_THREADS=1 python main.py --model bebold --env MiniGrid-Unlock-v0 --total_frames 10000000 --intrinsic_reward_coef 0.1 --entropy_cost 0.0005 --use_lstm --run_id 0
```

### Train IMPALA on Unlock
```
OMP_NUM_THREADS=1 python main.py --env MiniGrid-Unlock-v0 --total_frames 10000000 --entropy_cost 0.0005 --use_lstm --run_id 0
```
