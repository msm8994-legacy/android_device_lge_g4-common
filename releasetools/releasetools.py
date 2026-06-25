import os
import zipfile
from common import ZipWriteStr

def FullOTA_InstallEnd(info):
    """
    Called at the end of the full OTA package generation.
    """

    # Path to build.prop inside the build output
    build_prop_path = os.path.join(
        info.input_tmp,
        "SYSTEM",
        "build.prop"
    )

    if os.path.exists(build_prop_path):
        with open(build_prop_path, "r") as f:
            build_prop_data = f.read()

        # Add to the final zip
        ZipWriteStr(info.output_zip, "build.prop", build_prop_data)
        print("Added build.prop to OTA package")
    else:
        print("build.prop not found")
