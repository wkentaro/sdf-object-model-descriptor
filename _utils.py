from mesh_to_sdf import get_surface_point_cloud
import numpy as np
import skimage.measure
import trimesh


def mesh_to_voxels(
    mesh,
    voxel_resolution=64,
    surface_point_method="scan",
    sign_method="normal",
    scan_count=100,
    scan_resolution=400,
    sample_point_count=10000000,
    normal_sample_count=11,
    pad=False,
    check_result=False,
    return_gradients=False,
):
    surface_point_cloud = get_surface_point_cloud(
        mesh,
        surface_point_method,
        3**0.5,
        scan_count,
        scan_resolution,
        sample_point_count,
        sign_method == "normal",
    )

    return surface_point_cloud.get_voxels(
        voxel_resolution,
        sign_method == "depth",
        normal_sample_count,
        pad,
        check_result,
        return_gradients,
    )


def mesh_to_sdf(mesh):
    mesh = mesh.copy()

    offset = -mesh.bounding_box.centroid
    scale = 2 / max(mesh.bounding_box.extents)
    # scale = 2 / mesh.bounding_box.extents  # this squashes some long objects

    mesh.vertices += offset
    mesh.vertices *= scale

    sdf = mesh_to_voxels(
        mesh, voxel_resolution=64, pad=True, sign_method="depth"
    )

    return sdf, scale, offset


def sdf_to_mesh(sdf, scale, offset):
    spacing = (
        2 / (sdf.shape[0] - 2),
        2 / (sdf.shape[1] - 2),
        2 / (sdf.shape[2] - 2),
    )
    vertices, faces, vertex_normals, _ = skimage.measure.marching_cubes(
        sdf,
        level=0,
        spacing=spacing,
    )
    vertices -= 1
    vertices -= 0.5 * np.array(spacing)

    vertices /= scale
    vertices -= offset

    mesh = trimesh.Trimesh(
        vertices=vertices, faces=faces, vertex_normals=vertex_normals
    )
    return mesh
