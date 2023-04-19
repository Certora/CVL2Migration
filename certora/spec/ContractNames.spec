//// `PrimaryContract` and `SecondaryContract` are contract names;
//// `primary` and `secondary` are instance names
using PrimaryContract   as primary;
using SecondaryContract as secondary;

methods {
    //// CVL 2: in the `methods` block, the receiver may be either the contract
    ////        name or an instance name (the effect is the same)
    function secondary.balanceOf(address) external returns(uint) envfree;
    function SecondaryContract.transfer(address, uint) external returns(bool);

    //// CVL 2: user-defined types are named using the contract name
    //// TODO: this should require a `memory` annotation
    function getX(PrimaryContract.S) external returns(uint) envfree;
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

