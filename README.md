# 프롬프트 매니저 (Prompt Manager)

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 프로그램입니다.

## 실행 방법

```bash
python3 main.py
```

(Python 3.10 이상 필요. 예: `python3.12 main.py`)

## 메뉴 및 담당 함수

| 번호 | 메뉴 | 담당 함수 |
|---|---|---|
| 1 | 프롬프트 목록 보기 | `show_list()` |
| 2 | 카테고리별 조회 | `show_by_category()` |
| 3 | 프롬프트 상세 보기 | `show_detail()` |
| 4 | 프롬프트 추가 | `add_prompt()` |
| 5 | 프롬프트 수정 (보너스) | `edit_prompt()` |
| 6 | 프롬프트 삭제 (보너스) | `delete_prompt()` |
| 7 | 프롬프트 검색 | `search_prompt()` |
| 8 | 즐겨찾기 목록 보기 | `show_favorites()` |
| 9 | 즐겨찾기 추가/해제 | `toggle_favorite()` |
| 10 | 조회수 Top 목록 (보너스) | `show_top_viewed()` |
| 11 | 프롬프트 JSON으로 저장 (보너스) | `save_to_json()` |
| 12 | JSON에서 프롬프트 불러오기 (보너스) | `load_from_json()` |
| 13 | 카테고리별 Markdown으로 내보내기 (보너스) | `export_to_markdown()` |
| 0 | 종료 | - |

그 외:
- `show_menu()` — 메뉴 화면 출력 (박스 테두리 + 그룹별 구분)
- `choose_category()` — 카테고리 선택/직접입력 처리 (추가·카테고리별 조회에서 공용으로 사용)
- `input_prefilled()` — 수정 시 기존 값을 입력창에 미리 채워주는 헬퍼 (readline 기반, 미지원 환경은 자동 대체)
- `main()` — 전체 프로그램의 진입점 (메뉴 반복 출력 + 입력 분기)
