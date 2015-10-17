#!/usr/bin/env python
from itertools import chain, permutations

import requests


def main():
    choices1 = map(lambda x: x[::-1], ['reverse', 'question'])
    choices2 = map(lambda x: x[::-1], ['absolem', 'stupid', 'you'])
    base_url = 'http://46.101.159.170/0SQJHQ1G/esrever'
    for perm1 in ['']: # permutations(choices1):
        url1 = base_url + '/'.join(perm1) + '/'
        for perm2 in chain(
                permutations(choices2, 2),
                permutations(choices2, 3)):
            url2 = url1 + '-'.join(perm2) + '/'
            res = requests.get(url2)
            if res.status_code != 404:
                print url2


def main_json():
    base_url = 'http://46.101.159.170/0SQJHQ1G/esrever/%s'
    number = 123
    i = 1
    print i, '123'
    while True:
        i += 1
        res = requests.get(base_url % str(number)[::-1])
        json = res.json()
        if True or len(json) > 1:  # json.get('absolem'):
            print i, json
        number = json['number']

# 3 {u'absolem': u"There's a long way in front of you. Go forward if you want to get home.", u'number': 9622}
# 19 {u'absolem': u"I've been in underland, in marmoreal and even in outlands. Does it mean I've been in undelandmarmorealoutlands too?", u'number': 4239}
# 30 {u'absolem': u"I hope you enjoy the ride. I've put the words in wrong order and called you badly. I often call people names - I'm just a caterpillar. But how would you call me?", u'number': 7987}
# 69 {u'absolem': u"I'm at my finish. The way is yours now. Just remember the times you've listen to my words.", u'number': 2687}
# 76 {u'number': u"There's a huge gulf in front of you. Going further would not be a smart thing."}


def main_json_end():
    arr = [9622, 4239, 7987, 2687]
    base_url = 'http://46.101.159.170/0SQJHQ1G/esrever/%s/'
    url = base_url % '-'.join(map(lambda x: str(x)[::-1], arr))
    print url
    res = requests.get(url)
    print res.content


if __name__ == '__main__':
    number = "439 944 737 84"
    print 'the tel.', '00' + number[::-1]
    exit(0)

    main_json()

"""
1 123
2 {u'number': 2294}
3 {u'number': 439}
4 {u'absolem': u"There's a long way in front of you. Go forward if you want to get home.", u'number': 9622}
5 {u'number': 6945}
6 {u'number': 9611}
7 {u'number': 7537}
8 {u'number': 9138}
9 {u'number': 3017}
10 {u'number': 6612}
11 {u'number': 6033}
12 {u'number': 6733}
13 {u'number': 6248}
14 {u'number': 62}
15 {u'number': 6904}
16 {u'number': 8322}
17 {u'number': 8137}
18 {u'number': 4049}
19 {u'number': 944}
20 {u'absolem': u"I've been in underland, in marmoreal and even in outlands. Does it mean I've been in undelandmarmorealoutlands too?", u'number': 4239}
21 {u'number': 4990}
22 {u'number': 7890}
23 {u'number': 146}
24 {u'number': 4416}
25 {u'number': 8851}
26 {u'number': 3456}
27 {u'number': 8249}
28 {u'number': 5677}
29 {u'number': 1514}
30 {u'number': 737}
31 {u'absolem': u"I hope you enjoy the ride. I've put the words in wrong order and called you badly. I often call people names - I'm just a caterpillar. But how would you call me?", u'number': 7987}
32 {u'number': 1134}
33 {u'number': 2010}
34 {u'number': 7655}
35 {u'number': 2113}
36 {u'number': 8783}
37 {u'number': 4482}
38 {u'number': 1842}
39 {u'number': 4796}
40 {u'number': 9456}
41 {u'number': 4819}
42 {u'number': 5111}
43 {u'number': 4691}
44 {u'number': 3672}
45 {u'number': 7167}
46 {u'number': 3715}
47 {u'number': 1742}
48 {u'number': 9066}
49 {u'number': 586}
50 {u'number': 9174}
51 {u'number': 5079}
52 {u'number': 2085}
53 {u'number': 2542}
54 {u'number': 5547}
55 {u'number': 9812}
56 {u'number': 5262}
57 {u'number': 7006}
58 {u'number': 73}
59 {u'number': 3270}
60 {u'number': 9249}
61 {u'number': 2587}
62 {u'number': 1733}
63 {u'number': 7629}
64 {u'number': 7982}
65 {u'number': 5349}
66 {u'number': 329}
67 {u'number': 434}
68 {u'number': 759}
69 {u'number': 84}
70 {u'absolem': u"I'm at my finish. The way is yours now. Just remember the times you've listen to my words.", u'number': 2687}
71 {u'number': 8535}
72 {u'number': 8282}
73 {u'number': 5825}
74 {u'number': 7969}
75 {u'number': 1085}
76 {u'number': 7031}
77 {u'number': u"There's a huge gulf in front of you. Going further would not be a smart thing."}
"""
