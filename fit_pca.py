#!/usr/bin/env python

import pickle

import numpy as np
import path
import rich
import sklearn.decomposition


here = path.Path(__file__).abspath().parent


def main():
    root_dir = here / "data/YCB_Video_Models"
    data = []
    for model_dir in sorted(root_dir.listdir()):
        npz_file = model_dir / "sdf_64.npz"
        if not npz_file.exists():
            continue

        npz_data = np.load(npz_file)
        data.append(npz_data["sdf"])
    data = np.stack(data)
    X = data.reshape(data.shape[0], -1)

    pca = sklearn.decomposition.PCA(n_components=20)
    pca.fit(X)

    pkl_file = here / "data/pca.pkl"
    with open(pkl_file, "wb") as f:
        pickle.dump(pca, f)
    rich.print(f"Saved to: {pkl_file}")


if __name__ == "__main__":
    main()
