#!/usr/bin/env python3
"""
image_metadata_organizer.py

Scan a directory of images (jpg/jpeg/png), extract EXIF metadata, and optionally
organize images into date-based subfolders. Also generate a CSV report.

Usage:
    python3 image_metadata_organizer.py /path/to/images --report report.csv
    python3 image_metadata_organizer.py /path/to/images --organize --dry-run
"""

import os
import sys
import argparse
import csv
from datetime import datetime
from typing import Optional, Dict
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(img_path: str) -> Dict[str, Optional[str]]:
    """
    Extract EXIF metadata from image. Returns dict of tag → value (some may be None).
    """
    try:
        with Image.open(img_path) as img:
            info = img._getexif()
            if info is None:
                return {}
            data: Dict[str, Optional[str]] = {}
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                # If GPS info, convert nested keys
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub = GPSTAGS.get(t, t)
                        gps_data[sub] = value[t]
                    data["GPSInfo"] = gps_data
                else:
                    data[decoded] = value
            return data
    except Exception as e:
        # Could not open or read metadata
        return {}

def get_date_taken(exif: Dict[str, Optional[str]]) -> Optional[datetime]:
    # Common EXIF tags: "DateTimeOriginal", "DateTime"
    dt = exif.get("DateTimeOriginal") or exif.get("DateTime")
    if dt:
        try:
            # format: "YYYY:MM:DD HH:MM:SS"
            return datetime.strptime(dt, "%Y:%m:%d %H:%M:%S")
        except ValueError:
            pass
    return None

def generate_report(images: list[str], report_path: str) -> None:
    """
    Generate CSV report with columns: filename, date_taken, camera_make, camera_model, gps_lat, gps_lon
    """
    with open(report_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        header = ["filename", "date_taken", "camera_make", "camera_model", "gps_lat", "gps_lon"]
        writer.writerow(header)
        for img in images:
            exif = get_exif_data(img)
            dt = get_date_taken(exif)
            dt_str = dt.isoformat(sep=" ") if dt else ""
            make = str(exif.get("Make", "")) if exif.get("Make") else ""
            model = str(exif.get("Model", "")) if exif.get("Model") else ""
            gps = exif.get("GPSInfo") or {}
            # Simple parse GPS (if exists)
            latitude = gps.get("GPSLatitude")
            latitude_ref = gps.get("GPSLatitudeRef")
            longitude = gps.get("GPSLongitude")
            longitude_ref = gps.get("GPSLongitudeRef")
            # Converting GPS to decimal (very basic)
            def convert(coord, ref):
                if not coord or not ref:
                    return ""
                # coord is tuple of rationals (num, denom)
                try:
                    d = coord[0][0] / coord[0][1]
                    m = coord[1][0] / coord[1][1]
                    s = coord[2][0] / coord[2][1]
                    dec = d + m/60 + s/3600
                    if ref in ["S", "W"]:
                        dec = -dec
                    return f"{dec:.6f}"
                except Exception:
                    return ""
            lat_dec = convert(latitude, latitude_ref)
            lon_dec = convert(longitude, longitude_ref)
            writer.writerow([img, dt_str, make, model, lat_dec, lon_dec])

def organize_by_date(images: list[str], base_dir: str, dry_run: bool = False) -> None:
    """
    Move images into subfolders under base_dir: YYYY/MM/
    """
    for img in images:
        exif = get_exif_data(img)
        dt = get_date_taken(exif)
        if dt:
            subfolder = dt.strftime("%Y/%m")
        else:
            subfolder = "unknown_date"
        target_dir = os.path.join(base_dir, subfolder)
        os.makedirs(target_dir, exist_ok=True)
        dest = os.path.join(target_dir, os.path.basename(img))
        if dry_run:
            print(f"[DRY RUN] Would move: {img} → {dest}")
        else:
            try:
                os.rename(img, dest)
                print(f"Moved: {img} → {dest}")
            except Exception as e:
                print(f"Error moving {img}: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Image metadata extractor & organizer")
    parser.add_argument("directory", help="Directory containing images")
    parser.add_argument("--report", "-r", help="Path to output CSV report")
    parser.add_argument("--organize", "-o", action="store_true", help="Organize images into date folders")
    parser.add_argument("--dry-run", help="If set, just print moves, don’t execute", action="store_true")

    args = parser.parse_args()
    dirpath = args.directory
    if not os.path.isdir(dirpath):
        print("Error: directory not found", file=sys.stderr)
        sys.exit(1)

    # Find images (jpg/jpeg/png)
    exts = {".jpg", ".jpeg", ".png"}
    images = []
    for root, _, files in os.walk(dirpath):
        for fn in files:
            ext = os.path.splitext(fn)[1].lower()
            if ext in exts:
                images.append(os.path.join(root, fn))

    if not images:
        print("No images found in directory.")
        return

    if args.report:
        generate_report(images, args.report)
        print(f"Report written to: {args.report}")

    if args.organize:
        organize_by_date(images, dirpath, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
