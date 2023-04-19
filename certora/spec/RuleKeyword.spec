
//// CVL 2: rules must start with `rule`
rule transferReverts {
    env balanceEnv;
    env e; address recip; uint amount;

    require balanceOf(balanceEnv, e.msg.sender) < amount;

    transfer@withrevert(e, recip, amount);

    assert lastReverted,
        "transfer(recip,amount) must revert if sender's balance is less than `amount`";
}

