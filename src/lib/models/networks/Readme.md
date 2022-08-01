Description of modification made on each network:


- pose_dla_dcnv2.py: Separated SS, HM with Cosclassifier using nn.Linear and softmax, sigmoid after multiplying SS*HM.

- pose_dla_dcnv3.py: Separated SS, HM with Cosclassifier using nn.Linear and softmax, sigmoid after multiplying SS*HM, I added relu to cosdist layer

- pose_dla_dcnv4.py: Try to multiply SS and HM, with Cosclassifier using parameter W and softmax, using CTDET as used in CenterNet. Batchnom, relu applied to ss layer

- pose_dla_dcnv5.py: Same as before, but adding more layers to SS branch.

- pose_dla_dcnv6.py: Try to multiply SS and HM, applying sigmoid to HM before multiplying SS (removing sigmoid in ctdetv2).

- pose_dla_dcnv7.py:  Separated SS, HM with Cosclassifier using parameter W and softmax, without  multiplying SS*HM. Using focal loss to HM, and CELoss to SS (just for positives examples). Adding some changes and fixes to CosClassifier, modifing the way i permuted the W Matrix, before and after multiplying output.

- Last versión:  Using pose_dla_dcnv6.py, but adding a hm loss.