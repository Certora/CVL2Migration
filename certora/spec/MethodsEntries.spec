methods {
    //// CVL 1: methods block entries must not have `function` or visibility
    //// modifiers.  Terminating semicolons are optional.
    transferFrom(address, address, uint) returns(bool) envfree
    balanceOf(address) returns(uint256) => ALWAYS(3)
}
