def rgb_to_hls(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    # XXX Can optimize (maxc+minc) and (maxc-minc)
    l = (minc+maxc)/2.0
    if minc == maxc:
        return 0.0, l, 0.0
    if l <= 0.5:
        s = (maxc-minc) / (maxc+minc)
    else:
        s = (maxc-minc) / (2.0-maxc-minc)
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, l, s

def _v(m1, m2, hue):
    hue = hue % 1.0
    if hue < 1/6:
        return m1 + (m2-m1)*hue*6.0
    if hue < 0.5:
        return m2
    if hue < 2/3:
        return m1 + (m2-m1)*(2/3-hue)*6.0
    return m1

def hls_to_rgb(h, l, s):
    if s == 0.0:
        return l, l, l
    if l <= 0.5:
        m2 = l * (1.0+s)
    else:
        m2 = l+s-(l*s)
    m1 = 2.0*l - m2
    return (_v(m1, m2, h+1/3), _v(m1, m2, h), _v(m1, m2, h-1/3))


#get colors
def getRed(img):
    values = []
    for row in img:
        for col in row:
            values.append(col[0])
    return values

def getGreen(img):
    values = []
    for row in img:
        for col in row:
            values.append(col[1])
    return values

def getBlue(img):
    values = []
    for row in img:
        for col in row:
            values.append(col[2])
    return values

def getRGB(img):
    red = np.mean(getRed(img))
    green = np.mean(getGreen(img))
    blue = np.mean(getBlue(img))
    return red, green, blue


def apply_HLS(img, ref_img):
    r, g, b = getRGB(img)
    ref_r, ref_g, ref_b = getRGB(ref_img)
    h, l, s = rgb_to_hls(r, g, b)
    ref_h, ref_l, ref_s = rgb_to_hls(ref_r, ref_g, ref_b)
    
    return hls_to_rgb(h, ref_l, ref_s)