from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd

class MeasureThresholds:
    def __init__(self, name="test", id_2013="C00", rates_file=None):
        self.name = name
        self.id_2013 = id_2013
        pass

    def set_rates(self, rates=None):
        if rates is None:
            self.rates = pd.DataFrame({'rate':[0.5, 0.55, 0.57, 0.6, 0.6, 0.62, 0.65, 0.66, 0.7, 0.77, 0.8, 0.61]})
        else:
            self.rates = pd.DataFrame({'rate': rates})
        
        self.rates.sort_values(by='rate', inplace=True)

    def create_thresholds(self):
        self.cl = AgglomerativeClustering(n_clusters=5, linkage="ward")
        self.cl.fit_predict(self.rates)
        self.

        pass


if __name__ == "__main__":

    cl = AgglomerativeClustering(n_clusters=5, linkage="ward")
    rates = pd.DataFrame({'rate':[0.5, 0.55, 0.57, 0.6, 0.6, 0.62, 0.65, 0.66, 0.7, 0.77, 0.8, 0.61]})
    rates = rates.sort_values(by='rate', inplace=True)
    cl.fit_predict(rates)
 
    df = pd.DataFrame(data=rates, columns=['rate'], index=cl.labels_)
    dfmin = df.groupby(level=0).min()
    dfmin.sort_values(by="rate", inplace=True)
    df_fin = pd.DataFrame({'rate': dfmin['rate'], 'star': [1, 2, 3, 4, 5]})
    df_fin.set_index('star')
    print(df_fin)