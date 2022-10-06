#!/usr/bin/env python3

# Description: updates the image URL in all .json metadata files of a collection

# How to use: replace INSERT_URL_HERE with the link to where your IPFS images live.

import json
import os

path_of_dir = "./metadata/"

for filename in os.listdir(path_of_dir):
  butcher_filename = filename.split(".")
  token_id = butcher_filename[0]
  f = os.path.join(path_of_dir, filename)
  if os.path.isfile(f):
    rf = open(f, "r")
    data = json.loads(rf.read())
    # replace INSERT_URL_HERE with IPFS URL
    replacement_filename = "INSERT_URL_HERE" + token_id + ".png"
    data["image"] = replacement_filename
    wf = open(f, "w")
    wf.write(json.dumps(data))
    wf.close()
