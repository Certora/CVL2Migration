rule onlyApproveIncreasesAllowance {
    address sender; address recipient;
    uint allowance_before = allowance(sender, recipient);

    method f; env e; calldataarg args;
    f(e, args);

    uint allowance_after = allowance(sender, recipient);

    //// CVL 1: Method literals look like function calls
    assert allowance_after >= allowance_before
        => f.selector == approve(address, uint).selector,
        "only approve can increase allowances";
}

