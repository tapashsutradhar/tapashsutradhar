from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

# Create a basic wiring diagram for the solar-battery system
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')
ax.set_title('Solar-Battery System Wiring Diagram', fontsize=14)

# Add components as boxes
components = {
    'Solar Panel': (1, 5),
    'MPPT Charge Controller': (3, 5),
    'Battery (12V LiFePO4)': (5, 6),
    'DC Load': (5, 4),
    'Arduino Uno': (7, 5),
    'Sensors (INA219)': (6, 5),
}

for label, (x, y) in components.items():
    ax.add_patch(mpatches.Rectangle((x-0.4, y-0.2), 0.8, 0.4, fill=True, color='lightblue', edgecolor='black'))
    ax.text(x, y, label, ha='center', va='center', fontsize=9)

# Add arrows to show connections
connections = [
    ('Solar Panel', 'MPPT Charge Controller'),
    ('MPPT Charge Controller', 'Battery (12V LiFePO4)'),
    ('MPPT Charge Controller', 'DC Load'),
    ('Battery (12V LiFePO4)', 'DC Load'),
    ('Battery (12V LiFePO4)', 'Sensors (INA219)'),
    ('Sensors (INA219)', 'Arduino Uno'),
]

for start, end in connections:
    x1, y1 = components[start]
    x2, y2 = components[end]
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))

plt.tight_layout()
plt.show()
