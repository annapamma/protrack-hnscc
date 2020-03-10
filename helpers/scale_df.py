import pandas as pd
from sklearn import preprocessing
import pickle


def scale(df):
    # f = '/Users/anna/PycharmProjects/protrack-hnsc/data/Data_freeze_0.1/Proteomics_DIA_Gene_level_Tumor.cct'
    # df = pd.read_csv(f, sep='\t')
    x = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    return pd.DataFrame(x_scaled, columns=df.columns, index=df.index)

def load_pickle(f):
    return pickle.load(open(f'/Users/anna/PycharmProjects/protrack-hnsc/data/actual/{f}.pkl', 'rb'))

clinical = load_pickle('clinical_slim')
mutation = load_pickle('mutation')
rna_tumor = load_pickle('rna_tumor')
proteo = load_pickle('proteo_tumor_scaled')
scna = load_pickle('scna')
