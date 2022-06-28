# TODO

TODO list of steps that should be needed to the model to work correctly.

### Todo

- [X] Modify opts.py
- - [X] Set a new ctdet model called fewnet with opt.heads = {'ss','hm','wh','reg'}
- - [X] Modify dataset settings for new heads and add new parameter to Opts.dataset called fewcoco

- [P] Modify /datasets to new heads
- - [X] Modify /datasets/dataset_factory.py to add new datasets files (fewcoco.py & fewdet.py)
- - [X] Add and modify /datasets/dataset/fewcoco.py to new model
- - [P] Add and modify /datasets/sample/fewdet.py to new model (Check but should be ok)

- [X] Modify /models/networks/pose_dla_dcn.py last layer to add the new parameter ss
- [P] Modify models/decode.py to adapt new model, create losses, etc (Not sure if this file influences the train)
- [X] Modify models/losses.py to adapt new model, create losses, etc (Checked and not needed)

- [P] Modify trains/
- - [P] Add and modify trains/fewdet.py from cdnet.py to adapt new model
- - [X] trains/base_trains.py not necesary to modify, but check it anyways
- - [X] trains/train_factory.py add the new fewdet.py file to the factory list


X = Done
P = Partially Done / Need to be checked