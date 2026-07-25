# 프롬프트 매니저 (Prompt Manager)

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 프로그램입니다.

## 실행 방법

```bash
python3 main.py
```

(Python 3.10 이상 필요. 예: `python3.12 main.py`)

## 메뉴 및 담당 함수

| 번호 | 메뉴 | 담당 함수 | 구현 상태 |
|---|---|---|---|
| 1 | 프롬프트 추가 | `add_prompt()` | 완료 |
| 2 | 프롬프트 목록 보기 | `show_list()` | 완료 |
| 3 | 카테고리별 조회 | `show_by_category()` | 예정 |
| 4 | 프롬프트 검색 | `search_prompt()` | 예정 |
| 5 | 프롬프트 상세 보기 | `show_detail()` | 예정 |
| 6 | 즐겨찾기 추가/해제 | `toggle_favorite()` | 예정 |
| 7 | 즐겨찾기 목록 보기 | `show_favorites()` | 예정 |
| 0 | 종료 | - | 완료 |

그 외:
- `show_menu()` — 메뉴 화면 출력
- `choose_category()` — 프롬프트 추가 시 카테고리 선택/직접입력 처리
- `main()` — 전체 프로그램의 진입점 (메뉴 반복 출력 + 입력 분기)
