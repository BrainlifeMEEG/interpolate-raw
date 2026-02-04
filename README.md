# app-interpolate-raw

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.469-blue.svg)](https://doi.org/10.25663/brainlife.app.469)

## Description

Interpolates bad channels in MNE raw data using `mne.io.raw.interpolate_bads()`. Channels marked as bad in the input raw file are spatially interpolated using available methods (spherical spline, etc.), enabling their recovery for downstream analysis. Additional bad channels can be specified via the `bads` configuration parameter.

## Inputs

- **raw**: Path to MNE raw `.fif` file

## Outputs

- **out_dir/raw.fif**: Raw data with bad channels interpolated
- **product.json**: Summary of interpolation results including raw info and interpolation summary

## Configuration Parameters

- **raw** (string): Path to input MNE raw `.fif` file
- **bads** (string, optional): Comma-separated list of channel names to mark as bad before interpolation (e.g., "MEG0111,MEG0112,EEG001"). Channels already marked as bad in the input file plus any specified here will be interpolated. Leave empty to use only channels marked bad in the input file.

## Usage

The app:
1. Loads the raw MNE data file
2. Marks additional channels as bad if specified in config
3. Identifies all channels marked as bad (either in input file or via config)
4. Performs spatial interpolation on bad channels
5. Saves the resulting raw data with interpolated channels
6. Generates a product.json with detailed information

## Technical Details

- **Method**: MNE's `interpolate_bads()` function uses spherical spline interpolation or equivalent methods
- **Requirements**: Bad channels must be marked in the input raw data (raw.info['bads'])
- **Preload**: Data is preloaded before interpolation to ensure proper handling
- **Output format**: Standard MNE `.fif` format compatible with downstream processing

## Authors
- [Guiomar Niso](https://github.com/guiomar)
- [Kamilya Salibayeva](https://github.com/KSalibay) (Indiana University)
- [Maximilien Chaumon](https://github.com/dnacombo), Paris Brain Institute

## Citations

We kindly ask that you cite the following articles when publishing papers and code using this app:

**brainlife.io: A decentralized and open source cloud platform to support neuroscience research**. Hayashi, S., Caron, B. A., et al. & Pestilli, F. (2023). ArXiv. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10274934/

**MEG and EEG data analysis with MNE-Python**. Gramfort A, et al. & Hämäläinen MS. (2013). Frontiers in Neuroscience, 7(267):1–13. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

#### MIT Copyright (c) 2026 brainlife.io The University of Texas at Austin and Indiana University
