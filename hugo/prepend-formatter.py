#!/usr/bin/env python
# coding: utf-8

# 作用：如果 frontmatter 缺少开头的分隔符，则追加上

from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
    post_dir = "/Users/minicloudsky/codes/hugo-blog-backup/blog/content/post"
    for f in listdir(post_dir):
        fname = join(post_dir, f)
        if isfile(fname):
            new_content = []
            with open(fname) as post:
                first_line = True
                for line in post:
                    if first_line and '--' not in line:
                        new_content.append('---\n')
                    first_line = False

                    new_content.append(line)

            with open(fname, 'w') as post:
                post.write(''.join(new_content))