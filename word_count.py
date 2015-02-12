__version__ = '0.1.0'

import re


def word_count(content):
    """
    Counts the number of words in the specified string.
    Based on the regexes / logic from Countable.js:
    https://github.com/RadLikeWhoa/Countable
    (recommended to use this function for back-end validation, in
    conjunction with Countable.js for a front-end live word count).
    """

    trim_re = re.compile(r'^\s+|\s+$')
    striptags_re = re.compile(r'<\/?[a-z][^>]*>', re.IGNORECASE)
    stripsymbols_re = re.compile(r'[\'";:,.?\-!]+')
    words_re = re.compile(r'\S+')

    c = trim_re.sub('', content)
    c = striptags_re.sub('', content)
    c = stripsymbols_re.sub('', content)

    match = words_re.findall(c)

    return match and len(match) or 0
