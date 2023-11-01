# https://deeplearningcourses.com/c/cutting-edge-artificial-intelligence
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

logits = np.log([0.1, 0.2, 0.3, 0.4, 0.5])
ic(logits)
samples = []

for _ in range(100):
  noise = np.random.random(len(logits))
  ic(noise)
  sample = np.argmax(logits - np.log(-np.log(noise)))
  ic(sample)
  samples.append(sample)

plt.hist(samples)
plt.show()