from utils import filex

from harry_beck._utils import log
from harry_beck._xml import _, render_xml
from harry_beck.map import Map

WIDTH = 500
HEIGHT = 500
PADDING = 100
PLACE_RADIUS = 8
PLACE_STROKE_WIDTH = 4
PLACE_TEXT_COLOR = 'black'
ROAD_STROKE_WIDTH = 6


def get_bbox(m):
    min_x, max_x, min_y, max_y = None, None, None, None
    for __, point in m.__places__.items():
        x, y = point
        if min_x is None:
            min_x = max_x = x
        if min_y is None:
            min_y = max_y = y
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    return min_x, max_x, min_y, max_y


def get_func_transform(m):
    min_x, max_x, min_y, max_y = get_bbox(m)
    x_span = max_x - min_x
    y_span = max_y - min_y

    def transform(point):
        x, y = point
        px = (x - min_x) / x_span
        py = (y - min_y) / y_span
        return (
            px * (WIDTH - PADDING * 2) + PADDING,
            (1 - py) * (HEIGHT - PADDING * 2) + PADDING,
        )

    return transform


def draw_map(m):
    transform = get_func_transform(m)

    def draw_road(road, places):
        road_segments = []
        x1, y1 = None, None
        for place in places:
            x2, y2 = transform(m.__places__[place])
            if x1:
                road_segments.append(
                    _(
                        'line',
                        [],
                        {
                            'x1': x1,
                            'y1': y1,
                            'x2': x2,
                            'y2': y2,
                            'stroke': 'red',
                            'stroke-width': ROAD_STROKE_WIDTH,
                        },
                    )
                )
            x1, y1 = x2, y2
        return _('g', road_segments)

    roads = list(
        map(
            lambda x: draw_road(x[0], x[1]),
            m.__roads__.items(),
        )
    )

    def draw_point(place, point):
        x, y = transform(point)
        return _(
            'g',
            [
                _(
                    'circle',
                    [],
                    {
                        'cx': x,
                        'cy': y,
                        'r': PLACE_RADIUS,
                        'fill': 'white',
                        'stroke': 'red',
                        'stroke-width': PLACE_STROKE_WIDTH,
                    },
                ),
                _(
                    'text',
                    place,
                    {
                        'x': x + PLACE_RADIUS * 1.5,
                        'y': y + PLACE_RADIUS * 0.5,
                        'fill': PLACE_TEXT_COLOR,
                        'stroke': None,
                        'text-anchor': 'start',
                    },
                ),
            ],
        )

    circles = list(
        map(
            lambda x: draw_point(x[0], x[1]),
            m.__places__.items(),
        )
    )

    svg = _(
        'svg',
        roads + circles,
        {
            'width': WIDTH,
            'height': HEIGHT,
        },
    )

    svg_file = '/tmp/harry_beck.svg'
    filex.write(svg_file, render_xml(svg))
    log.info(f'Saved {svg_file}')


if __name__ == '__main__':
    m = Map.create_example1()
    draw_map(m)
