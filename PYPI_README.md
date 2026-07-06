# GVD-OpenSeesPy

GVD-OpenSeesPy is a modified OpenSeesPy distribution that includes the GVDHysteretic uniaxial material developed for modeling the cyclic behaviour of dowel-type timber connections.

## Installation

Install with:

    pip install gvd-openseespy

## Usage

Use the package as:

    import gvd_openseespy.opensees as ops

    ops.wipe()
    ops.model("basic", "-ndm", 1, "-ndf", 1)

    # Define the GVDHysteretic material using the required parameters
    ops.uniaxialMaterial("GVDHysteretic", 1, ...)

## Current support

This first release currently supports:

- Windows 64-bit
- Python 3.13

The package includes a precompiled OpenSeesPy binary so users do not need to compile OpenSees from source.

## Citation

If you use this material, please cite:

Gholami, M., Viau, C., and Doudak, G. (2026). Proposed new hysteresis model for dowel-type connections of timber lateral load resisting systems. Engineering Structures. https://doi.org/10.1016/j.engstruct.2026.123034

## License and attribution

This package is a modified OpenSees/OpenSeesPy distribution. Users should follow the original OpenSees/OpenSeesPy license terms in addition to citing the associated research paper.

## Disclaimer and license notice

This package provides an unofficial modified OpenSeesPy build containing the `GVDHysteretic` uniaxial material model developed for research purposes.

This package is not an official OpenSees/OpenSeesPy release and is not endorsed by UC Berkeley, PEER, or the OpenSees developers.

This package is intended primarily for research and educational use. Commercial redistribution or incorporation into commercial products may require permission from the appropriate copyright holder(s).

OpenSees/OpenSeesPy copyright and license notices are retained in accordance with the original license.
