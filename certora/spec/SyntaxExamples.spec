methods {
    //// CVL 2: in the `methods` block, you can use either the contract name or the
    //// instance name
    function secondaryInstance.balanceOf(address) external returns(uint) envfree;
    function SecondaryContract.transferFrom(address, address, uint) external returns(bool) envfree;
}

use rule exampleImportedRule filtered {
    f -> !f.isView
}

rule onlyApproveIncreasesAllowance {
    address sender; address recipient;
    uint allowance_before = allowance(sender, recipient);

    method f; env e; calldataarg args;
    f(e, args);

    uint allowance_after = allowance(sender, recipient);

    //// CVL 2: Method literals must be prefixed with `sig:`
    assert allowance_after >= allowance_before
        => f.selector == sig:approve(address, uint).selector,
        "only approve can increase allowances";
}




