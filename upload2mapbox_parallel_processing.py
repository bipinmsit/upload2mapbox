import multiprocessing as mp
from mapbox import Uploader
import argparse
import os

"""
Script to upload mapbox supported data as tilesets

Author: Bipin Kumar
Company: Laminaar Aviation Infotech India Pvt. Ltd.
Date: 17 Nov 2021
"""


def get_args():
    parser = argparse.ArgumentParser(
        description="Upload mapbox supported data to mapbox"
    )
    parser.add_argument("--dir", type=str, help="Directory to upload to mapbox")

    return parser.parse_args()


def upload_to_mapbox(file_to_upload):
    output_file_name = os.path.basename(file_to_upload).split(".")[0]
    valid_tileset_id = output_file_name.replace(" ", "_")

    service = Uploader()
    with open(file_to_upload, "rb") as src:
        upload_resp = service.upload(
            src,
            tileset=valid_tileset_id
            if len(valid_tileset_id) == 32
            else valid_tileset_id[0:32],
        )

    return upload_resp


def main(data_dir):
    pool = mp.Pool(mp.cpu_count())
    pool.map(
        upload_to_mapbox,
        [
            os.path.join(os.path.abspath(data_dir), file)
            for file in os.listdir(data_dir)
        ],
    )


if __name__ == "__main__":
    args = get_args()
    main(args.dir)
