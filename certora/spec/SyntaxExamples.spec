//// CVL 1: `using`, `pragma`, and `import` do not require terminating semicolons
pragma specify 1.0
import "imported.spec"
using SecondaryContract as secondaryInstance

methods {
    //// CVL 1: methods block entries don't have `function`, visibility
    //// modifiers, or `;`
    transferFrom(address, address, uint) returns(bool) envfree

    //// CVL 1: the order of the modifiers is loose
    //// TODO: can't actually reorder them?
    allowance(address,address) returns(uint) envfree

    //// CVL 1: in the `methods` block, the receiver must be the contract instance
    secondaryInstance.balanceOf(address) returns(uint) envfree
    secondaryInstance.transfer(address, uint) returns(bool) envfree
}

//// CVL 1: `use` statements don't require semicolons
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

    //// CVL 1: Method literals look like function calls
    assert allowance_after >= allowance_before
        => f.selector == approve(address, uint).selector,
        "only approve can increase allowances";
}




