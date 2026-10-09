import math, re

def oklch_to_hex(L, C, H):
    h = math.radians(H)
    a, b = C * math.cos(h), C * math.sin(h)
    l_ = L + 0.3963377774*a + 0.2158037573*b
    m_ = L - 0.1055613458*a - 0.0638541728*b
    s_ = L - 0.0894841775*a - 1.2914855480*b
    l, m, s = l_**3, m_**3, s_**3
    r =  4.0767416621*l - 3.3077115913*m + 0.2309699292*s
    g = -1.2684380046*l + 2.6097574011*m - 0.3413193965*s
    bb= -0.0041960863*l - 0.7034186147*m + 1.7076147010*s
    def f(u):
        u = u if u <= 0.0031308 else 1.055*(abs(u)**(1/2.4)) - 0.055
        return max(0, min(255, round(u*255)))
    return "#%02X%02X%02X" % (f(r), f(g), f(bb))

def parse(s):
    m = re.match(r'oklch\(\s*([\d.]+)%?\s+([\d.]+)\s+([\d.]+)', s.strip())
    if not m: return None
    L = float(m.group(1)); L = L/100 if L > 1.5 else L
    return oklch_to_hex(L, float(m.group(2)), float(m.group(3)))

if __name__ == '__main__':
    import sys
    block = open('nuxt_ui_colors.txt', encoding='utf-8').read()
    for fam in ['primary','secondary','neutral','error','success','warning','info']:
        print(f"\n--- {fam} ---")
        for m in re.finditer(rf'--ui-color-{fam}-([\w-]+)\s*:\s*var\([^,]+,\s*(oklch\([^)]+\))\)', block):
            step, val = m.group(1), parse(m.group(2))
            print(f"  {step:<6} {val}")
