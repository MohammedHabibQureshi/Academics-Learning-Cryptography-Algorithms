
import hashlib

# Simple hash function
def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

# 8 leaf nodes
leaves = ["Tx1", "Tx2", "Tx3", "Tx4", "Tx5", "Tx6", "Tx7", "Tx8"]

# Hash the leaves
level = [h(x) for x in leaves]
print("Leaf Hashes:")
for i, l in enumerate(level):
    print(f"Tx{i+1}: {l}")

# Build the tree
while len(level) > 1:
    new_level = []
    for i in range(0, len(level), 2):
        new_level.append(h(level[i] + level[i+1]))
    level = new_level

# Merkle root
print("\nMerkle Root:", level[0])




"""
//Expt 6: Compute the merkle tree nodes from 8 given leaf nodes

#include <stdio.h>

int main() {
    char char1 = 'A'; // ASCII value of 'A' is 65 (01000001 in binary)
    char char2 = 'B'; // ASCII value of 'B' is 66 (01000010 in binary)
    char char3 = 'C';
    char char4 = 'D';
    char char5 = 'E';
    char char6 = 'F';
    char char7 = 'G';
    char char8 = 'H';
    
    char h1 = char1 ^ char2;
    char h2 = char3 ^ char4;
    char h3 = char5 ^ char6;
    char h4 = char7 ^ char8;
    
    char h5 = h1 ^ h2;
    char h6 = h3 ^ h4;
    
    char h7 = h5 ^ h6;
    

    // Print the root node
    printf("Root node is: %d \n", h7);
    
    // print the 2 children nodes of root
    printf("Two children of Root node are: %d %d\n", h5, h6);
    
    // print the children of children of root
    printf(" Children of children of Root node are: %d %d %d %d\n", h1, h2, h3, h4);
    
    // print the leaf nodes
    printf(" Leaf node are: %d %d %d %d %d %d %d %d\n", char1, char2, char3, char4, char5, char6, char7, char8);

    return 0;
}
"""
