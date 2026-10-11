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
    pointer=0
    while L!=[None]*len(pages):
        L[pointer][1]-=1
        if L[pointer][1]==0:
            final.append(L[pointer][0])
            L[pointer]=None
            pointer=(pointer+1)%len(pages)
        else:
            pointer=(pointer+1)%len(pages)
    return final
       
       
pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
