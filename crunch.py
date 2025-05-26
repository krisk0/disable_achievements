import glob, os, re, sys

def die(x):
    print(x)
    sys.exit(1)

try:
    with open('disable_achievements/descriptor.mod', 'rb'):
        ''
except:
    die('Must be run from directory containing readme.md')

tgt_file = 'common/scripted_effects/00_achievement_effects.txt'

def do_it(i, o):
    os.makedirs(os.path.dirname(o), exist_ok=True)
    with open(i, 'rb') as ii:
        with open(o, 'wb') as oo:
            do_with_file(ii, oo)

s_patt = re.compile(r'(\S+) = {')
def do_with_file(i, o):
    c = 0
    for j in i:
        k = j.decode("utf-8")
        m = s_patt.match(k)
        if m:
            n = m[1] + ' = {}\n'
            o.write(n.encode('utf-8'))
            c += 1
    if c:
        print('Success, %d effects emptied' % c)

try:
    p = sys.argv[1]
    p = p.replace('\\','/')
except:
    die('Search path not given')

f_patt = re.compile('.+/' + tgt_file)
for f in glob.glob(p + '/**/*.txt', recursive=True):
    f = f.replace('\\','/')
    if f_patt.match(f):
        do_it(f, 'disable_achievements/' + tgt_file)
        sys.exit(0)
print('Failed to find %s in %s' % (tgt_file, p))
