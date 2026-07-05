# Native PowerPoint Vector Object Library

All icons must be built from editable PowerPoint shapes.

## Object DSL

Use `objects` in the JSON spec to request domain objects. Each object supports normalized `x`, `y`, `w`, `h`, optional `label`, and type-specific parameters.

## Supported objects

### dataset
Stacked rounded rectangles and short lines. Use for tables, databases, image sets, field data, or simulation data.

### neural_network
Editable circles and connector lines. Parameters: `layers`, `emphasis`.

### material_microstructure
Hexagons, circles, grains, and boundary lines. Use for alloys, composites, crystals, porous materials, and microstructure schematics.

### magnetic_domain
A rounded container with aligned vector arrows and alternating domains. Use for magnetic materials and domain evolution.

### rare_earth_magnet
A magnet block with domain arrows and simplified RE-Fe-B composition markers. Use for rare-earth permanent magnet graphical abstracts.

### crack_defect
Jagged editable polyline with optional suppressed branch marks. Use for crack detection, defect propagation, and fracture examples.

### sensor_array
Repeating sensor nodes and signal arcs. Use for monitoring, smart construction, IoT, or experiments.

### monitoring_site
A simplified civil monitoring scene combining structures and sensors. Use for smart construction and field measurement abstracts.

### civil_structure
Editable beams, columns, slabs, and ground baseline. Use for civil engineering, structural monitoring, tunnels, excavation, and infrastructure examples.

### fem_mesh
Editable triangular/quadrilateral mesh. Use for finite element modeling and computational mechanics.

### finite_element_result
Mesh plus editable deformed/result curve. Use for simulation-result schematics without embedding screenshots.

### vision_pipeline
Camera rectangle, image tile, segmentation mask, and vector arrow. Use for computer vision workflows.

### molecule_grid
Repeating circles and bonds. Use for chemistry, biology, and materials atomistic concepts.

### mechanism_loop
Circular arrows approximated with arcs. Use for feedback, closed-loop optimization, or iterative calibration.

### optimization_loop
Closed-loop optimization nodes for design-simulation-update workflows.

### multiscale_bridge
Micro-meso-macro connected objects. Use for multiscale mechanics, materials, geoscience, and manufacturing.

### process_stack
Layered editable process steps. Use for synthesis, manufacturing, staged simulation, or workflow stacks.

### performance_chart
Native vector bars/line markers, not an inserted chart bitmap. Use only for verified results.

## Redraw policy

When the user provides a raster figure, redraw the concept as vector shapes. Do not embed the original image. If the source is too complex, create a simplified schematic and state what was simplified.

## Quality rule

A domain object is acceptable only when it improves scientific communication. Prefer fewer, clearer, evidence-supported vector objects over decorative icon density.
