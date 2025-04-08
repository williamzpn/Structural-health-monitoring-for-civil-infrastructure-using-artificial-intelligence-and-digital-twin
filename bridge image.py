import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Node positions for the 3D healthy truss model
node_positions_3d = {
    29: (0, 0, 0), 27: (1, 0, 0), 26: (2, 0, 0), 25: (3, 0, 0), 24: (4, 0, 0), 23:(5,0,0), 22: (6, 0, 0), 21: (7, 0, 0), 2:(8, 0, 0),
    32: (0, 1, 0), 19: (1, 1, 0), 18: (2, 1, 0), 17: (3, 1, 0), 16: (4, 1, 0), 15: (5, 1, 0), 14: (6, 1, 0),13:(7, 1, 0),3:(8, 1, 0),
    28: (1, 0, 1), 31: (2, 0, 1), 30: (3, 0, 1), 20: (4, 0, 1), 12: (5, 0, 1), 11: (6, 0, 1), 10: (7, 0, 1),
    9: (1, 1, 1), 8: (2, 1, 1), 7: (3, 1, 1), 6: (4, 1, 1), 5: (5, 1, 1), 4: (6, 1, 1), 1: (7, 1, 1),33: (4, 0, 0.75),34: (4, 0, 0.25),
}

# Edges for the 3D truss model
edges_3d = [
    (29, 27), (27, 26), (26, 25), (25, 24), (24, 23), (23, 22), (22, 21), (21, 2),
    (32, 19), (19, 18), (18, 17), (17, 16), (16, 15), (15, 14), (14, 13), (13, 3),
    (28, 31), (31, 30), (30, 20), (20, 12), (12, 11), (11, 10),
    (9, 8), (8, 7), (7, 6), (6, 5), (5, 4), (4, 1),
    (29, 32), (27, 19), (26, 18), (25, 17), (24, 16), (23, 15), (22, 14), (21, 13),(2, 3),
    (9, 28), (8, 31), (7, 30), (6, 20), (5, 12), (4, 11),(1, 10),
    (29, 28), (28, 26), (26, 30), (30, 24), (24, 12), (12, 22), (22, 10), (10, 2),
    (28, 27), (31, 26), (25, 30), (23, 12), (11, 22), (10, 21),
    (9, 19), (8, 18), (7, 17), (6, 16), (5, 15), (4, 14),(1, 13),
    (9, 32), (9, 18), (7, 18), (7, 16), (5, 16), (5, 14), (1, 14),(1, 3),
    (28, 8), (8, 30), (6, 30), (6, 12), (4, 12), (4, 10),
    (29, 19), (19, 26), (26, 17), (17, 24), (24, 15), (15, 22), (22, 13), (13, 2),(20, 33),(24, 34),
]

# Extract 3D node positions
x_coords = [pos[0] for pos in node_positions_3d.values()]
y_coords = [pos[1] for pos in node_positions_3d.values()]
z_coords = [pos[2] for pos in node_positions_3d.values()]

# Plot the 3D truss model
fig = plt.figure(figsize=(18, 16))  # Adjust figure size for scaling
ax = fig.add_subplot(111, projection='3d')

# Remove the background and grid lines
ax.set_axis_off()  # Turns off the entire axis background

# Plot nodes
ax.scatter(x_coords, y_coords, z_coords, c='green', s=25, label='Nodes')
"""
# Annotate nodes with labels
for node, (x, y, z) in node_positions_3d.items():
    ax.text(x, y, z, str(node), color='red', fontsize=10)
"""
# Plot edges
for edge in edges_3d:
    x = [node_positions_3d[edge[0]][0], node_positions_3d[edge[1]][0]]
    y = [node_positions_3d[edge[0]][1], node_positions_3d[edge[1]][1]]
    z = [node_positions_3d[edge[0]][2], node_positions_3d[edge[1]][2]]
    ax.plot(x, y, z, c='blue', linewidth=3)  # Default color
ax.plot([4,4], [0,0], [0.25,0.75], c='red', linewidth=8)  # Default color
# Adjust scaling and limits for better visualization
ax.set_box_aspect([1, 1, 0.6])  # Adjust aspect ratio
ax.set_xlim([-0.5, 6.5])
ax.set_ylim([-0.5, 2.5])
ax.set_zlim([-0.5, 2.5])

plt.show()
