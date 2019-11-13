from typing import NamedTuple, List, Tuple, Optional
from datetime import datetime


class ImageDetails(NamedTuple):
    width: int
    pairs: List[Tuple[int, int]]


class ImageDecompressor(object):

    def __init__(self, img_str):
        self._img_str = img_str
        self.width, self._pairs = ImageDecompressor._derive_pairs(img_str)
        self.running_pairs = ImageDecompressor._running_total_pairs(self._pairs)
        self.pixel_cnt = self.running_pairs[-1][1] + 1  # +1 because running pair indices are 0 based

    @staticmethod
    def _derive_pairs(img_str):
        parts = img_str.split()
        width = int(parts[0])
        nums = [int(n) for n in parts[1:]]
        pairs = [[nums[i], nums[i + 1]] for i in range(0, len(nums), 2)]
        return width, pairs

    @staticmethod
    def _running_total_pairs(pairs):
        new_pairs = []
        for (i, (px, cnt)) in enumerate(pairs):
            if i == 0:
                new_pairs.append((px, cnt - 1))
            else:
                pair = (px, cnt + new_pairs[i - 1][1])
                new_pairs.append(pair)
        return new_pairs

    def pixel_at_idx(self, idx):
        for px, px_boundary in self.running_pairs:
            if idx <= px_boundary:
                return px
        # raise AssertionError('Control should not reach here -- %s' % locals())

    def gen_img(self):
        counter, max_cnt = 0, 10000
        buf = []
        for i in range(self.pixel_cnt):
            px = self.pixel_at_idx(i)
            neighbours = self._neighbouring_pixels(i)
            new_px = max(abs(px - n) for n in neighbours)
            buf.append(new_px)
            counter += 1

            if counter == max_cnt:
                # print('Filled buffer, returning back')
                counter = 0
                yield buf
                buf = []

        yield buf

    def _neighbouring_pixels(self, idx):
        p_cnt = self.pixel_cnt
        w = self.width
        left_idx = None if (idx % w == 0) else (idx - 1)
        top_left_idx = None if (idx < w or idx % w == 0) else (idx - w - 1)
        top_idx = None if (idx < w) else (idx - w)
        top_right_idx = None if (idx < w or idx % w == w - 1) else (idx - w + 1)
        right_idx = None if (idx % w == w - 1) else (idx + 1)
        bottom_right_idx = None if (idx + w >= p_cnt or idx % w == w - 1) else (idx + w + 1)
        bottom_idx = None if (idx + w >= p_cnt) else (idx + w)
        bottom_left_idx = None if (idx + w >= p_cnt or idx % w == 0) else (idx + w - 1)
        all_points = [left_idx, top_left_idx, top_idx, top_right_idx, right_idx,
                      bottom_right_idx, bottom_idx, bottom_left_idx]
        pixels = [self.pixel_at_idx(i) for i in all_points if i is not None]
        return pixels


class ImageCompressor(object):

    def __init__(self, img_width):
        self._pairs = []
        self._pixel = None
        self._count = 0
        self._width = img_width

    def update(self, pixel_row):
        if self._pixel is None:
            self._pixel = pixel_row[0]

        for p in pixel_row:
            if p == self._pixel:
                self._count += 1
            else:
                self._pairs.append((self._pixel, self._count))
                self._pixel = p  # update the pixel value
                self._count = 1  # reset the count

    def finish(self):
        self._pairs.append((self._pixel, self._count))

    def __str__(self):
        gen = ('%s %s' % (p, c) for (p, c) in self._pairs)
        pair_repr = ' '.join(gen)
        return '%s %s' % (self._width, pair_repr)


def edge_detection(img_str):
    print('Start edge detection', datetime.now())
    de_comp = ImageDecompressor(img_str)
    comp = ImageCompressor(de_comp.width)
    for buf in de_comp.gen_img():
        comp.update(buf)
    comp.finish()
    print('Finished edge detection at', datetime.now())
    return str(comp)


if __name__ == '__main__':
    s = '10 35 5000000 200 5000000'
    # s = '10 35 500000000 200 500000000'
    # s = '500000000 35 500000000'
    # s = '7 15 4 100 15 25 2 175 2 25 5 175 2 25 5'
    print(edge_detection(s))
    # '7 85 5 0 2 85 5 75 10 150 2 75 3 0 2 150 2 0 4' expected
    # '7 85 5 0 2 85 5 75 10 150 2 75 3 0 2 150 2 0 4
