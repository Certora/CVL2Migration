//// CVL 1: `import` statements must not have terminating semicolons
import "imported.spec"

//// CVL 1: `using` statements must not have terminating semicolons
using SecondaryContract as secondaryInstance

//// CVL 1: `use` statements must not have terminating semicolons
use invariant exampleImportedInvariant
use rule exampleImportedRule filtered {
    f -> !f.isView
}

//// CVL 1: `invariant`s must not have terminating semicolons
invariant balanceOfZeroIsZero()
    balanceOf(0) == 0

invariant totalSupplyBoundsBalance(address a)
    balanceOf(a) <= totalSupply()
    { preserved { require false; } }

