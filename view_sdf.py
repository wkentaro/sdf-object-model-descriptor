#!/usr/bin/env python

import argparse

import numpy as np
import path

import _utils


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("sdf_file", type=path.Path)
    args = parser.parse_args()

    sdf = np.load(args.sdf_file)
    mesh = _utils.sdf_to_mesh(sdf)
    mesh.show(resolution=(640, 480))


if __name__ == "__main__":
    main()
