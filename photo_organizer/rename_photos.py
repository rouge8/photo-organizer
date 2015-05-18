from collections import defaultdict
from datetime import datetime
import os
import shutil

import click
import exifread


def rename(src, dst):
    click.echo('%s -> %s' % (src, dst))
    shutil.move(src, dst)


@click.command()
@click.option('--input-dir', type=click.Path(file_okay=False, dir_okay=True, exists=True),
              required=True, help='Input directory full of photos')
def main(input_dir):
    src_files_by_renamed = defaultdict(list)

    os.chdir(input_dir)

    for filename in sorted(os.listdir('.')):
        _, ext = os.path.splitext(filename)

        if ext.lower() not in {'.jpg', '.png'}:
            continue

        with open(filename, 'rb') as f:
            tags = exifread.process_file(f)

        timestamp = tags.get('Image DateTime')

        if not timestamp:
            click.echo('No timestamp found in %s, ignoring.' % (filename,), err=True)
            continue

        timestamp = datetime.strptime(timestamp.values, '%Y:%m:%d %H:%M:%S')

        hdr = bool(tags.get('MakerNote HDRImageType'))

        renamed = timestamp.strftime('%Y-%m-%d %H.%M.%S')
        if hdr:
            renamed += ' HDR'
        renamed += ext.lower()

        src_files_by_renamed[renamed].append(filename)

    for renamed, src_files in src_files_by_renamed.items():
        if len(src_files) == 1:
            src = src_files[0]
            rename(src, renamed)
        else:
            for i, src in enumerate(src_files, 1):
                basename, ext = os.path.splitext(renamed)
                renamed_with_count = '{}-{}{}'.format(basename, i, ext)
                rename(src, renamed_with_count)
