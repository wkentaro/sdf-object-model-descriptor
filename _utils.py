import skimage.measure
import trimesh


def mesh_to_sdf(mesh):
    sdf = mesh_to_sdf.mesh_to_voxels(mesh, 64, pad=True)
    return sdf


def sdf_to_mesh(sdf):
    vertices, faces, vertex_normals, _ = skimage.measure.marching_cubes(
        sdf, level=0
    )
    mesh = trimesh.Trimesh(
        vertices=vertices, faces=faces, vertex_normals=vertex_normals
    )
    return mesh
