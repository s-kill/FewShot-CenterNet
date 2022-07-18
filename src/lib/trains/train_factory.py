from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .ctdet import CtdetTrainer
from .ctdetv2 import CtdetTrainer as CtdetTrainerv2
from .fewdet import FewdetTrainer
from .fewdetv2 import FewdetTrainer as FewdetTrainerv2
from .fewdetv3 import FewdetTrainer as FewdetTrainerv3
from .ddd import DddTrainer
from .exdet import ExdetTrainer
from .multi_pose import MultiPoseTrainer

train_factory = {
  'exdet': ExdetTrainer, 
  'ddd': DddTrainer,
  'ctdet': CtdetTrainer,
  'ctdetv2': CtdetTrainerv2,
  'fewdet': FewdetTrainer,
  'fewdetv2': FewdetTrainerv2,
  'fewdetv3': FewdetTrainerv3,
  'multi_pose': MultiPoseTrainer, 
}
