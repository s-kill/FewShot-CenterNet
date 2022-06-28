# TODO

TODO file :)

### Todo

- [X] Modify opts.py
- - [X] Set a new ctdet model with opt.heads = {'ss','hm','wh','reg'}
- - [X] Modify dataset settings for new heads

- [ ] Modify /datasets to new heads
-- [ ] Modify /datasets/dataset_factory.py to add new datasets
-- [ ] Add and modify /datasets/dataset/fewcoco.py to new model
-- [ ] Add and modify /datasets/sample/fewdet.py to new model

- [ ] Modify /models/networks/pose_dla_dcn.py last layer to add the new parameter ss
- [ ] Modify models/decode.py to adapt new model, create losses, etc
- [ ] Modify models/losses.py to adapt new model, create losses, etc

- [ ] Modify trains/
- - [ ] And and modify trains/fewdet.py from cdnet.py to adapt new model
- - [ ] trains/base_trains.py not necesary to modify, but check it anyways
- - [ ] trains/train_factory.py add the new fewdet.py file to the factory list