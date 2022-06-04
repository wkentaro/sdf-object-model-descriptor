#!/usr/bin/env python

import numpy as np
import path
import pickle
import trimesh
import trimesh.viewer

import _utils


here = path.Path(__file__).abspath().parent

pkl_file = here / "data/pca.pkl"
with open(pkl_file, "rb") as f:
    pca = pickle.load(f)

npz1_file = here / "data/YCB_Video_Models/003_cracker_box/sdf_64.npz"
npz2_file = here / "data/YCB_Video_Models/006_mustard_bottle/sdf_64.npz"

npz1 = np.load(npz1_file)
npz2 = np.load(npz2_file)

sdf1_desc = pca.transform(npz1["sdf"].reshape(-1)[None])
sdf2_desc = pca.transform(npz2["sdf"].reshape(-1)[None])

scene = trimesh.Scene()

for i, sdf_desc in enumerate(np.linspace(sdf1_desc, sdf2_desc, num=10)):
    sdf = pca.inverse_transform(sdf_desc)
    mesh = _utils.sdf_to_mesh(
        sdf.reshape(66, 66, 66), scale=(1, 1, 1), offset=(0, 0, 0)
    )
    mesh.apply_translation([2 * i, 0, 0])
    scene.add_geometry(mesh)

scene.show(resolution=(1280, 960))
