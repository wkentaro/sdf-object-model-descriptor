#!/usr/bin/env python

import argparse

import numpy as np
import path
import skimage.measure
import trimesh


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("sdf_file", type=path.Path)
args = parser.parse_args()

sdf = np.load(args.sdf_file)
vertices, faces, vertex_normals, _ = skimage.measure.marching_cubes(
    sdf, level=0
)
mesh = trimesh.Trimesh(
    vertices=vertices, faces=faces, vertex_normals=vertex_normals
)
mesh.show(resolution=(640, 480))
