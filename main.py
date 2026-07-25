"""프롬프트 매니저 - 콘솔 기반 프롬프트 관리 프로그램"""

import textwrap

# 프롬프트가 속할 수 있는 카테고리 목록 (프롬프트 추가 시 이 목록에서 고르거나 직접 입력 가능)
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 프로그램 시작 시 기본으로 등록되는 프롬프트 데이터 (리스트 안에 딕셔너리)
# 각 프롬프트는 title, content, category, favorite 네 가지 정보를 가진다.
prompts = [
    {
        "title": "베트남 한국어 학습자용 문법 블로그 글 작성",
        "content": (
            "너는 베트남인 한국어 학습자를 위한 블로그의 전문 필진이야. 20대 한국어 강사로서 "
            "문법 지식이 정확하고, 베트남어로 유창하게 글을 쓸 수 있어. 트렌디하고 활발한 스타일로 "
            "독자가 끝까지 재미있게 읽을 수 있는 글을 써.\n\n"
            "[목표]\n"
            "사용자가 문법 주제를 주면, 베트남인 한국어 학습자가 읽는 블로그 글 한 편을 완성해서 줘. "
            "문법 주제의 난이도에 맞게 독자 수준(입문/중고급)을 자동으로 판단해서 써.\n\n"
            "[출력 형식]\n"
            "1. 훅으로 시작 (1~2문장, 공감형 상황 묘사)\n"
            "2. 베트남어 메인 + 한국어 번역 병기\n"
            "3. 문법 규칙은 기본형/격식체/반말 3단계로 소제목과 함께 제시\n"
            "4. 대화형 예문 (로마자 발음 병기, 유머 포인트 최소 1개 포함)\n"
            "5. 연습문제 제공\n"
            "6. 교재체 말투, 어려운 문법 용어, 단조로운 예문 반복 금지\n\n"
            "[SEO 규칙]\n"
            "- title: '베트남어로 배우는 한국어 + 문법 주제' 형식\n"
            "- meta description 150자 이내 핵심 요약\n"
            "- 본문 첫 문단에 핵심 키워드 자연스럽게 포함\n\n"
            "[안전장치 / 사실 처리 규칙]\n"
            "- 베트남어 표현이 확실하지 않으면 '(베트남어 표현 확인 필요)'라고 명시\n"
            "- 문법 규칙은 표준 한국어 문법 기준, 불규칙 활용은 정확히 반영\n"
            "- 확신할 수 없는 문법 사항은 단정하지 말고 '확인 필요'로 표기\n"
            "- 문법 주제가 너무 모호하면 글 쓰기 전에 확인 질문 먼저\n\n"
            "[출력 순서]\n"
            "STEP 1: 베트남어 HTML 전문 출력\n"
            "--- 구분선 ---\n"
            "STEP 2: 운영자 검토용 한국어 plain text 재작성 (발행 안 함)"
        ),
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "제품 상세페이지 배경 제거 이미지 생성",
        "content": (
            "product photo of {제품명}, centered composition, soft studio lighting, "
            "pure white background, high resolution, e-commerce catalog style, "
            "no shadows, no text, no watermark --ar 1:1"
        ),
        "category": "이미지 생성",
        "favorite": True,
    },
    {
        "title": "친절한 IT 헬프데스크 상담원 페르소나",
        "content": (
            "너는 5년 차 IT 헬프데스크 상담원 '지우'야. 항상 친절하고 차분한 말투를 쓰고, "
            "전문 용어를 쓸 때는 바로 쉬운 말로 풀어서 설명해줘. 사용자가 감정적으로 화가 나있어도 "
            "먼저 공감한 뒤 해결책을 단계별로 안내해. 모르는 내용은 추측하지 말고 '확인 후 안내드리겠습니다'라고 답해."
        ),
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "노코드 자동화 시나리오 설계 도우미",
        "content": (
            "너는 Make(구 Integromat)/Zapier 자동화 설계 전문가야. 내가 자동화하고 싶은 업무를 설명하면, "
            "① 트리거(Trigger) ② 중간 처리 단계(Filter/Transform) ③ 최종 액션(Action) 순서로 "
            "시나리오를 표로 정리해줘. 각 단계에 필요한 앱/모듈 이름과 설정값 예시도 함께 제시해."
        ),
        "category": "자동화",
        "favorite": False,
    },
]


# ===== 화면 출력 도우미 (ANSI 색상 / 구분선 / 줄바꿈) =====
# 외부 라이브러리 없이, 터미널이 인식하는 ANSI 이스케이프 코드 문자열만 사용한다.

LINE_WIDTH = 44

COLOR_RESET = "\033[0m"
COLOR_TITLE = "\033[1;36m"   # 굵은 청록색 - 메뉴/섹션 제목
COLOR_CATEGORY = "\033[33m"  # 노란색 - 카테고리 태그
COLOR_STAR = "\033[33m"      # 노란색 - 즐겨찾기 별
COLOR_ERROR = "\033[31m"     # 빨간색 - 오류/결과 없음 안내
COLOR_SUCCESS = "\033[32m"   # 초록색 - 성공 안내


def print_divider():
    """일관된 길이의 구분선을 출력한다."""
    print(COLOR_TITLE + "=" * LINE_WIDTH + COLOR_RESET)


def print_section(title):
    """섹션(목록/검색결과 등) 제목을 색상과 함께 출력한다."""
    print(f"\n{COLOR_TITLE}--- {title} ---{COLOR_RESET}")


def print_error(message):
    """오류/결과 없음 안내 메시지를 빨간색으로 출력한다."""
    print(f"{COLOR_ERROR}{message}{COLOR_RESET}")


def print_success(message):
    """성공 안내 메시지를 초록색으로 출력한다."""
    print(f"{COLOR_SUCCESS}{message}{COLOR_RESET}")


def print_wrapped(text, width=LINE_WIDTH + 26):
    """긴 텍스트를 원래 줄바꿈(문단 구분)은 유지하면서, 각 줄만 터미널 폭에 맞게 접어서 출력한다."""
    for line in text.split("\n"):
        if line.strip() == "":
            print()
        else:
            print(textwrap.fill(line, width=width))


def format_item(number, prompt, show_category=True):
    """목록에 쓰이는 '번호. [카테고리] 제목 ⭐' 한 줄을 만든다."""
    category_tag = f"{COLOR_CATEGORY}[{prompt['category']}]{COLOR_RESET} " if show_category else ""
    star = f"{COLOR_STAR}⭐{COLOR_RESET}" if prompt["favorite"] else ""
    return f"{number}. {category_tag}{prompt['title']} {star}"


# ===== 전체 구조 (메뉴 화면 + 진입점) =====

def show_menu():
    """메인 메뉴를 출력한다."""
    print()
    print_divider()
    print(f"{COLOR_TITLE}프롬프트 매니저{COLOR_RESET}")
    print_divider()
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    print_divider()


def main():
    """프로그램의 진입점. 메뉴를 반복 출력하며 사용자 입력을 처리한다."""
    while True:
        show_menu()
        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print_success("프로그램을 종료합니다.")
            break
        else:
            print_error("잘못된 번호입니다. 다시 입력해주세요.")


# ===== 세부 기능 함수 =====

def choose_category():
    """카테고리 목록을 보여주고, 번호 선택 또는 직접 입력 중 하나로 카테고리명을 반환한다."""
    print("카테고리를 선택하세요.")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")
    print("목록에 없으면 원하는 카테고리명을 직접 입력하세요.")

    selection = input("카테고리 번호 또는 이름: ").strip()
    while not selection:
        print_error("카테고리는 비어있을 수 없습니다. 다시 입력해주세요.")
        selection = input("카테고리 번호 또는 이름: ").strip()

    if selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(CATEGORIES):
            return CATEGORIES[index]
        print_error("목록에 없는 번호라서, 입력하신 값을 그대로 카테고리명으로 사용합니다.")
        return selection

    return selection


def add_prompt():
    """제목, 내용, 카테고리를 입력받아 새 프롬프트를 prompts 리스트에 추가한다."""
    print_section("새 프롬프트 추가")

    title = input("제목: ").strip()
    while not title:
        print_error("제목은 비어있을 수 없습니다. 다시 입력해주세요.")
        title = input("제목: ").strip()

    content = input("내용: ").strip()
    while not content:
        print_error("내용은 비어있을 수 없습니다. 다시 입력해주세요.")
        content = input("내용: ").strip()

    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print_success(f"\n'{title}' 프롬프트가 추가되었습니다. (카테고리: {category})")


def show_list():
    """저장된 모든 프롬프트를 번호, 제목, 카테고리, 즐겨찾기 여부와 함께 출력한다."""
    if not prompts:
        print_error("등록된 프롬프트가 없습니다.")
        return

    print_section("프롬프트 목록")
    for i, prompt in enumerate(prompts, start=1):
        print(format_item(i, prompt))


def show_by_category():
    """카테고리를 선택받아, 해당 카테고리에 속한 프롬프트만 원래 번호와 함께 출력한다."""
    category = choose_category()
    matched = [(i, p) for i, p in enumerate(prompts, start=1) if p["category"] == category]

    if not matched:
        print_error(f"'{category}' 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print_section(f"'{category}' 카테고리 프롬프트")
    for i, prompt in matched:
        print(format_item(i, prompt, show_category=False))


def search_prompt():
    """키워드를 입력받아, 제목 또는 내용에 그 키워드가 포함된 프롬프트를 원래 번호와 함께 출력한다."""
    keyword = input("검색어를 입력하세요: ").strip()
    while not keyword:
        print_error("검색어는 비어있을 수 없습니다. 다시 입력해주세요.")
        keyword = input("검색어를 입력하세요: ").strip()

    matched = [
        (i, p) for i, p in enumerate(prompts, start=1)
        if keyword.lower() in p["title"].lower() or keyword.lower() in p["content"].lower()
    ]

    if not matched:
        print_error(f"'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print_section(f"'{keyword}' 검색 결과")
    for i, prompt in matched:
        print(format_item(i, prompt))


def show_detail():
    """번호를 입력받아 해당 프롬프트의 제목, 카테고리, 즐겨찾기 여부, 내용 전체를 출력한다."""
    if not prompts:
        print_error("등록된 프롬프트가 없습니다.")
        return

    number = input("상세히 볼 프롬프트 번호: ").strip()
    index = int(number) - 1 if number.isdigit() else -1

    if not (0 <= index < len(prompts)):
        print_error("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    star = f"{COLOR_STAR}⭐ 즐겨찾기 됨{COLOR_RESET}" if prompt["favorite"] else "즐겨찾기 안 됨"

    print_section(f"{number}번 프롬프트 상세")
    print(f"{COLOR_TITLE}제목{COLOR_RESET}: {prompt['title']}")
    print(f"{COLOR_TITLE}카테고리{COLOR_RESET}: {COLOR_CATEGORY}{prompt['category']}{COLOR_RESET}")
    print(f"{COLOR_TITLE}즐겨찾기{COLOR_RESET}: {star}")
    print(f"{COLOR_TITLE}내용{COLOR_RESET}:")
    print_wrapped(prompt["content"])


def toggle_favorite():
    """번호를 입력받아 해당 프롬프트의 즐겨찾기 상태를 반전(추가 ↔ 해제)시킨다."""
    if not prompts:
        print_error("등록된 프롬프트가 없습니다.")
        return

    number = input("즐겨찾기를 변경할 프롬프트 번호: ").strip()
    index = int(number) - 1 if number.isdigit() else -1

    if not (0 <= index < len(prompts)):
        print_error("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print_success(f"'{prompt['title']}'을(를) 즐겨찾기에 추가했습니다. ⭐")
    else:
        print(f"'{prompt['title']}'을(를) 즐겨찾기에서 해제했습니다.")


def show_favorites():
    """즐겨찾기로 표시된 프롬프트만 원래 번호와 함께 모아서 출력한다."""
    matched = [(i, p) for i, p in enumerate(prompts, start=1) if p["favorite"]]

    if not matched:
        print_error("즐겨찾기한 프롬프트가 없습니다.")
        return

    print_section("즐겨찾기 목록")
    for i, prompt in matched:
        print(format_item(i, prompt))


if __name__ == "__main__":
    main()
