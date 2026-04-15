"""
Interpolate bad channels in MNE raw data.

This app identifies channels marked as bad in the raw data and interpolates
their values using MNE's interpolate_bads() function. Interpolation is performed
using spherical spline or other available methods depending on channel types and
digitized head points. Additional bad channels can be specified via configuration.

Input:
    - config.json:
      - raw: Path to MNE raw .fif file
      - bads: Optional comma-separated list of channel names to mark as bad

Output:
    - out_dir/raw.fif: Raw data with interpolated bad channels
    - product.json: Summary of interpolation results
"""

# Copyright (c) 2026 brainlife.io
#
# This app interpolates bad channels in MNE raw data.
#
# Authors:
# - Guiomar Niso (https://github.com/guiomar)
# - Kamilya Salibayeva (https://github.com/KSalibay)
# - Maximilien Chaumon (https://github.com/dnacombo)

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

# == MARK ADDITIONAL BAD CHANNELS ==
# Parse bads from config if provided
bads_config = config.get('bads', '')
if bads_config and bads_config != 'None':
    bads = [ch.strip() for ch in bads_config.split(',')]
    # Filter to only channels that exist in the raw file
    bads = [ch for ch in bads if ch in raw.ch_names]
    if bads:
        raw.info['bads'].extend(bads)
        raw.info['bads'] = list(set(raw.info['bads']))  # Remove duplicates

# == INTERPOLATE BAD CHANNELS ==
bads_before = raw.info['bads'].copy()
raw.interpolate_bads()
bads_after = raw.info['bads'].copy()

# == SAVE DATA ==
raw.save(os.path.join('out_dir', 'raw.fif'), overwrite=True)

# == CREATE PSD PLOT ==
fig = raw.compute_psd().plot(exclude='bads', show=False)
fig.savefig(os.path.join('out_figs', 'psd.png'), dpi=100, bbox_inches='tight')
plt.close(fig)

# == CREATE PRODUCT JSON ==
product_items = []

# Add raw info
add_raw_info_to_product(product_items, raw)

# Add interpolation summary
if bads_before:
    interp_msg = f"Interpolated {len(bads_before)} bad channel(s): {', '.join(bads_before)}"
    add_info_to_product(product_items, interp_msg, msg_type='success')
else:
    add_info_to_product(product_items, "No bad channels to interpolate", msg_type='success')
    
# Add PSD plot if it exists
psd_image_path = os.path.join('out_figs', 'psd.png')
if os.path.exists(psd_image_path):
    add_image_to_product(product_items, name='Power Spectral Density (PSD)', filepath=psd_image_path)

create_product_json(product_items)