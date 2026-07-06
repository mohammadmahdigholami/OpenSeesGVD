# GVDHysteretic: OpenSees Uniaxial Material for Dowel-Type Timber Connections

This repository provides the OpenSees C++ implementation of **GVDHysteretic**, a uniaxial hysteretic material model developed for simulating the monotonic and cyclic response of dowel-type timber connections used in timber lateral load-resisting systems.

The model was developed as part of the doctoral research of **Mohammadmahdi Gholami** and is associated with the following journal paper:

> Gholami, M., Viau, C., and Doudak, G. (2026).  
> **Proposed new hysteresis model for dowel-type connections of timber lateral load resisting systems.**  
> *Engineering Structures*.  
> DOI: https://doi.org/10.1016/j.engstruct.2026.123034

ScienceDirect link: https://www.sciencedirect.com/science/article/pii/S014102962600948X

---

## 1. Purpose of the Model

Dowel-type timber connections often exhibit highly nonlinear hysteretic behavior, including:

- initial slack or gap effects associated with oversized holes;
- asymmetric cyclic response;
- pinching during unloading and reloading;
- stiffness degradation;
- strength degradation;
- cyclic deterioration governed by accumulated energy dissipation;
- smooth transition between stiffness branches;
- different response characteristics in positive and negative loading directions.

Conventional hysteretic material models may not accurately represent all of these features simultaneously, especially when the objective is to model connection-level response and then use the calibrated connection model in nonlinear dynamic analysis of timber structural systems.

**GVDHysteretic** was developed to provide a physically motivated and computationally efficient material model for dowel-type timber connections within the OpenSees framework.

---

## 2. Main Capabilities

The implemented material model can simulate:

- monotonic and cyclic behavior of dowel-type timber connections;
- connection response with initial gap/slack;
- pinched hysteretic loops;
- peak-oriented and pinching-oriented cyclic response modes;
- positive and negative backbone branches;
- stiffness deterioration;
- strength deterioration;
- reloading and unloading stiffness rules;
- energy-based cyclic degradation;
- smooth transition between branches to reduce abrupt numerical jumps.

The material is intended for connection-level modeling and for system-level nonlinear analysis of timber lateral load-resisting systems, such as timber braced frames.

---

## 3. Citation

If you use this material model, please cite:

```bibtex
@article{Gholami2026GVDHysteretic,
  title   = {Proposed new hysteresis model for dowel-type connections of timber lateral load resisting systems},
  author  = {Gholami, Mohammadmahdi and Viau, Christian and Doudak, Ghasan},
  journal = {Engineering Structures},
  year    = {2026},
  doi     = {10.1016/j.engstruct.2026.123034}
}
```

---

## 4. Authors

**Mohammadmahdi Gholami**  
Ph.D. student, Structural Engineering  
Carleton University / University of Ottawa research collaboration

**Christian Viau, Ph.D., P.Eng.**  
Assistant Professor  
Department of Civil and Environmental Engineering  
Carleton University

**Ghasan Doudak, Ph.D., P.Eng.**  
Professor  
Department of Civil Engineering  
University of Ottawa

---


## PyPI installation

The GVDHysteretic material is also available through PyPI as a precompiled Windows Python package. This allows users to install and use the material without compiling OpenSees from source.

### Installation

```bash
pip install gvd-openseespy
```

Current package support:

- Windows 64-bit
- Python 3.13

### Python usage

```python
import gvd_openseespy.opensees as ops

ops.wipe()
ops.model("basic", "-ndm", 1, "-ndf", 1)

ops.uniaxialMaterial(
    "GVDHysteretic",
    1,
    "-posBackBone",
    0.01, 100.0,
    0.02, 120.0,
    0.04, 80.0,
)
```

### Verification

After installation, users can verify that the package works by running:

```bash
python -m gvd_openseespy.examples.verify_gvdhysteretic
```

Expected output:

```text
GVDHysteretic verification completed successfully.
Node 2 displacement after one step: 0.001
```

### Citation

If you use this material, please cite:

Gholami, M., Viau, C., and Doudak, G. (2026). Proposed new hysteresis model for dowel-type connections of timber lateral load resisting systems. Engineering Structures. https://doi.org/10.1016/j.engstruct.2026.123034

## Disclaimer and license notice

This package provides an unofficial modified OpenSeesPy build containing the `GVDHysteretic` uniaxial material model developed for research purposes.

This package is not an official OpenSees/OpenSeesPy release and is not endorsed by UC Berkeley, PEER, or the OpenSees developers.

This package is intended for research and educational use. Commercial redistribution or incorporation into commercial products may require permission from the appropriate copyright holder(s).

OpenSees/OpenSeesPy copyright and license notices are retained in accordance with the original license.
