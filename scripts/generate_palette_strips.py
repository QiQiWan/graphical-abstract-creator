#!/usr/bin/env python3
"""Generate an editable vector PowerPoint palette-strip preview."""
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
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
ORDER = ["background", "neutral", "primary", "secondary", "accent", "line", "text"]


def rgb(h):
    h = h.strip().lstrip('#')
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))


def box(x,y,w,h):
    return Inches(x*SLIDE_W), Inches(y*SLIDE_H), Inches(w*SLIDE_W), Inches(h*SLIDE_H)


def add_text(slide, text, x, y, w, h, size=9, bold=False, color="#111827", align=PP_ALIGN.LEFT):
    sh = slide.shapes.add_textbox(*box(x,y,w,h))
    tf = sh.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = rgb(color)
    return sh


def add_rect(slide, x, y, w, h, fill, line="#D1D5DB", width=0.4):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, *box(x,y,w,h))
    sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    sh.line.color.rgb = rgb(line); sh.line.width = Pt(width)
    return sh


def build(out):
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(slide,0,0,1,1,"#FFFFFF","#FFFFFF",0)
    add_text(slide,"Graphical Abstract Creator: editable palette strips",0.055,0.035,0.72,0.06,20,True,"#111827")
    add_text(slide,"All strips are native PowerPoint rectangles and editable labels. Order: background, neutral, primary, secondary, accent, line, text.",0.055,0.10,0.86,0.045,9.5,False,"#52616B")
    y0 = 0.18
    row_h = 0.062
    gap = 0.012
    for idx,(name,pal) in enumerate(PALETTES.items()):
        y = y0 + idx*(row_h+gap)
        add_text(slide,name,0.055,y+0.006,0.20,row_h*0.75,8.2,True,"#111827")
        x = 0.265
        for j,key in enumerate(ORDER):
            col = pal[key]
            add_rect(slide,x+j*0.082,y,0.075,row_h,col,"#C8CED6",0.35)
        add_text(slide,"  ".join([pal[k] for k in ORDER]),0.86,y+0.007,0.12,row_h*0.72,5.2,False,"#374151",PP_ALIGN.LEFT)
    prs.save(out)
    print(f"Wrote {out}")


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("palette_strips.pptx")
    out.parent.mkdir(parents=True, exist_ok=True)
    build(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
