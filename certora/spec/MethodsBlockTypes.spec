//// CVL 2 supports all Solidity types (except function types)
////
//// TODO: See https://docs.certora.com/.../cvl2/changes.md#all-solidity-types-allowed-as-arguments

methods {
    //// CVL 2: supports enums in the methods block
    ////
    //// here `f` expects a Permission enum as an argument
    f(Example.Permission permission) => NONDET
}
