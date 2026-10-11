# 개미 규칙 RL — 튜밋 격자

> Generalized Langton's ant (turmite) rule RL, drawn as ASCII. Zero dependencies.

**2026-10-12** · daily-lab day project

## 뭐 하는 건가

규칙은 L 과 R 로 된 문자열 하나가 전부다. 그런데 "LR" 은 만 보쯤에서 갑자기 고속도로를 놓기 시작하고, 색이 셋 이상이면 삼각형이나 나선 같은 구조가 나온다. 어느 규칙이 무엇을 그릴지는 돌려 보기 전에는 아무도 모른다 — 그래서 120000보를 돌린다.

## 어떻게 만들어졌나

모델을 쓸 수 없을 때 도는 오프라인 생성기가 만들었다. 파라미터는 날짜에서 결정론적으로 뽑힌다 — 규칙 RL · 120000보 · 폭 121.

## 실행

```bash
python3 main.py RL 120000 121
```

## 파일

- `main.py`

---

매일 하나씩 만드는 [daily-lab](https://github.com/456rtyfgh/daily-lab)에서 자동 생성됐다.
