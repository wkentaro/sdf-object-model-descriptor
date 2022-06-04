#!/usr/bin/env python

import numpy as np
import path
import rich
import trimesh

import _utils


here = path.Path(__file__).abspath().parent


def main():
    root_dir = here / "data/YCB_Video_Models"
    for model_dir in sorted(root_dir.listdir()):
        npz_file = model_dir / "sdf_64.npz"
        if npz_file.exists():
            continue

        mesh_file = model_dir / "textured_simple.obj"
        mesh = trimesh.load_mesh(mesh_file)

        rich.print(f"Converting: {mesh_file}")
        sdf, scale, offset = _utils.mesh_to_sdf(mesh)
        rich.print(f"Finished converting: {mesh_file}")

        np.savez(npz_file, sdf=sdf, offset=offset, scale=scale)
        rich.print(f"Saved to: {npz_file}")


if __name__ == "__main__":
    main()
