import pandas as pd
import matplotlib.pyplot as plt

graphs = {
    '8cell' : 's_SRR5836473_1_bismark_bt2_pe.deduplicated.bedGraph',
    'icm': 's_SRR5836475_1_bismark_bt2_pe.deduplicated.bedGraph',
    'epiblast': 's_SRR3824222_1_bismark_bt2_pe.deduplicated.bedGraph'
    }

for stage in graphs:
  df = pd.read_csv(graphs[stage], delimiter='\t', skiprows=1, header=None)

  plt.figure(figsize=[10, 6])
  plt.title(stage, fontsize=16)
  plt.hist(df[3], bins=100, density=True, color='purple')
  plt.show()
