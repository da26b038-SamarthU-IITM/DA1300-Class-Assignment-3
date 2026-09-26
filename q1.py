from typing import List


def printer_queue_order(pages: List[int]) -> List[int]:
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """
    final=[]
    L=[None for i in range (len(pages))]
    for i in range(len(pages)):
        L[i]=[i,pages[i]]
    while True:
        if len(L)==0:
            return final
        L[0][1]-=1
        if L[0][1]==0:
            final.append(L[0][0])
            L.pop(0)
        else:
            L=L[1:]+L[0:1]
       
pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
