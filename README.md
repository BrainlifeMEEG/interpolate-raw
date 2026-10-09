# Interpolate Bad Channels in Raw MEG/EEG Data

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.816-blue.svg)](https://doi.org/10.25663/brainlife.app.816)

## Description

Interpolates bad channels in continuous MNE raw MEG/EEG data using `raw.interpolate_bads()` (`mne.io.Raw.interpolate_bads`). Channels already marked as bad in the input raw file — plus any additional channels given via the `bads` configuration parameter — are spatially interpolated using the available method for their channel type (e.g. spherical spline for EEG), enabling their recovery for downstream analysis.

The app generates:
- Raw data with bad channels interpolated
- A power spectral density (PSD) plot of the resulting data
- A `product.json` summary of the interpolation

## Inputs

- **`raw`** (`neuro/meeg/mne/raw`): continuous raw data containing the channel(s) to interpolate (required)

## Outputs

- **`out_dir/raw.fif`** (`neuro/meeg/mne/raw`): raw data with bad channels interpolated
- **`out_figs/psd.png`**: power spectral density plot of the interpolated data
- **`product.json`**: summary of the interpolation, including raw info and the list of channels interpolated

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `bads` | string (optional) | `""` | Comma-separated list of additional channel names to mark as bad before interpolation (e.g. `"MEG0111,MEG0112,EEG001"`). These are combined with any channels already marked bad in the input file. Leave empty to interpolate only the channels already marked bad. |

## Usage

### Running on Brainlife.io

1. Select a continuous MEG/EEG dataset as the `raw` input.
2. Optionally set `bads` to mark extra channels for interpolation.
3. Submit the task.
4. Review the PSD plot and interpolation summary in the output viewer.

### Local Testing

```bash
# Update config.json with your data path
python main.py
```

## Technical Details

- **Method**: MNE's `interpolate_bads()` function uses spherical spline interpolation or an equivalent method, depending on channel type and the availability of digitized head points.
- **Requirements**: Bad channels must be marked in the input raw data (`raw.info['bads']`), either already present in the file or added via the `bads` parameter.
- **Preload**: Data is preloaded before interpolation to allow in-place modification.
- **Output format**: Standard MNE `.fif` format compatible with downstream processing.

## Authors
- [Guiomar Niso](https://github.com/guiomar)
- [Kamilya Salibayeva](https://github.com/KSalibay) (Indiana University)
- [Maximilien Chaumon](https://github.com/dnacombo), Paris Brain Institute

## Citations

We kindly ask that you cite the following articles when publishing papers and code using this app:

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2

Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
