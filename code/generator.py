import cv2
import json
import argparse
import treepoem
import numpy as np
from matplotlib import pyplot as plt


def load_json(fname, *args, **kwargs):
    with open(fname) as f:
        return json.load(f, *args, **kwargs)


def save_json(jd, fname, *args, indent=4, **kwargs):
    with open(fname, 'w') as f:
        json.dump(jd, f, *args, indent=indent, **kwargs)


def aligned_affine(bar, M, fix_position=True):
    xps = [0, 0, 1, 1]
    yps = [1, 0, 0, 1]
    
    height, width, _ = bar.shape
    corners = np.array([[x*width, y*height, 1] for x, y in zip(xps, yps)]).T
    
    if fix_position:
        M[:,-1] = -np.min(M@corners, axis=-1)
    new_sz = np.ceil(np.max(M@corners, axis=-1)).astype(np.int32)
    img = cv2.warpAffine(bar, M, new_sz)
    return img, M@corners


def export(img, coords, name, barcodetype):
    plt.imsave(f'{name}.jpg', img)
    ptsx, ptsy = coords
    res = {f'{name}.jpg813086': {'filename': f'../code/{name}.jpg',
    'size': 813086,
    'regions': [{
        'shape_attributes': {
            'name': 'polygon',
            'all_points_x': list(ptsx),
            'all_points_y': list(ptsy)
        },
        'region_attributes': {'barcode': barcodetype}},
    ],
    'file_attributes': {}}}
    save_json(res, f'{name}.json')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Distorted barcode generator', description='''TODO''')
    parser.add_argument('-b', '--barcode_type', help='barcode type', type=str)
    parser.add_argument('-c', '--content_barcode', help='barcode content', type=str)
    parser.add_argument('-f', '--filename', help='name of the json markup and result img', type=str)
    parser.add_argument('-d', '--dimension', help='1d or 2d barcode', type=str)
    parser.print_help()
    args = parser.parse_args()

    barimg = treepoem.generate_barcode(args.barcode_type, args.content_barcode)
    img, coords = aligned_affine(np.array(barimg), np.random.randn(2, 3))
    export(img, coords, args.filename, args.dimension)
