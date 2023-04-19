//// `PrimaryContract` and `SecondaryContract` are contract names;
//// `primary` and `secondary` are instance names
using PrimaryContract   as primary
using SecondaryContract as secondary

methods {
    //// CVL 1: in the `methods` block, the receiver must be an instance name
    secondary.balanceOf(address) returns(uint) envfree
    secondary.transfer(address, uint) returns(bool)

    //// CVL 1: user-defined types are named using an instance name
    getX(primary.S) returns(uint) envfree
}

rule structExample {
    //// CVL 1: user-defined types are named using an instance name
    primary.S s;
    require s.x == 0;
    assert getX(s) == 0;
}

rule multicontractExample {
    //// CVL 1: multicontract methods are called using an instance name
    mathint y = secondary.balanceOf(0);
    assert true;
}

