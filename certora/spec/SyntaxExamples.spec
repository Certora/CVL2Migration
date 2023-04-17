methods {
    //// CVL 1: in the `methods` block, the receiver must be the contract instance
    secondaryInstance.balanceOf(address) returns(uint) envfree
    secondaryInstance.transfer(address, uint) returns(bool) envfree
}

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




