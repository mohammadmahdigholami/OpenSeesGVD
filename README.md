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
