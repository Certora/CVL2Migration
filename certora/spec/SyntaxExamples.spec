




//// CVL 1: `using`, `pragma`, and `import` do not require terminating semicolons
pragma specify 1.0
import imported.spec
using SecondaryContract as secondaryInstance

methods {
    //// CVL 1: methods block entries don't have `function`, visibility
    //// modifiers, or `;`
    transferFrom(address, uint) envfree

    //// CVL 1: the order of the modifiers is loose
    balanceOf(address) envfree returns(uint)

    //// CVL 1: in the `methods` block, the receiver must be the contract instance
    secondaryInstance.balanceOf(address) returns(uint) envfree;
    secondaryInstance.transferFrom(address, uint) envfree;
}

//// CVL 1: `use` statements don't require semicolons
use invariant importedInvariant

use rule importedInvariant filtered {
    f -> !excludeFromProver(f)
}

rule onlyApproveIncreasesAllowance {
    address sender; address recipient;
    allowance_before = allowance(sender, recipient);

    method f; env e; calldataarg args;
    f(e, args);

    allowance_after = allowance(sender, recipient);

    //// CVL 1: Method literals look like function calls
    assert allowance_after >= allowance_before
        => f.selector == approve(address, uint).selector,
        "only approve can increase allowances";
}




