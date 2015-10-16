import md5
from bs4 import BeautifulSoup


class Point(object):
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)


class Maze(object):
    maze = None
    maze_len = None
    start = None
    stop = None

    def __init__(self, maze, start, stop):
        self.maze = maze
        self.maze_len = len(maze)
        self.start = start
        self.stop = stop

    def maze_to_str(self):
        return '\n'.join(map(lambda x: repr(x), self.maze))

    def __repr__(self):
        return u'start: %r\nstop: %r\nmaze:\n%s\n' % (
            self.start, self.stop, self.maze_to_str())

    def is_stop(self, x, y):
        return self.stop.x == x and self.stop.y == y

    def is_visited(self, x, y):
        return self.maze[x][y] is None

    def mark_as_visited(self, x, y):
        self.maze[x][y] = None

    def is_on_maze(self, x, y):
        return (x >= 0 and x < self.maze_len and
                y >= 0 and y < len(self.maze[x]))

    def can_move(self, x, y):
        return (self.is_on_maze(x, y) and
                not self.is_visited(x, y) and
                self.maze[x][y])


MOVES = ((-1, 0, 'L'),
         (1, 0, 'R'),
         (0, -1, 'T'),
         (0, 1, 'B'))


class MazeSolver(object):
    maze_path = None

    def __init__(self, maze_path):
        self.maze_path = maze_path

    def load_maze_html(self):
        fd = open(self.maze_path, 'r')
        return fd.read()

    def parse_maze(self, html):
        soap = BeautifulSoup(html, 'lxml')
        maze_svg = soap.find('svg')
        rects = maze_svg.findAll('rect')

        maze_arr = []
        start = None
        stop = None

        def set_maze(x, y, walkable):
            to_create = x + 1 - len(maze_arr)
            if to_create > 0:
                for i in range(to_create):
                    maze_arr.append([])
            col = maze_arr[x]
            col.insert(y, walkable)

        for rect in rects:
            x = int(rect.attrs['x']) / int(rect.attrs['width'])
            y = int(rect.attrs['y']) / int(rect.attrs['height'])
            fill = rect.attrs['fill']
            if fill == 'green':
                start = Point(x, y)
                set_maze(x, y, True)
            elif fill == 'red':
                stop = Point(x, y)
                set_maze(x, y, True)
            elif fill == 'white':
                set_maze(x, y, True)
            elif fill == 'black':
                set_maze(x, y, False)
            else:
                raise RuntimeError('malformed maze')
        maze = Maze(maze_arr, start, stop)
        return maze

    def rec_solve(self, maze, x, y, acc=''):
        if maze.is_stop(x, y):
            return acc
        else:
            maze.mark_as_visited(x, y)
            for xd, yd, move in MOVES:
                x1 = x + xd
                y1 = y + yd
                if maze.can_move(x1, y1):
                    # print x, y, x1, y1, acc + move
                    result = self.rec_solve(maze, x1, y1, acc + move)
                    if result:
                        return result

    def solve(self):
        html = self.load_maze_html()
        maze = self.parse_maze(html)
        print 'Solution to the maze:'
        solution = self.rec_solve(maze, maze.start.x, maze.start.y)
        print solution
        print 'and the md5sum of it:'
        md5solution = md5.new(solution).hexdigest()
        print 'http://46.101.159.170/0SQJHQ1G/amaze/solve/%s' % (md5solution,)
