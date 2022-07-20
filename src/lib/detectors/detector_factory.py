from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .exdet import ExdetDetector
from .ddd import DddDetector
from .ctdet import CtdetDetector
from .ctdetv2 import CtdetDetector as CtdetDetectorv2
from .multi_pose import MultiPoseDetector
from .fewdetv2 import FewdetDetector
from .fewdetv3 import FewdetDetector as FewdetDetectorv3

detector_factory = {
  'exdet': ExdetDetector, 
  'ddd': DddDetector,
  'ctdet': CtdetDetector,
  'ctdetv2': CtdetDetectorv2,
  'multi_pose': MultiPoseDetector,
  'fewdetv2': FewdetDetector,
  'fewdetv3': FewdetDetectorv3,
}
