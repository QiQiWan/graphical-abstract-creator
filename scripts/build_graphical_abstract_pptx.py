#!/usr/bin/env python3
"""Build an editable vector PowerPoint graphical abstract from a JSON spec."""
import json, sys, math
from pathlib import Path
from typing import Dict, Any, List

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE

SLIDE_W = 13.333
SLIDE_H = 7.5

PALETTES = {
    "nature_blue": {"background":"#FFFFFF","text":"#1F2933","muted":"#52616B","primary":"#1F6B99","secondary":"#3BA7C9","accent":"#F28E2B","neutral":"#F4F8FB","line":"#2B3A42","white":"#FFFFFF"},
    "science_graphite": {"background":"#FFFFFF","text":"#111827","muted":"#6B7280","primary":"#374151","secondary":"#9CA3AF","accent":"#D97706","neutral":"#F3F4F6","line":"#1F2937","white":"#FFFFFF"},
    "advanced_materials_teal": {"background":"#FFFFFF","text":"#172A3A","muted":"#5C677D","primary":"#087E8B","secondary":"#56A3A6","accent":"#F25F5C","neutral":"#F6FAFA","line":"#1B4965","white":"#FFFFFF"},
    "cell_biomedical": {"background":"#FFFFFF","text":"#253237","muted":"#64748B","primary":"#7B2CBF","secondary":"#2EC4B6","accent":"#FF9F1C","neutral":"#F8F5FF","line":"#3D405B","white":"#FFFFFF"},
    "engineering_amber": {"background":"#FFFFFF","text":"#1F2937","muted":"#6B7280","primary":"#0F4C5C","secondary":"#E36414","accent":"#5F0F40","neutral":"#FAF7F2","line":"#334155","white":"#FFFFFF"},
    "ai4science_indigo": {"background":"#FFFFFF","text":"#202A44","muted":"#6C7280","primary":"#3B5BDB","secondary":"#20C997","accent":"#F76707","neutral":"#F5F7FF","line":"#243B53","white":"#FFFFFF"},
    "earth_environment": {"background":"#FFFFFF","text":"#233D4D","muted":"#607D8B","primary":"#2D6A4F","secondary":"#40916C","accent":"#DDA15E","neutral":"#F4F8F5","line":"#264653","white":"#FFFFFF"},
    "minimal_mono": {"background":"#FFFFFF","text":"#111111","muted":"#666666","primary":"#222222","secondary":"#888888","accent":"#B45309","neutral":"#F5F5F5","line":"#222222","white":"#FFFFFF"},
    "chinese_science_blue": {"background":"#FFFFFF","text":"#1A2A3A","muted":"#5A6B7A","primary":"#1D5F8A","secondary":"#3A8FB7","accent":"#B23A48","neutral":"#F4F8FB","line":"#243B53","white":"#FFFFFF"},
    "chinese_academy_red": {"background":"#FFFFFF","text":"#241A1A","muted":"#675C5C","primary":"#9E2A2B","secondary":"#335C67","accent":"#C9A227","neutral":"#FBF7F4","line":"#3A2E2E","white":"#FFFFFF"},
    "sci_cjk_bilingual": {"background":"#FFFFFF","text":"#172033","muted":"#627083","primary":"#255F85","secondary":"#2A9D8F","accent":"#D45D44","neutral":"#F5F8FA","line":"#2D3748","white":"#FFFFFF"},
}
PALETTE_ORDER = ["background", "neutral", "primary", "secondary", "accent", "line", "text"]
TYPE_TO_COLOR = {"data":"primary","dataset":"primary","sample":"secondary","instrument":"primary","process":"primary","model":"accent","mechanism":"secondary","validation":"accent","outcome":"secondary","application":"secondary"}


def rgb(hex_color: str) -> RGBColor:
    h = str(hex_color).strip().lstrip('#')
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def box(x,y,w,h):
    return Inches(x*SLIDE_W), Inches(y*SLIDE_H), Inches(w*SLIDE_W), Inches(h*SLIDE_H)

def point(x,y):
    return Inches(x*SLIDE_W), Inches(y*SLIDE_H)

def font_for(spec):
    if spec.get('font'):
        return spec['font']
    lang = str(spec.get('language','en'))
    profile = str(spec.get('journal_profile',''))
    if lang.startswith('zh') or lang == 'bilingual' or profile == 'chinese_top_journal':
        return 'Microsoft YaHei'
    return 'Arial'

def set_fill_line(shape, fill, line, width=1.0):
    shape.fill.solid(); shape.fill.fore_color.rgb = rgb(fill)
    shape.line.color.rgb = rgb(line); shape.line.width = Pt(width)

def textbox(slide, txt, x,y,w,h, size=11, bold=False, color='#1F2933', align=PP_ALIGN.LEFT, font='Arial'):
    sh = slide.shapes.add_textbox(*box(x,y,w,h))
    tf = sh.text_frame; tf.clear(); tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = str(txt or '')
    run.font.name = font; run.font.size = Pt(size); run.font.bold = bold; run.font.color.rgb = rgb(color)
    return sh

def rect(slide,x,y,w,h,fill,line,width=0.8,rounded=False):
    shp = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    sh = slide.shapes.add_shape(shp,*box(x,y,w,h))
    set_fill_line(sh,fill,line,width)
    return sh

def oval(slide,x,y,w,h,fill,line,width=0.8):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL,*box(x,y,w,h)); set_fill_line(sh,fill,line,width); return sh

def add_line(slide, x1,y1,x2,y2, color, width=1.1):
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, *point(x1,y1), *point(x2,y2))
    ln.line.color.rgb = rgb(color); ln.line.width = Pt(width)
    return ln

def add_arrow(slide, x1,y1,x2,y2, color, width=1.1):
    add_line(slide,x1,y1,x2,y2,color,width)
    size = 0.018
    tri = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, *box(x2-size, y2-size, size*2, size*2))
    set_fill_line(tri, color, color, 0.1)
    tri.rotation = math.degrees(math.atan2(y2-y1, x2-x1)) + 90
    return tri

def add_elbow_arrow(slide, x1,y1,x2,y2, color, width=1.1):
    midx=(x1+x2)/2
    add_line(slide,x1,y1,midx,y1,color,width)
    add_line(slide,midx,y1,midx,y2,color,width)
    return add_arrow(slide,midx,y2,x2,y2,color,width)

def layout_blocks(blocks: List[Dict[str,Any]], pattern: str) -> List[Dict[str,Any]]:
    n = max(1, len(blocks))
    has_coords = all(all(k in b for k in ('x','y','w','h')) for b in blocks)
    if has_coords:
        return blocks
    out = [dict(b) for b in blocks]
    if pattern in ('left_to_right_pipeline','problem_method_outcome','data_model_decision'):
        w = min(0.20, 0.78/n)
        gap = (0.84 - n*w)/(n-1) if n > 1 else 0
        x0 = 0.08
        for i,b in enumerate(out):
            b.update({'x': x0+i*(w+gap), 'y':0.34, 'w':w, 'h':0.34})
    elif pattern == 'center_core_radial':
        cx, cy = 0.50, 0.52
        for i,b in enumerate(out):
            if i == 0:
                b.update({'x':0.38,'y':0.31,'w':0.24,'h':0.30})
            else:
                ang = 2*math.pi*(i-1)/max(1,n-1) - math.pi/2
                b.update({'x':cx+0.34*math.cos(ang)-0.10,'y':cy+0.30*math.sin(ang)-0.10,'w':0.20,'h':0.20})
    elif pattern == 'before_after_comparison':
        for i,b in enumerate(out):
            if i == 0: b.update({'x':0.08,'y':0.30,'w':0.28,'h':0.38})
            elif i == 1: b.update({'x':0.36,'y':0.32,'w':0.24,'h':0.34})
            elif i == 2: b.update({'x':0.64,'y':0.30,'w':0.28,'h':0.38})
            else: b.update({'x':0.10+0.20*(i-3),'y':0.74,'w':0.18,'h':0.14})
    elif pattern == 'multiscale_stack':
        h = min(0.16, 0.60/n)
        gap = 0.025
        for i,b in enumerate(out):
            b.update({'x':0.18,'y':0.25+i*(h+gap),'w':0.64,'h':h})
    elif pattern == 'comparison':
        for i,b in enumerate(out):
            col = i % 2; row = i // 2
            b.update({'x':0.08 + col*0.46,'y':0.26+row*0.22,'w':0.38,'h':0.18})
    else:
        return layout_blocks(out, 'left_to_right_pipeline')
    return out

def object_box(parent, obj):
    if parent:
        px, py, pw, ph = parent['x'], parent['y'], parent['w'], parent['h']
        x = px + float(obj.get('x',0.35))*pw
        y = py + float(obj.get('y',0.18))*ph
        w = float(obj.get('w',0.24))*pw
        h = float(obj.get('h',0.24))*ph
        return x,y,w,h
    return float(obj.get('x',0.4)),float(obj.get('y',0.4)),float(obj.get('w',0.1)),float(obj.get('h',0.1))

# Vector object library

def draw_dataset(slide,x,y,w,h,pal):
    for i in range(3):
        sh = rect(slide,x+i*w*0.12,y+i*h*0.10,w*0.78,h*0.46,pal['white'],pal['primary'],0.7,True)
        for j in range(3):
            add_line(slide, x+w*0.14+i*w*0.12, y+h*0.12+i*h*0.10+j*h*0.10, x+w*0.60+i*w*0.12, y+h*0.12+i*h*0.10+j*h*0.10, pal['primary'], 0.45)

def draw_neural(slide,x,y,w,h,pal,layers=None):
    layers = layers or [3,4,3]
    if len(layers) < 2: layers=[3,3]
    xs = [x + w*(0.12 + i*(0.76/(len(layers)-1))) for i in range(len(layers))]
    coords = []
    for li,count in enumerate(layers):
        ys = [y + h*(0.18 + j*(0.64/(max(1,count-1)))) for j in range(count)]
        layer=[]
        for yy in ys:
            oval(slide,xs[li]-w*0.035,yy-h*0.035,w*0.07,h*0.07,pal['white'],pal['accent'],0.7)
            layer.append((xs[li], yy))
        coords.append(layer)
    for a in range(len(coords)-1):
        for p1 in coords[a]:
            for p2 in coords[a+1]:
                add_line(slide,p1[0],p1[1],p2[0],p2[1],'#C7D0D9',0.22)

def draw_micro(slide,x,y,w,h,pal):
    for i in range(10):
        cx = x + w*(0.15 + (i%5)*0.17)
        cy = y + h*(0.25 + (i//5)*0.30)
        sh = slide.shapes.add_shape(MSO_SHAPE.HEXAGON, *box(cx-w*0.055, cy-h*0.08, w*0.11, h*0.16))
        set_fill_line(sh, pal['neutral'], pal['secondary'], 0.55)
    for i in range(8):
        oval(slide,x+w*(0.10+i*0.10), y+h*(0.70-0.05*(i%2)), w*0.045, h*0.045, pal['secondary'], pal['secondary'], 0.2)

def draw_magnetic(slide,x,y,w,h,pal):
    rect(slide,x,y,w,h,pal['white'],pal['secondary'],0.5,True)
    for i in range(5):
        yy = y + h*(0.20+i*0.14)
        add_arrow(slide, x+w*0.18, yy, x+w*0.78, yy + h*(0.04 if i%2 else -0.02), pal['secondary'], 0.9)

def draw_rare_earth_magnet(slide,x,y,w,h,pal):
    rect(slide,x+w*0.10,y+h*0.20,w*0.80,h*0.52,pal['neutral'],pal['primary'],0.8,True)
    for i in range(5):
        xx=x+w*(0.18+i*0.14)
        add_arrow(slide,xx,y+h*0.62,xx+w*0.08,y+h*0.32,pal['accent'] if i%2 else pal['secondary'],0.9)
    for i,lab in enumerate(['RE','Fe','B']):
        oval(slide,x+w*(0.20+i*0.20),y+h*0.75,w*0.10,h*0.12,pal['white'],pal['primary'],0.6)
        textbox(slide,lab,x+w*(0.20+i*0.20),y+h*0.775,w*0.10,h*0.045,6.5,True,pal['text'],PP_ALIGN.CENTER)

def draw_crack(slide,x,y,w,h,pal):
    pts = [(x+w*0.15,y+h*0.20),(x+w*0.32,y+h*0.34),(x+w*0.27,y+h*0.48),(x+w*0.52,y+h*0.56),(x+w*0.48,y+h*0.76),(x+w*0.78,y+h*0.86)]
    for a,b in zip(pts[:-1], pts[1:]): add_line(slide,a[0],a[1],b[0],b[1],pal['accent'],1.4)
    for t in [0.33,0.62]: add_line(slide,x+w*t,y+h*(0.50+t*0.2),x+w*(t+0.08),y+h*(0.42+t*0.15),pal['accent'],0.8)

def draw_sensor(slide,x,y,w,h,pal):
    for i in range(4):
        cx = x + w*(0.18+i*0.20)
        oval(slide,cx-w*0.04,y+h*0.55,w*0.08,h*0.08,pal['white'],pal['primary'],0.8)
        add_line(slide,cx,y+h*0.59,cx,y+h*0.32,pal['primary'],0.7)
        for r in [0.13,0.20]:
            arc = slide.shapes.add_shape(MSO_SHAPE.ARC,*box(cx-w*r/2,y+h*(0.18-r/2),w*r,h*r))
            arc.line.color.rgb = rgb(pal['secondary']); arc.line.width = Pt(0.5); arc.fill.background()

def draw_monitoring_site(slide,x,y,w,h,pal):
    rect(slide,x+w*0.05,y+h*0.65,w*0.90,h*0.08,pal['line'],pal['line'],0.2)
    for i in range(3):
        bx=x+w*(0.12+i*0.22); by=y+h*(0.44-0.06*i)
        rect(slide,bx,by,w*0.16,h*(0.21+0.06*i),pal['neutral'],pal['primary'],0.6)
    draw_sensor(slide,x+w*0.60,y+h*0.15,w*0.32,h*0.55,pal)

def draw_civil_structure(slide,x,y,w,h,pal):
    rect(slide,x+w*0.08,y+h*0.70,w*0.84,h*0.06,pal['line'],pal['line'],0.2)
    for i in range(3):
        add_line(slide,x+w*(0.20+i*0.24),y+h*0.25,x+w*(0.20+i*0.24),y+h*0.70,pal['primary'],1.4)
    for j in range(3):
        rect(slide,x+w*0.12,y+h*(0.25+j*0.15),w*0.72,h*0.025,pal['secondary'],pal['secondary'],0.2)

def draw_mesh(slide,x,y,w,h,pal):
    rows, cols = 4, 5
    for i in range(cols): add_line(slide,x+w*i/(cols-1),y,x+w*i/(cols-1),y+h,pal['primary'],0.45)
    for j in range(rows): add_line(slide,x,y+h*j/(rows-1),x+w,y+h*j/(rows-1),pal['primary'],0.45)
    for i in range(cols-1):
        for j in range(rows-1): add_line(slide,x+w*i/(cols-1),y+h*j/(rows-1),x+w*(i+1)/(cols-1),y+h*(j+1)/(rows-1),pal['secondary'],0.3)

def draw_fe_result(slide,x,y,w,h,pal):
    draw_mesh(slide,x,y,w,h*0.75,pal)
    vals=[0.25,0.42,0.68,0.50,0.82]
    for i,v in enumerate(vals[:-1]):
        add_line(slide,x+w*(0.10+i*0.18),y+h*(0.85-v*0.35),x+w*(0.10+(i+1)*0.18),y+h*(0.85-vals[i+1]*0.35),pal['accent'],1.2)

def draw_vision(slide,x,y,w,h,pal):
    rect(slide,x,y+h*0.35,w*0.18,h*0.22,pal['white'],pal['primary'],0.8)
    oval(slide,x+w*0.14,y+h*0.39,w*0.08,h*0.14,pal['neutral'],pal['primary'],0.8)
    add_arrow(slide,x+w*0.26,y+h*0.46,x+w*0.42,y+h*0.46,pal['line'],0.8)
    rect(slide,x+w*0.45,y+h*0.25,w*0.22,h*0.42,pal['white'],pal['secondary'],0.8)
    for i in range(3): add_line(slide,x+w*0.48,y+h*(0.34+i*0.08),x+w*0.63,y+h*(0.34+i*0.08),pal['secondary'],0.4)
    rect(slide,x+w*0.74,y+h*0.25,w*0.18,h*0.42,pal['neutral'],pal['accent'],0.8)
    draw_crack(slide,x+w*0.74,y+h*0.25,w*0.18,h*0.42,pal)

def draw_molecule(slide,x,y,w,h,pal):
    coords=[]
    for i in range(4):
        for j in range(3): coords.append((x+w*(0.18+i*0.20), y+h*(0.20+j*0.25)))
    for i,p in enumerate(coords):
        if i+1 < len(coords): add_line(slide,p[0],p[1],coords[i+1][0],coords[i+1][1],pal['secondary'],0.35)
        oval(slide,p[0]-w*0.028,p[1]-h*0.028,w*0.056,h*0.056,pal['white'],pal['primary'],0.7)

def draw_loop(slide,x,y,w,h,pal):
    for rot in [0,90,180,270]:
        arc = slide.shapes.add_shape(MSO_SHAPE.ARC,*box(x+w*0.18,y+h*0.18,w*0.64,h*0.64))
        arc.rotation = rot; arc.line.color.rgb = rgb(pal['primary']); arc.line.width = Pt(1.2); arc.fill.background()
    oval(slide,x+w*0.38,y+h*0.38,w*0.24,h*0.24,pal['neutral'],pal['accent'],0.7)

def draw_optimization_loop(slide,x,y,w,h,pal):
    draw_loop(slide,x,y,w,h,pal)
    for i,lab in enumerate(['Design','Sim','Update']):
        ang=2*math.pi*i/3-math.pi/2
        cx=x+w*(0.50+0.32*math.cos(ang)); cy=y+h*(0.50+0.32*math.sin(ang))
        oval(slide,cx-w*0.07,cy-h*0.07,w*0.14,h*0.14,pal['white'],pal['primary'],0.7)
        textbox(slide,lab,cx-w*0.065,cy-h*0.025,w*0.13,h*0.05,5.6,False,pal['text'],PP_ALIGN.CENTER)

def draw_multiscale_bridge(slide,x,y,w,h,pal):
    for i,(r,lab) in enumerate([(0.20,'micro'),(0.36,'meso'),(0.52,'macro')]):
        oval(slide,x+w*(0.08+i*0.28),y+h*0.28,w*0.18,h*0.28,pal['white'],pal['primary' if i==2 else 'secondary'],0.8)
        textbox(slide,lab,x+w*(0.08+i*0.28),y+h*0.38,w*0.18,h*0.05,5.8,False,pal['text'],PP_ALIGN.CENTER)
        if i<2: add_arrow(slide,x+w*(0.26+i*0.28),y+h*0.42,x+w*(0.36+i*0.28),y+h*0.42,pal['line'],0.7)

def draw_process_stack(slide,x,y,w,h,pal):
    for i in range(4):
        rect(slide,x+w*(0.12+i*0.06),y+h*(0.12+i*0.13),w*0.68,h*0.09,pal['neutral'] if i<3 else pal['secondary'],pal['primary'],0.6,True)
        add_arrow(slide,x+w*(0.46+i*0.06),y+h*(0.21+i*0.13),x+w*(0.50+i*0.06),y+h*(0.25+i*0.13),pal['line'],0.55)

def draw_chart(slide,x,y,w,h,pal,values=None):
    values = values or [0.36,0.52,0.70]
    values = [max(0.05,min(0.88,float(v))) for v in values[:5]]
    add_line(slide,x+w*0.12,y+h*0.82,x+w*0.90,y+h*0.82,pal['line'],0.6)
    for i,v in enumerate(values):
        bw=w*0.10; bx=x+w*(0.20+i*0.14); by=y+h*(0.82-v)
        fill = pal['secondary'] if i==len(values)-1 else '#D9E2EC'
        rect(slide,bx,by,bw,h*v,fill,fill,0.2)

def draw_object(slide, obj, pal, parent=None, font='Arial'):
    x,y,w,h = object_box(parent,obj)
    typ = obj.get('type','dataset')
    if typ in ('dataset','data'): draw_dataset(slide,x,y,w,h,pal)
    elif typ == 'neural_network': draw_neural(slide,x,y,w,h,pal,obj.get('layers'))
    elif typ == 'material_microstructure': draw_micro(slide,x,y,w,h,pal)
    elif typ == 'magnetic_domain': draw_magnetic(slide,x,y,w,h,pal)
    elif typ == 'rare_earth_magnet': draw_rare_earth_magnet(slide,x,y,w,h,pal)
    elif typ == 'crack_defect': draw_crack(slide,x,y,w,h,pal)
    elif typ == 'sensor_array': draw_sensor(slide,x,y,w,h,pal)
    elif typ == 'monitoring_site': draw_monitoring_site(slide,x,y,w,h,pal)
    elif typ == 'civil_structure': draw_civil_structure(slide,x,y,w,h,pal)
    elif typ == 'fem_mesh': draw_mesh(slide,x,y,w,h,pal)
    elif typ == 'finite_element_result': draw_fe_result(slide,x,y,w,h,pal)
    elif typ == 'vision_pipeline': draw_vision(slide,x,y,w,h,pal)
    elif typ == 'molecule_grid': draw_molecule(slide,x,y,w,h,pal)
    elif typ == 'mechanism_loop': draw_loop(slide,x,y,w,h,pal)
    elif typ == 'optimization_loop': draw_optimization_loop(slide,x,y,w,h,pal)
    elif typ == 'multiscale_bridge': draw_multiscale_bridge(slide,x,y,w,h,pal)
    elif typ == 'process_stack': draw_process_stack(slide,x,y,w,h,pal)
    elif typ == 'performance_chart': draw_chart(slide,x,y,w,h,pal,obj.get('values'))
    else: draw_dataset(slide,x,y,w,h,pal)
    if obj.get('label'):
        textbox(slide,obj['label'],x,y+h*0.82,w,h*0.16,7.5,False,pal['muted'],PP_ALIGN.CENTER,font)

def draw_block(slide, block, pal, font):
    x,y,w,h = [float(block[k]) for k in ('x','y','w','h')]
    stroke = pal[TYPE_TO_COLOR.get(block.get('type','process'), 'primary')]
    rect(slide,x,y,w,h,pal['neutral'],stroke,1.0,True)
    for obj in block.get('objects',[]) or []:
        draw_object(slide,obj,pal,block,font)
    label = block.get('label','')
    textbox(slide,label,x+0.025,y+0.025,w-0.05,h*0.16,11.5,True,pal['text'],PP_ALIGN.CENTER,font)
    if block.get('label_secondary'):
        textbox(slide,block.get('label_secondary'),x+0.025,y+h*0.17,w-0.05,h*0.10,8.0,False,pal['muted'],PP_ALIGN.CENTER,font)
    bullets = block.get('bullets',[]) or []
    if bullets:
        txt = '\n'.join([f"- {b}" for b in bullets[:3]])
        textbox(slide,txt,x+0.035,y+h*0.66,w-0.07,h*0.28,8.4,False,pal['muted'],PP_ALIGN.LEFT,font)
    return {'x':x,'y':y,'w':w,'h':h}

def center(b): return b['x']+b['w']/2,b['y']+b['h']/2

def draw_bg(slide,pal):
    rect(slide,0,0,1,1,pal['background'],pal['background'],0)
    rect(slide,0,0,1,0.09,pal['neutral'],pal['neutral'],0)

def flatten_content(ac):
    if isinstance(ac,str): return ac
    if isinstance(ac,dict):
        parts=[]
        for k,v in ac.items():
            val='; '.join(map(str,v)) if isinstance(v,list) else str(v)
            parts.append(f"{k}: {val}")
        return '\n'.join(parts)
    return str(ac)

def add_notes_slide(prs,spec,pal,font):
    slide = prs.slides.add_slide(prs.slide_layouts[6]); draw_bg(slide,pal)
    textbox(slide,'Generation notes and provenance',0.06,0.06,0.88,0.08,20,True,pal['text'],PP_ALIGN.LEFT,font)
    content = flatten_content(spec.get('abstract_content',''))
    pconf = spec.get('prompt_confirmation',{})
    txt = 'Abstract content brief\n' + content + '\n\nPrompt confirmation\n' + json.dumps(pconf,ensure_ascii=False,indent=2)
    textbox(slide,txt,0.08,0.18,0.84,0.70,10,False,pal['text'],PP_ALIGN.LEFT,font)

def add_quality_slide(prs,spec,pal,font):
    slide = prs.slides.add_slide(prs.slide_layouts[6]); draw_bg(slide,pal)
    textbox(slide,'Quality gates',0.06,0.06,0.88,0.08,20,True,pal['text'],PP_ALIGN.LEFT,font)
    gates=['Q0 content brief sufficient','Q1 visible claims traceable','Q2 one central visual story','Q3 editable vector construction','Q4 typography and language discipline','Q5 palette and contrast consistency','Q6 no raster/media/OLE/external assets','Q7 requested package complete','Q8 palette preview available when needed']
    for i,g in enumerate(gates):
        y=0.18+i*0.07
        oval(slide,0.09,y,0.025,0.045,pal['secondary'],pal['secondary'],0.2)
        textbox(slide,g,0.13,y-0.004,0.74,0.055,10.5,False,pal['text'],PP_ALIGN.LEFT,font)

def add_palette_slide(prs,font):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    rect(slide,0,0,1,1,'#FFFFFF','#FFFFFF',0)
    textbox(slide,'Palette strip preview',0.055,0.035,0.72,0.06,20,True,'#111827',PP_ALIGN.LEFT,font)
    textbox(slide,'Order: background, neutral, primary, secondary, accent, line, text. All swatches are editable vector rectangles.',0.055,0.10,0.86,0.045,9.5,False,'#52616B',PP_ALIGN.LEFT,font)
    y0=0.18; row_h=0.062; gap=0.012
    for idx,(name,pal) in enumerate(PALETTES.items()):
        y=y0+idx*(row_h+gap)
        textbox(slide,name,0.055,y+0.006,0.20,row_h*0.75,8.2,True,'#111827',PP_ALIGN.LEFT,font)
        x=0.265
        for j,key in enumerate(PALETTE_ORDER):
            rect(slide,x+j*0.082,y,0.075,row_h,pal[key],'#C8CED6',0.35)
        textbox(slide,'  '.join([pal[k] for k in PALETTE_ORDER]),0.86,y+0.007,0.12,row_h*0.72,5.2,False,'#374151',PP_ALIGN.LEFT,font)

def build(spec,out):
    prs = Presentation(); prs.slide_width=Inches(SLIDE_W); prs.slide_height=Inches(SLIDE_H)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    pal = PALETTES.get(spec.get('palette_name','nature_blue'), PALETTES['nature_blue'])
    font = font_for(spec)
    draw_bg(slide,pal)
    textbox(slide,spec.get('title','Graphical abstract'),0.06,0.035,0.72,0.07,20,True,pal['text'],PP_ALIGN.LEFT,font)
    if spec.get('subtitle'):
        textbox(slide,spec.get('subtitle'),0.06,0.105,0.70,0.045,9.5,False,pal['muted'],PP_ALIGN.LEFT,font)
    badge = spec.get('journal_profile','graphical abstract').replace('_',' ')
    textbox(slide,badge,0.78,0.045,0.16,0.045,8.5,False,pal['primary'],PP_ALIGN.RIGHT,font)

    blocks = layout_blocks(spec.get('blocks',[]) or [], spec.get('layout_pattern','left_to_right_pipeline'))
    block_map = {b.get('id',str(i)): b for i,b in enumerate(blocks)}
    for conn in spec.get('connectors',[]) or []:
        a = block_map.get(conn.get('from')); b = block_map.get(conn.get('to'))
        if not a or not b: continue
        x1,y1 = center(a); x2,y2 = center(b)
        if conn.get('style') == 'elbow': add_elbow_arrow(slide,x1,y1,x2,y2,pal['line'],0.9)
        else: add_arrow(slide,x1,y1,x2,y2,pal['line'],0.9)
        if conn.get('label'):
            textbox(slide,conn['label'],(x1+x2)/2-0.045,(y1+y2)/2-0.025,0.09,0.04,7.3,False,pal['muted'],PP_ALIGN.CENTER,font)
    for b in blocks:
        draw_block(slide,b,pal,font)
    for obj in spec.get('objects',[]) or []:
        draw_object(slide,obj,pal,None,font)
    claim = spec.get('central_claim') or spec.get('visual_claim')
    if claim:
        rect(slide,0.12,0.86,0.76,0.075,pal['white'],pal['accent'],1.0,True)
        textbox(slide,claim,0.14,0.875,0.72,0.04,10.5,True,pal['text'],PP_ALIGN.CENTER,font)
    opts = spec.get('output_options',{}) or {}
    if opts.get('include_notes_slide'): add_notes_slide(prs,spec,pal,font)
    if opts.get('include_quality_slide'): add_quality_slide(prs,spec,pal,font)
    if opts.get('include_palette_slide'): add_palette_slide(prs,font)
    prs.save(out)

def main():
    if len(sys.argv) != 3:
        print('Usage: build_graphical_abstract_pptx.py <spec.json> <out.pptx>')
        return 2
    spec = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    build(spec, sys.argv[2])
    print(f'Wrote {sys.argv[2]}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
