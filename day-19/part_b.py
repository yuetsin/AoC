#!/usr/bin/env python3
import json
import itertools

def get_input(f: str='./input_fixed') -> list[str]:
    with open(f, 'r') as f:
        return [v for v in [v.strip() for v in f.readlines()] if v]


dictionaries = {}
rules = get_input('./rules_fixed')
rule_count = len(rules)

while len(dictionaries) < rule_count - 3:
    print('len(d) =', len(dictionaries), 'rule_count =', rule_count)
    for line in rules:
        ident, body = line.split(': ')
        if body.startswith('"'):
            dictionaries.update({ident: set([eval(body)])})
        else:
            bodies = body.split(' | ')
            possible_body_strs = set()

            ok = True
            for bdy in bodies:
                try:
                    # print([dictionaries[v] for v in bdy.split(' ')])
                    for p in itertools.product(*[dictionaries[v] for v in bdy.split(' ')]):
                        possible_body_strs.add(''.join(p))
                except KeyError:
                    # print(e)
                    ok = False
                    break
            if ok:
                dictionaries.update({ident: possible_body_strs})

# print(dictionaries)
# print(len(dictionaries['0']))


msgs = set(get_input('./messages'))


"""
8: 42 | 42 8
11: 42 31 | 42 11 31
0: 8 11
"""
set_31 = {'bbabbbab', 'bbbbaaaa', 'aaaaaaab', 'abbaabba', 'babbbaab', 'bababbbb', 'bbaabaab', 'bbaabaaa', 'abbaaaab', 'abaababa', 'aaaabbba', 'bbabbbaa', 'babbaaab', 'aabbbbbb', 'bbbabbbb', 'baabbbab', 'baaabaab', 'bbbabbba', 'baababbb', 'abbbabbb', 'aabbbaab', 'bbaaabaa', 'baabbbbb', 'abbabbaa', 'aabbbbaa', 'babbbbaa', 'bbbbaaba', 'abbbbbba', 'abbabbba', 'abbbaaaa', 'bbabbaab', 'abbaabab', 'bbabaaaa', 'abbababa', 'aaabaaba', 'bababaaa', 'bbbbbaba', 'abbbbbab', 'babbabbb', 'abbbbaba', 'aabbbaaa', 'bbbbbabb', 'bbaaaaba', 'abaabbba', 'bbbaaabb', 'abaabaaa', 'bbaabbba', 'baaaaaba', 'bbbabaab', 'abbabbbb', 'baababab', 'bababbba', 'aababbaa', 'ababaabb', 'aababbbb', 'baabbaaa', 'baaabbbb', 'aabababb', 'bbbabbaa', 'aabbabbb', 'abababba', 'abbbabaa', 'baaaabbb', 'babaabba', 'bbbbbbab', 'abbbbbbb', 'bbbabbab', 'babbbbba', 'aaabbaba', 'ababbaab', 'bbabbaaa', 'aaababab', 'babbbabb', 'abaaaaba', 'aababbab', 'aabaabab', 'aaaababa', 'bbbbabba', 'abbbaaab', 'abaaabba', 'baaaaaab', 'aaabbbba', 'babbbaaa', 'bbabbbbb', 'babbabab', 'aaabaaaa', 'babaaaba', 'babbbbbb', 'aabaaaaa', 'abbbbaaa', 'abaaaaab', 'babbabba', 'babbabaa', 'aabaaaba', 'baaabbab', 'bbbbbbba', 'abaabbaa', 'bbaaabbb', 'baabaaab', 'bbaabbab', 'baaabbba', 'baabbaba', 'abababab', 'abababbb', 'ababbbaa', 'aaabbaaa', 'baabbabb', 'abbbabab', 'babababb', 'aabbabab', 'baababba', 'bbbabaaa', 'bbbbaaab', 'babaaabb', 'abbabbab', 'aaabbabb', 'babababa', 'abbbabba', 'bbababba', 'aaaaabaa', 'abbbbaab', 'aaaabbab', 'abaababb', 'babaabab', 'bbbababa', 'baaabbaa', 'bbababab', 'aabbabba'}
set_42 = {'bbaaaaaa', 'aabbbbab', 'abaaabab', 'bbbaaaaa', 'abaabbab', 'aabbaaab', 'aaabbbaa', 'ababbbbb', 'bbaababa', 'baaabaaa', 'abaaaabb', 'bbababbb', 'baaaaabb', 'bbabaaab', 'aaaaaabb', 'aabbaabb', 'baabbbaa', 'babaabaa', 'aaababaa', 'aaaaabbb', 'aaabbbab', 'bbabaaba', 'abbabaaa', 'baabbbba', 'aababaaa', 'abbaaabb', 'abbaabbb', 'babaaaaa', 'aaaaaaaa', 'bbaaaabb', 'baababaa', 'aaaaabba', 'aabababa', 'bbbaabbb', 'abbaaaaa', 'bbababaa', 'aababaab', 'aabbbaba', 'aababbba', 'aabaaabb', 'bbbbabab', 'abaaaaaa', 'babbaaba', 'aaaaaaba', 'aabaaaab', 'abbaaaba', 'bbbaabab', 'bbaaaaab', 'bbabaabb', 'baabaabb', 'bbbbbaab', 'aaababbb', 'bbabbaba', 'bbbaaaab', 'ababaaba', 'baaaabaa', 'bbabbabb', 'aaaabbaa', 'baaaaaaa', 'bbbbbbbb', 'bbaabbaa', 'bababbaa', 'aabbbbba', 'aaaaabab', 'bbbaabba', 'abbbaaba', 'bbaaabba', 'baabaaba', 'bbbbabbb', 'aaababba', 'aabbabaa', 'bababbab', 'aaabaabb', 'abaabbbb', 'abbaabaa', 'abbabaab', 'bababaab', 'aabaabba', 'abaabaab', 'aaaabaab', 'bbbbabaa', 'bbaababb', 'babbbbab', 'aabaabaa', 'bbbaabaa', 'aaabaaab', 'ababbaba', 'bbbababb', 'babaabbb', 'abaaabbb', 'babbaaaa', 'baaababa', 'bbbbbaaa', 'ababaaab', 'baaaabba', 'abababaa', 'ababbbab', 'baabaaaa', 'ababbabb', 'aabbbabb', 'babaaaab', 'baaababb', 'abbbaabb', 'bbaabbbb', 'bbbbbbaa', 'ababbaaa', 'abbbbbaa', 'aabbaaba', 'bbbaaaba', 'aaabbbbb', 'ababbbba', 'bbbbaabb', 'abaaabaa', 'babbaabb', 'abbbbabb', 'aaaabaaa', 'ababaaaa', 'abbababb', 'aaaabbbb', 'baabbaab', 'baaaabab', 'aaabbaab', 'aabbaaaa', 'aaaababb', 'bbabbbba', 'babbbaba', 'bbaaabab', 'aabaabbb'}


def is_11(msg: str) -> bool:
    if msg == '':
        return True
    if not any([msg.startswith(s) for s in set_42]):
        return False
    if not any([msg.endswith(s) for s in set_31]):
        return False
    return is_11(msg[8:-8])

def is_8(msg: str) -> bool:
    if msg == '':
        return True
    if not any([msg.startswith(s) for s in set_42]):
        return False
    return is_8(msg[8:])

def is_0(msg: str) -> bool:
    for i in range(8, len(msg), 8):
        if is_8(msg[:i]) and is_11(msg[i:]):
            return True
    return False

print(sum([1 if is_0(v) else 0 for v in msgs]))

