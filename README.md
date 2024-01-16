# FewShot-CenterNet


# Abstract  
En este trabajo se propone una nueva arquitectura, basada en un modelo
que representa la detección de objetos como mapas de calor, CenterNet, capaz de explorar
este problema. Esta propuesta de modelo se entrena con la base de datos COCO, igual que
CenterNet. Además, entrega como resultado un mapa de calor único, que contiene la detección
de los objetos, logrando incluso, detecciones de objetos que no se presentan en la base
de datos en la que se entrenó. Una vez entrenado, se extraen las características del objeto
detectado para luego ser comparado con una pequeña base de datos de objetos particulares.
En una evaluación preliminar, la precisión lograda en términos de clasificación para esta base
de datos reducida de 26 objetos fue del 80.77 %.
En conclusión, en cuanto a la detección de objetos, se logra un F-score del 55.92% para
la configuración de 6 objetos por imagen con un umbral de IoU de 0.75, y un F-score del
82.28% con un umbral de IoU de 0.50. Es relevante señalar que, aunque el modelo muestra
buen rendimiento en detección y clasificación por separado, se identifican desafíos al intentar
integrar eficazmente ambos aspectos. Este hallazgo destaca la complejidad de lograr una
armoniosa combinación de detección y clasificación de objetos en un único modelo.




## Repository forked from: Objects as Points
Object detection, 3D detection, and pose estimation using center point detection:
> [**Objects as Points**](http://arxiv.org/abs/1904.07850),            
> Xingyi Zhou, Dequan Wang, Philipp Kr&auml;henb&uuml;hl,        
> *arXiv technical report ([arXiv 1904.07850](http://arxiv.org/abs/1904.07850))*
> Github(https://github.com/xingyizhou/CenterNet)      
Contact: [zhouxy@cs.utexas.edu](mailto:zhouxy@cs.utexas.edu).
