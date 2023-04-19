//// `PrimaryContract` and `SecondaryContract` are contract names;
//// `primary` and `secondary` are instance names
using PrimaryContract   as primary
using SecondaryContract as secondary

methods {
    //// CVL 2: in the `methods` block, the receiver must be an instance name
    secondary.balanceOf(address) returns(uint) envfree
    secondary.transfer(address, uint) returns(bool) envfree

    //// CVL 2: user-defined types are named using the contract name
    getX(PrimaryContract.S) returns(uint) envfree
}

rule structExample {
    //// CVL 2: user-defined types are named using the contract name
    PrimaryContract.S s;
    require s.x == 0;
    assert getX(s) == 0;
}

rule multicontractExample {
    //// CVL 2: multicontract methods are still called using an instance name
    mathint y = secondary.balanceOf(0);
    assert true;
}

