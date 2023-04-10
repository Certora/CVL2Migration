//// CVL 2: `using`, `pragma`, and `import` require terminating semicolons
pragma specify 2.0;
import "imported.spec";
using SecondaryContract as secondaryInstance;

methods {
    //// CVL 2: methods block entries must start with `function`, end with
    //// `;`, and declare visibility (internal or external)
    function transferFrom(address, address, uint) external returns(bool) envfree;

    //// CVL 2: the order of the modifiers is strict
    //// TODO: can't actually reorder them?
    function allowance(address,address) external returns(uint) envfree;

    //// CVL 2: in the `methods` block, you can use either the contract name or the
    //// instance name
    function secondaryInstance.balanceOf(address) external returns(uint) envfree;
    function SecondaryContract.transferFrom(address, address, uint) external returns(bool) envfree;
}

//// CVL 2: `use` statements require semicolons, unless they end with a block
use invariant exampleImportedInvariant

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




