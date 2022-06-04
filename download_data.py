#!/usr/bin/env python

import gdown
import path


here = path.Path(__file__).abspath().parent


gdown.cached_download(
    path=here / "data/YCB_Video_Models.zip",
    url="https://drive.google.com/uc?id=1BoXR3rNqWIoILDQK8yiB6FWgvHGpjtJe",
    md5="054b845708318a9d38a3f080572dcb3c",
)
