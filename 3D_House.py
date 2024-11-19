import cairo

# Canvas size
WIDTH, HEIGHT = 800, 600

# Create surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background
context.set_source_rgb(1, 1, 1)  # White background
context.rectangle(0, 0, WIDTH, HEIGHT)
context.fill()

# Helper function to draw polygons
def draw_polygon(ctx, points, color):
    ctx.set_source_rgb(*color)
    ctx.move_to(*points[0])
    for point in points[1:]:
        ctx.line_to(*point)
    ctx.close_path()
    ctx.fill()

# Colors
ground_color = (0.6, 0.9, 0.4)  # Green ground
wall_color = (0.9, 0.9, 0.9)  # Light beige walls
roof_color = (0.2, 0.2, 0.3)  # Dark gray roof
window_color = (0.5, 0.7, 0.9)  # Light blue windows
door_color = (0.2, 0.3, 0.5)  # Dark blue door
step_color = (0.8, 0.8, 0.8)  # Gray steps
chimney_color = (0.7, 0.7, 0.7)  # Light gray chimney

# Ground (green base)
draw_polygon(context, [(200, 500), (600, 400), (700, 500), (300, 600)], ground_color)

# Main structure - front wall
draw_polygon(context, [(300, 300), (500, 250), (500, 450), (300, 500)], wall_color)

# Main structure - side wall
draw_polygon(context, [(500, 250), (650, 200), (650, 400), (500, 450)], (0.8, 0.8, 0.8))

# Roof - front
draw_polygon(context, [(300, 300), (500, 250), (550, 150), (350, 200)], roof_color)

# Roof - side
draw_polygon(context, [(500, 250), (650, 200), (550, 150)], roof_color)

# Windows (front wall)
context.set_source_rgb(*window_color)
context.rectangle(350, 350, 40, 60)  # Left window
context.fill()
context.rectangle(410, 350, 40, 60)  # Right window
context.fill()

# Door (front wall)
context.set_source_rgb(*door_color)
context.rectangle(380, 420, 40, 80)  # Door
context.fill()

# Steps
draw_polygon(context, [(370, 500), (430, 480), (450, 490), (390, 510)], step_color)

# Chimney
draw_polygon(context, [(530, 150), (560, 140), (570, 190), (540, 200)], chimney_color)

# Save the final image
output_path = "\PycharmProjects\Basic_Drawing"
surface.write_to_png(output_path)

output_path = "3d_house_exact.png"
