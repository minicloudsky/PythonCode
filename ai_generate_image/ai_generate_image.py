import io
import os, sys
import requests
import PIL

import torch
import torchvision.transforms as T
import torchvision.transforms.functional as TF

from dall_e import map_pixels, unmap_pixels, load_model
from IPython.display import display, display_markdown
import torch.nn.functional as F

target_image_size = 256


def download_image(url):
    proxies = {"http": "http://127.0.0.1:4780"}
    resp = requests.get(url, proxies=proxies)
    resp.raise_for_status()
    return PIL.Image.open(io.BytesIO(resp.content))


def preprocess(img):
    s = min(img.size)

    if s < target_image_size:
        raise ValueError(f'min dim for image {s} < {target_image_size}')

    r = target_image_size / s
    s = (round(r * img.size[1]), round(r * img.size[0]))
    img = TF.resize(img, s, interpolation=PIL.Image.LANCZOS)
    img = TF.center_crop(img, output_size=2 * [target_image_size])
    img = torch.unsqueeze(T.ToTensor()(img), 0)
    return map_pixels(img)


if __name__ == '__main__':
    # This can be changed to a GPU, e.g. 'cuda:0'.
    dev = torch.device('cpu')

    # For faster load times, download these files locally and use the local paths instead.
    enc = load_model("./encoder.pkl", dev)
    dec = load_model("./decoder.pkl", dev)

    print("loaded model")
    f = PIL.Image.open('./img.png')
    x = preprocess(f)
    print("process image")
    display_markdown('Original image:')
    display(T.ToPILImage(mode='RGBA')(x[0]))

    z_logits = enc(x)
    z = torch.argmax(z_logits, axis=1)
    z = F.one_hot(z, num_classes=enc.vocab_size).permute(0, 3, 1, 2).float()

    x_stats = dec(z).float()
    x_rec = unmap_pixels(torch.sigmoid(x_stats[:, :3]))
    x_rec = T.ToPILImage(mode='RGBA')(x_rec[0])
    display_markdown('Reconstructed image:')
    display(x_rec)
