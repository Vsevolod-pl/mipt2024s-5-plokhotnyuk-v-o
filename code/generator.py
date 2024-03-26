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
        M = M.copy()
        M[:,-1] *= 0
        M[:,-1] = -np.min(M@corners, axis=-1)

    new_sz = np.ceil(np.max(M@corners, axis=-1)).astype(np.int32)
    img = cv2.warpAffine(bar, M, new_sz)
    return img, M@corners


def coords_to_regions(coords, dimensions):
    res = []
    for i in range(len(coords)):
        ptsx, ptsy = coords[i]
        
        res.append({\
        'shape_attributes': {
            'name': 'polygon',
            'all_points_x': list(ptsx),
            'all_points_y': list(ptsy)
        },
        'region_attributes': {'barcode': dimensions[i]}})
    return res


def export(img, name, coords, dimensions):
    plt.imsave(f'{name}.jpg', np.clip(img, 0, 1))
    res = {f'{name}.jpg813086': {'filename': f'../code/{name}.jpg',
    'size': 813086,
    'regions': coords_to_regions(coords, dimensions),
    'file_attributes': {}}}
    save_json(res, f'{name}.json')


def generate_distorted(barcode_types, content_barcodes, distortions=None):
    if distortions is None:
        distortions = np.random.randn(len(barcode_types), 2, 3)
    barimgs = [treepoem.generate_barcode(typ, content) for typ, content in zip(barcode_types, content_barcodes)]
    imgs, coords = zip(*[aligned_affine(np.array(img), dis) for img, dis in zip(barimgs, distortions)])
    masks, _ = zip(*[aligned_affine(np.ones_like(img), dis) for img, dis in zip(barimgs, distortions)])
    width, height = np.max(coords, axis=(0, 2))*2
    combined = np.zeros((int(width), int(height), 3))
    for i in range(len(imgs)):
        w, h, _ = imgs[i].shape
        dw = np.random.randint(0, width - w)
        dh = np.random.randint(0, height - h)
        coords[i][0] += dh
        coords[i][1] += dw
        expanded_img = np.zeros_like(combined)
        expanded_img[dw:w+dw, dh:h+dh] = imgs[i]
        expanded_mask = np.zeros_like(combined)
        expanded_mask[dw:w+dw, dh:h+dh] = masks[i]
        combined = combined*(1-expanded_mask) + expanded_img
    return combined, coords


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Distorted barcode generator', description='''TODO''')
    parser.add_argument('-c', '--config', help='json config to generate image with barcodes', type=str)
    # parser.add_argument('-b', '--barcode_type', help='barcode type', type=str)
    # parser.add_argument('-c', '--content_barcode', help='barcode content', type=str)
    # parser.add_argument('-f', '--filename', help='name of the json markup and result img', type=str)
    # parser.add_argument('-d', '--dimension', help='1d or 2d barcode', type=str)
    parser.print_help()
    args = parser.parse_args()

    conf = load_json(args.config)
    img, coords = generate_distorted(conf['barcode_types'], conf['barcode_contents'])
    export(img, conf['name'], coords, conf['barcode_dimensions'])

    # barimg = treepoem.generate_barcode(args.barcode_type, args.content_barcode)
    # img, coords = aligned_affine(np.array(barimg), np.random.randn(2, 3))
    # export(img, coords, args.filename, args.dimension)
