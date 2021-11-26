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


def upload_to_mapbox(dir):

    for file in os.listdir(dir):
        output_file_name = file.split(".")[0]
        valid_tileset_name = output_file_name.replace(" ", "_")
        valid_tileset_id = valid_tileset_name[0:14]

        print("{} is uploading".format(valid_tileset_name))

        service = Uploader()
        with open(os.path.join(os.path.abspath(dir), file), "rb") as src:
            upload_resp = service.upload(
                src,
                name=valid_tileset_name
                if len(valid_tileset_name) == 32
                else valid_tileset_name[0:32],
                tileset=valid_tileset_id,
            )

    return upload_resp


def main(data_dir):
    upload_to_mapbox(data_dir)


if __name__ == "__main__":
    args = get_args()
    main(args.dir)
