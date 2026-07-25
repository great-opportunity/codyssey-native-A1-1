"""프롬프트 매니저 - 콘솔 기반 프롬프트 관리 프로그램"""

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


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n===== 프롬프트 매니저 =====")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/해제")
    print("7. 즐겨찾기 목록 보기")
    print("0. 종료")
    print("===========================")


def add_prompt():
    print("[준비 중] 프롬프트 추가 기능은 다음 커밋에서 구현됩니다.")


def show_list():
    print("[준비 중] 프롬프트 목록 보기 기능은 다음 커밋에서 구현됩니다.")


def show_by_category():
    print("[준비 중] 카테고리별 조회 기능은 다음 커밋에서 구현됩니다.")


def search_prompt():
    print("[준비 중] 프롬프트 검색 기능은 다음 커밋에서 구현됩니다.")


def show_detail():
    print("[준비 중] 프롬프트 상세 보기 기능은 다음 커밋에서 구현됩니다.")


def toggle_favorite():
    print("[준비 중] 즐겨찾기 추가/해제 기능은 다음 커밋에서 구현됩니다.")


def show_favorites():
    print("[준비 중] 즐겨찾기 목록 보기 기능은 다음 커밋에서 구현됩니다.")


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
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
