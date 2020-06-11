#!/usr/bin/env python3
# coding: utf-8

# 作用：把 frontmatter 中 categories/tags 变成严格的数组格式
# pip install pyyaml
import yaml
from os import listdir
from os.path import isfile, join


def pretty_print(stream):
    try:
        front = yaml.safe_load(stream)
        print("front: ", front)
        if 'categories' in front:
            if isinstance(front['categories'], list) is False:
                front['categories'] = [front['categories']]

        if 'tags' in front:
            if isinstance(front['tags'], list) is False:
                front['categories'] = [front['tags']]

        return yaml.dump(front, default_flow_style=False, allow_unicode=True)
    except yaml.YAMLError as exc:
        print(exc)
        return None


def iter_dir(post_dir):
    for f in listdir(post_dir):
        fname = join(post_dir, f)
        if isfile(fname):
            frontmatters = []
            body = []
            with open(fname) as post:
                dashed_lines = 0
                for line in post:
                    if dashed_lines < 2 and '--' in line:
                        dashed_lines += 1
                        continue

                    if dashed_lines < 2:
                        frontmatters.append(line)
                    else:
                        body.append(line)

            with open(fname, 'w', encoding='utf8') as post:
                fm = ''.join(frontmatters)
                formated = pretty_print(fm)
                if formated:
                    post.write('---\n{}---\n'.format(formated))
                    post.write(''.join(body))
                else:
                    print('err frontmatter: %s' % (fname,))


if __name__ == '__main__':
    post_dir = "/Users/minicloudsky/codes/hugo-blog-backup/blog/content/post"
    iter_dir(post_dir)
