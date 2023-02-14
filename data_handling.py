import os
import json
import joblib
import numpy as np
import pandas as pd
import torch


def save_model(model, hyperparams, metrics, folder, name="model"):
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    model_path = os.path.join(folder, f"{name}.joblib")
    hyperparams_path = os.path.join(folder, f"{name}_hyperparams.json")
    metrics_path = os.path.join(folder, f"{name}_metrics.json")
    joblib.dump(model, model_path)
    with open(hyperparams_path, 'w') as fp:
        json.dump(hyperparams, fp)
    with open(metrics_path, 'w') as fp:
        json.dump(metrics, fp)


def load_airbnb(clean_df: pd.DataFrame, label):

    df = clean_df.copy()
    labels = np.array(df.pop(label))
    try:
        df[label]
        return None
    except:
        features = np.array(df.select_dtypes(['number']))
    return (features, labels)


def standardise(dataset, mean=None, std=None):
    if mean is None and std is None:
        mean, std = np.mean(dataset, axis=0), np.std(dataset, axis=0)  # get mean and standard deviation of dataset
    standardised_dataset = (dataset - mean) / std
    return standardised_dataset, (mean, std)

def standardise_multiple(*datasets, mean=None, std=None):
    for dataset in datasets:
        dataset, (_, _) = standardise(dataset, mean, std)
        yield dataset



if __name__ == "__main__":
    pass