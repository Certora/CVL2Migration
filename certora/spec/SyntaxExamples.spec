methods {
    //// CVL 1: in the `methods` block, the receiver must be the contract instance
    secondaryInstance.balanceOf(address) returns(uint) envfree
    secondaryInstance.transfer(address, uint) returns(bool) envfree
}



