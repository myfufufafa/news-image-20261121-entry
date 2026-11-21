"""news-image-20261121: copy the shipped front page to /output/entry.png.

The image itself is the entry: a dense broadsheet front page summing up
Saturday 21 November 2026 in 36 stories (lead: Russian missiles landing in
Poland and the mass barrage that hit three Kyiv bridges) plus a labelled
world-map panel. Version 2 of the image restores story #19 (GOLD TUMBLES)
as its own numbered headline, fixes the subhead typos of version 1, and
completes story #24; all 36 numbered headlines render. This program does
no drawing and no network access; it copies the shipped PNG byte for byte,
so two runs always produce identical output.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1048576


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from a PNG IHDR chunk (no image library needed)."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError("missing PNG IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def source_path() -> Path:
    here = Path(__file__).resolve().parent
    candidate = here / SOURCE_NAME
    if candidate.is_file():
        return candidate
    fallback = Path.cwd() / SOURCE_NAME
    if fallback.is_file():
        return fallback
    raise FileNotFoundError(f"shipped image not found: {candidate}")


def output_dir() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def main() -> int:
    src = source_path()
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / OUTPUT_NAME
    shutil.copyfile(src, out)
    data = out.read_bytes()
    if data != src.read_bytes():
        raise ValueError("output differs from shipped image")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("output is not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError(f"output too large: {len(data)} bytes")
    width, height = png_dimensions(data)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(f"unexpected dimensions: {width}x{height}")
    print(f"wrote {out} ({len(data)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
