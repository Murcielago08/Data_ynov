from __future__ import annotations
from rich.pretty import pprint
from typing import Iterator

class InvoiceNumberIterator :
    def __init__(self, prefix: str = "INV" , start: int = 1) -> None :
        self.prefix = prefix
        self.valeur = start

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.valeur > 100:
            raise StopIteration
        else:
            invoice_number = f"{self.prefix}-{self.valeur:03}"
            self.valeur += 1
            return invoice_number
        
        
# Test
if __name__ == "__main__":
    test = InvoiceNumberIterator("FAC", 2)

    print(next(test))
    print(next(test))
    
    print("---------------------\n")
    
    custom = InvoiceNumberIterator(prefix="INV", start=42)
    
    print(next(custom))
    print(next(custom))
    print(next(custom))
    print(next(custom))