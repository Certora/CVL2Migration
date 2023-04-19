methods {
    //// CVL 2: in the `methods` block, you can use either the contract name or the
    //// instance name
    function secondaryInstance.balanceOf(address) external returns(uint) envfree;
    function SecondaryContract.transferFrom(address, address, uint) external returns(bool) envfree;
}
