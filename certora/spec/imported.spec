invariant exampleImportedInvariant() true

rule exampleImportedRule(method f) {
    env e; calldataarg args;
    f(e, args);
    assert true;
}
