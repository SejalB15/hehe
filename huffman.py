# Huffman Encoding using Greedy Strategy (Simple & Working in VS Code)

import heapq  # Used to get the smallest two frequencies easily

# Step 1: Input characters and their frequencies
char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}

# Step 2: Create a priority queue (min-heap)
heap = [[freq, [char, ""]] for char, freq in char_freq.items()]
heapq.heapify(heap)  # Convert list into a min-heap

# Step 3: Build Huffman Tree using greedy approach
while len(heap) > 1:
    # Take out two smallest frequency nodes
    low1 = heapq.heappop(heap)
    low2 = heapq.heappop(heap)

    # Add '0' to left branch, '1' to right branch
    for pair in low1[1:]:
        pair[1] = '0' + pair[1]
    for pair in low2[1:]:
        pair[1] = '1' + pair[1]

    # Merge two nodes and add their frequencies
    new_node = [low1[0] + low2[0]] + low1[1:] + low2[1:]
    heapq.heappush(heap, new_node)

# Step 4: Extract and print Huffman codes
huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

print("\n===============================")
print(" HUFFMAN ENCODING OUTPUT ")
print("===============================\n")
print("Character | Frequency | Huffman Code")
print("------------------------------------")

for char, code in huffman_codes:
    print(f"    {char}      |    {char_freq[char]}       |     {code}")

print("\n✅ Huffman Encoding completed successfully!")