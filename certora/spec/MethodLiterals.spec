rule onlyApproveIncreasesAllowance {
    address sender; address recipient;

    env e_before;
    uint allowance_before = allowance(e_before, sender, recipient);

    method f; env e; calldataarg args;
    f(e, args);

    env e_after;
    uint allowance_after = allowance(e_after, sender, recipient);

    //// CVL 1: Method literals look like function calls
    assert allowance_after >= allowance_before
        => f.selector == approve(address, uint).selector,
        "only approve can increase allowances";
}

