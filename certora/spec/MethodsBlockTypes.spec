//// CVL 2 supports all Solidity types (except function types)
//// TODO: See https://docs.certora.com/.../cvl2/changes.md#all-solidity-types-allowed-as-arguments

methods {
    //// CVL 1: enum arguments to contract functions needed to be encoded as `uint8`
    ////
    //// here `f` actually expects a Permission enum as an argument, not a uint8
    f(uint8 permission) => NONDET

    //// TODO: more examples
}
