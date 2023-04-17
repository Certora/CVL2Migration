//// CVL 2: `import` statements must have terminating semicolons
import "imported.spec";

//// CVL 1: `using` statements must have terminating semicolons
using SecondaryContract as secondaryInstance;

//// CVL 1: `use` statements must have terminating semicolons, unless followed
//// by a block (in which case they must not have terminating semicolons)
use invariant exampleImportedInvariant;
use rule exampleImportedRule filtered {
    f -> !f.isView
}

//// CVL 1: `invariant`s must have terminating semicolons, unless followed by a
//// `filtered` or `preserved` block
invariant balanceOfZeroIsZero()
    balanceOf(0) == 0;

invariant totalSupplyBoundsBalance(address a)
    balanceOf(a) <= totalSupply()
    { preserved { require false; } }

