pairs = [

    ('Algeria', 'dz'),
    ('Egypt', 'eg'),
    ('Israel', 'il'),
    ('Jordan', 'jo'),
    ('Lebanon', 'lb'),
    ('Libya', 'ly'),
    ('Morocco', 'ma'),
    ('Palestine', 'ps'),
    ('Tunisia', 'tn'),

    ('Armenia', 'am'),
    ('Azerbaijan', 'az'),
    ('Belarus', 'by'),
    ('Georgia', 'ge'),
    ('Moldova', 'md'),
    ('Ukraine', 'ua'),

]
if key_based:
    res = {}
    for p in pairs:
        res[p[1]] = p[0]
    return res

res = {}
for p in pairs:
    res[p[0]] = p[1]

return res