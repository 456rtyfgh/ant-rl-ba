"""Generalized Langton's ant (turmite) on a wrapping grid.

개미 한 마리가 격자 위를 걷는다. 규칙은 L/R 문자열 하나뿐이다:
현재 칸의 색을 보고 그 자리의 문자대로 돌고, 칸 색을 하나 올리고, 한 칸 전진한다.
규칙이 "LR" 이면 만 보 즈음부터 개미가 스스로 고속도로를 놓기 시작한다.
"""

import sys

TURNS = {"L": -1, "R": 1}
# 북 동 남 서
DX = (0, 1, 0, -1)
DY = (-1, 0, 1, 0)
RAMP = " .:-=+*#%@"


def run(rule, width, height, steps):
    """개미를 steps 번 걷게 하고 최종 격자를 돌려준다."""
    colors = len(rule)
    grid = [[0] * width for _ in range(height)]
    x, y, facing = width // 2, height // 2, 0

    for _ in range(steps):
        color = grid[y][x]
        facing = (facing + TURNS[rule[color]]) % 4
        grid[y][x] = (color + 1) % colors
        x = (x + DX[facing]) % width
        y = (y + DY[facing]) % height

    return grid, x, y


def render(grid, ax, ay, colors):
    lines = []
    for y, row in enumerate(grid):
        out = []
        for x, c in enumerate(row):
            if x == ax and y == ay:
                out.append("@")
            elif c == 0:
                out.append(" ")
            else:
                out.append(RAMP[1 + (c * (len(RAMP) - 2)) // max(1, colors - 1)])
        lines.append("".join(out))
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    rule = args[0].upper() if len(args) > 0 else "RL"
    try:
        steps = int(args[1]) if len(args) > 1 else 120000
        width = int(args[2]) if len(args) > 2 else 121
    except ValueError:
        print("usage: main.py [rule] [steps] [width]   e.g. main.py LR 12000 101", file=sys.stderr)
        return 1

    if not rule or any(ch not in TURNS for ch in rule):
        print("rule must be made of L and R only. Got: %s" % rule, file=sys.stderr)
        return 1
    if not 1 <= steps <= 5_000_000:
        print("steps must be from 1 to 5000000.", file=sys.stderr)
        return 1
    if not 11 <= width <= 400:
        print("width must be from 11 to 400.", file=sys.stderr)
        return 1

    height = max(11, width // 2)
    grid, ax, ay = run(rule, width, height, steps)

    painted = sum(1 for row in grid for c in row if c)
    print("rule %s  %d colors  %d steps  grid %dx%d" % (rule, len(rule), steps, width, height))
    print("-" * width)
    print(render(grid, ax, ay, len(rule)))
    print("-" * width)
    print("painted %d of %d cells (%.1f%%)" % (painted, width * height, 100.0 * painted / (width * height)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
