#!/usr/bin/env python

import mesh_to_sdf
import numpy as np
import path
import rich
import trimesh


here = path.Path(__file__).abspath().parent


root_dir = here / "data/YCB_Video_Models"
for model_dir in sorted(root_dir.listdir()):
    sdf_file = model_dir / "sdf_64.npy"
    if sdf_file.exists():
        continue

    mesh_file = model_dir / "textured_simple.obj"
    mesh = trimesh.load_mesh(mesh_file)
    rich.print(f"Converting: {mesh_file}")
    voxels = mesh_to_sdf.mesh_to_voxels(mesh, 64, pad=True)
    rich.print(f"Finished converting: {mesh_file}")
    np.save(sdf_file, voxels)
