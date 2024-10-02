# frm

[![PyPI](https://img.shields.io/pypi/v/frm?label=PyPI%20Package)](https://pypi.org/project/frm/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/84233a0d4c944e7e92abdb4011db33b4)](https://app.codacy.com/gh/frmcalcs/frm/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

frm is an in-development python package for quantitative financial pricing and modelling.
frm uses common 3rd party python packages for scientific computing (numpy, scipy, pandas, numba, matplotlib) and the holidays package.

This package will have a similar function set to Quantlib however we want to make it more *accessible*, *documented*, and *productive* through:
1. The python (core + 3rd party libaries) implementation
2. In line academic and industry references to support users own validation and testing
3. Supporting [excel/VBA models](https://github.com/shasafoster/frm/tree/master/excel_models) that validate/support the code 
4. Significant code examples  

## Installation
```bash
pip install --upgrade frm
```

## Complete with examples
- Clewlow-Strickland 1-factor simulation
- Heston parameter calibration to European FX option volatility smile
- Heston simulation

## In progress
- Interest rate swaps pricing
- Interest rate curve bootstrapping

## Pipeline
- SABR volatility model calibration to European swaptions
- Swaption and cap floor pricing using calibrated SABR model
- CDS Bootstrapper


