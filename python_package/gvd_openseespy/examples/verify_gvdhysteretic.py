import gvd_openseespy.opensees as ops


def main():
    ops.wipe()
    ops.model("basic", "-ndm", 1, "-ndf", 1)

    # Minimal GVDHysteretic material definition.
    # Positive backbone points are provided as displacement-force pairs:
    # pd1 pf1 pd2 pf2 pd3 pf3.
    # If -negBackBone is not provided, the material mirrors the positive backbone.
    ops.uniaxialMaterial(
        "GVDHysteretic",
        1,
        "-posBackBone",
        0.01, 100.0,
        0.02, 120.0,
        0.04, 80.0,
    )

    # Simple one-dimensional zeroLength spring model.
    ops.node(1, 0.0)
    ops.node(2, 0.0)
    ops.fix(1, 1)
    ops.fix(2, 0)
    ops.element("zeroLength", 1, 1, 2, "-mat", 1, "-dir", 1)

    ops.timeSeries("Linear", 1)
    ops.pattern("Plain", 1, 1)
    ops.load(2, 1.0)

    ops.constraints("Plain")
    ops.numberer("Plain")
    ops.system("BandGeneral")
    ops.test("NormDispIncr", 1.0e-8, 10)
    ops.algorithm("Newton")
    ops.integrator("DisplacementControl", 2, 1, 0.001)
    ops.analysis("Static")

    ok = ops.analyze(1)
    if ok != 0:
        raise RuntimeError("Verification analysis failed")

    disp = ops.nodeDisp(2, 1)
    print("GVDHysteretic verification completed successfully.")
    print(f"Node 2 displacement after one step: {disp}")


if __name__ == "__main__":
    main()
