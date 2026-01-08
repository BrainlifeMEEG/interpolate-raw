"""
Interpolate bad channels in MNE raw data.

This app identifies channels marked as bad in the raw data and interpolates
their values using MNE's interpolate_bads() function. Interpolation is performed
using spherical spline or other available methods depending on channel types and
digitized head points.

Input:
    - raw: Path to MNE raw .fif file

Output:
    - out_dir/raw.fif: Raw data with interpolated bad channels
    - product.json: Summary of interpolation results
"""

# Copyright (c) 2020 brainlife.io
#
# This app interpolates bad channels in MNE raw data.
#
# Author: Guiomar Niso
# Contributor: Kami Salibayeva
# Indiana University

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_raw_info_to_product
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir')

# Load configuration
config = load_config()

# == LOAD DATA ==
fname = config['raw']
raw = mne.io.read_raw_fif(fname, preload=True)

# == INTERPOLATE BAD CHANNELS ==
bads_before = raw.info['bads'].copy()
raw.interpolate_bads()
bads_after = raw.info['bads'].copy()

# == SAVE DATA ==
raw.save(os.path.join('out_dir', 'raw.fif'), overwrite=True)

# == CREATE PRODUCT JSON ==
product_items = []

# Add raw info
add_raw_info_to_product(product_items, raw)

# Add interpolation summary
if bads_before:
    interp_msg = f"Interpolated {len(bads_before)} bad channel(s): {', '.join(bads_before)}"
    add_info_to_product(product_items, interp_msg)
else:
    add_info_to_product(product_items, "No bad channels to interpolate")

create_product_json(product_items)