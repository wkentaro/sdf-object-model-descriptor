#!/usr/bin/env python

import argparse

import numpy as np
import path
import trimesh

import _utils


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("npz_file", type=path.Path)
    args = parser.parse_args()

    scene = trimesh.Scene()

    mesh = trimesh.load_mesh(args.npz_file.parent / "textured_simple.obj")
    scene.add_geometry(mesh)

    data = np.load(args.npz_file)
    mesh = _utils.sdf_to_mesh(
        sdf=data["sdf"], scale=data["scale"], offset=data["offset"]
    )
    scene.add_geometry(mesh)

    scene.show(resolution=(1280, 960))


if __name__ == "__main__":
    main()
