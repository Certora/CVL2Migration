methods {
    //// CVL 2: methods block entries must start with `function`, end with
    //// `;`, and declare visibility (internal or external)
    function transferFrom(address, address, uint) external returns(bool) envfree;
    function balanceOf(address) external returns(uint256) => ALWAYS(3);
}
