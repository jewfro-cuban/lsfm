from .landmark import landmark_mesh
from .visualize import visualize_nicp_result
from .correspond import correspond_mesh
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def landmark_and_correspond_mesh(mesh, img_shape=(320, 240), template_fn=None, verbose=False):
    # Don't touch the original mesh
    mesh = mesh.copy()
    lms = landmark_mesh(mesh, img_shape=img_shape, template_fn=template_fn, verbose=verbose)

    mesh.landmarks['__lsfm_masked'] = lms['landmarks_3d_masked']

    return_dict = {
        'shape_nicp': correspond_mesh(mesh, mask=lms['occlusion_mask'], template_fn=template_fn,
                                      verbose=verbose),
        'landmarked_image': lms['landmarked_image']
    }
    return_dict['shape_nicp_visualization'] = visualize_nicp_result(
        return_dict['shape_nicp'], template_fn=template_fn)

    return return_dict
