import streamlit as st
import random
import streamlit as st

st.set_page_config(page_title="MBTI 학습 성향 분석기", page_icon="📘")

st.title("📘 MBTI 기반 학습 성향 분석기")
st.write("12가지 질문에 답하고, 당신의 MBTI에 맞는 학습 성향과 공부 팁을 알아보세요!")

questions = [
    ("다른 사람들과 함께 있을 때 에너지가 생긴다", "혼자 있을 때 에너지가 충전된다", "E", "I"),
    ("여럿이 떠드는 분위기가 즐겁다", "조용한 대화나 혼자 있는 것이 편하다", "E", "I"),
    ("즉흥적으로 활동 계획을 세운다", "충분히 혼자 생각한 후 계획한다", "E", "I"),

    ("사실과 현실 중심으로 정보를 받아들인다", "직관이나 영감으로 의미를 파악한다", "S", "N"),
    ("경험을 중시하고 구체적인 예시를 좋아한다", "추상적인 개념과 가능성을 좋아한다", "S", "N"),
    ("실용적이고 눈에 보이는 결과를 선호한다", "새로운 아이디어나 이론적 토론이 좋다", "S", "N"),

    ("객관적 사실과 논리를 우선시한다", "사람의 감정이나 상황을 고려한다", "T", "F"),
    ("갈등보다 사실을 바로잡는 것이 중요하다", "분위기와 감정 조율이 중요하다", "T", "F"),
    ("비판적 사고로 문제를 해결한다", "공감과 이해로 문제를 해결한다", "T", "F"),

    ("계획적으로 일정을 세워 실천한다", "상황에 따라 융통성 있게 움직인다", "J", "P"),
    ("마감일 전 미리미리 끝내는 편이다", "마감이 다가와야 집중이 된다", "J", "P"),
    ("정리되고 예측 가능한 생활이 좋다", "즉흥적이고 자유로운 게 편하다", "J", "P"),
]

mbti_scores = {k: 0 for k in "EISNTFJP"}

# 질문 표시
for i, (opt1, opt2, type1, type2) in enumerate(questions):
    choice = st.radio(f"{i+1}.", [opt1, opt2], key=f"q{i}")
    mbti_scores[type1 if choice == opt1 else type2] += 1

# 결과 확인
if st.button("📊 결과 확인하기"):
    mbti = (
        ("E" if mbti_scores["E"] >= 2 else "I") +
        ("S" if mbti_scores["S"] >= 2 else "N") +
        ("T" if mbti_scores["T"] >= 2 else "F") +
        ("J" if mbti_scores["J"] >= 2 else "P")
    )

    st.subheader(f"🧬 당신의 MBTI 유형은 **{mbti}**입니다!")

    # 전체 16유형 학습 성향 데이터
    from textwrap import dedent

    learning_data = {
        "INTJ": {
            "style": "독립적이며 구조화된 사고를 통해 문제 해결을 선호합니다.",
            "env": "조용하고 분석적인 분위기, 방해받지 않는 공간",
            "strategies": [
                "계획 세우고 주간 단위로 체크하기",
                "마인드맵을 활용해 전체 흐름 파악",
                "복잡한 개념은 직접 요약 정리"
            ],
            "tips": [
                "복습 루틴을 명확히 설정하세요",
                "자료를 분석적으로 비교하세요",
                "학습 목표를 시각적으로 정리하세요"
            ]
        },
        "INTP": {
            "style": "이론 중심 학습을 선호하며 탐구심이 강하고 토론을 즐깁니다.",
            "env": "비형식적이고 유연한 분위기, 고요한 환경",
            "strategies": [
                "추상 개념을 그림이나 도식으로 표현",
                "호기심 생긴 주제는 깊게 파고들기",
                "혼잣말로 설명하며 정리"
            ],
            "tips": [
                "메모앱 활용한 즉흥 정리 습관화",
                "의문이 생긴 건 즉시 검색해보기",
                "혼자 설명해보며 복습하세요"
            ]
        },
        "ENTJ": {
            "style": "목표 지향적이며 효율적인 학습을 추구합니다.",
            "env": "계획 중심 환경, 경쟁과 도전이 있는 과제",
            "strategies": [
                "일정표 만들고 달성률 추적",
                "중요도별 우선순위 학습",
                "타이머 이용한 집중 블록 학습"
            ],
            "tips": [
                "과제를 작은 단위로 나누어 즉시 실행",
                "정기적인 자기 점검 루틴 만들기",
                "결과 위주의 피드백 적극 반영"
            ]
        },
        "ENTP": {
            "style": "다양한 자극과 아이디어 교환을 통해 흥미를 느낍니다.",
            "env": "열린 토론 분위기, 유동적인 스케줄",
            "strategies": [
                "친구와 아이디어 브레인스토밍",
                "다양한 매체(영상, 팟캐스트) 활용",
                "개념 간 연결 관계 정리"
            ],
            "tips": [
                "학습을 프로젝트처럼 기획해보기",
                "경쟁하거나 발표할 기회 만들기",
                "기억보다 창의적 연결에 초점 맞추기"
            ]
        },
        "INFJ": {
            "style": "깊이 있고 의미 있는 학습을 선호합니다.",
            "env": "조용하고 따뜻한 분위기, 사색적 공간",
            "strategies": [
                "감정이입이 가능한 예시 사용",
                "글쓰기나 일기로 개념 정리",
                "장기적 목표 설정 후 거꾸로 계획"
            ],
            "tips": [
                "스스로에게 질문하며 학습하기",
                "비판적 사고보단 공감적 분석 시도",
                "자료를 감정과 연결해 기억하기"
            ]
        },
        "INFP": {
            "style": "창의적이고 자기표현이 허용되는 학습에 흥미를 느낍니다.",
            "env": "감성적인 공간, 자기만의 루틴 유지 가능",
            "strategies": [
                "의미 있는 사례나 문장 메모",
                "글쓰기나 스토리 기반 학습",
                "느낀 점 중심의 요약"
            ],
            "tips": [
                "감성적인 색이나 음악 활용",
                "명언이나 문장으로 동기부여",
                "나만의 노트 디자인 만들기"
            ]
        },
        "ENFJ": {
            "style": "사람들과 함께 나누고 설명하며 배웁니다.",
            "env": "협력적인 분위기, 상호작용 중심 환경",
            "strategies": [
                "스터디 그룹에서 요약 담당",
                "다른 사람에게 설명하며 복습",
                "공감 기반으로 이해 확장"
            ],
            "tips": [
                "누군가를 도와주며 학습하기",
                "감정을 나누는 노트 활용",
                "긍정 피드백을 학습 보상으로 삼기"
            ]
        },
        "ENFP": {
            "style": "다양성과 재미가 있는 활동에서 에너지를 얻습니다.",
            "env": "새로운 자극 많은 공간, 자율성 보장",
            "strategies": [
                "학습 목표를 시각적으로 표현",
                "다양한 포맷으로 자료 정리",
                "창의적 방법으로 자기 표현"
            ],
            "tips": [
                "색상, 도형 등 시각적 자극 활용",
                "자기만의 발표 콘텐츠 만들기",
                "즉흥적 아이디어를 메모하기"
            ]
        },
        "ISTJ": {
            "style": "체계적이고 규칙적인 학습을 선호합니다.",
            "env": "정돈된 환경, 반복 가능한 구조",
            "strategies": [
                "계획표와 점검표 만들기",
                "반복 암기 및 요약 노트 활용",
                "문제집 정리하며 실수 유형 분석"
            ],
            "tips": [
                "매일 같은 시간에 학습 루틴 만들기",
                "성취도 기록하기",
                "체크리스트로 완료 표시"
            ]
        },
        "ISFJ": {
            "style": "현실적이고 실용적인 방식으로 정보를 습득합니다.",
            "env": "조용하고 따뜻한 분위기, 정해진 학습 시간",
            "strategies": [
                "사례 중심으로 개념 정리",
                "친숙한 방식으로 반복 학습",
                "요약 → 암기 → 복습 순서 지키기"
            ],
            "tips": [
                "색깔펜 등 익숙한 도구 활용",
                "기록 남기며 정리하는 습관 들이기",
                "작은 목표로 자신감 확보"
            ]
        },
        "ESTJ": {
            "style": "실행 중심으로 결과를 중요시하며 계획적으로 학습합니다.",
            "env": "규칙과 기준이 명확한 환경, 타인과 비교 가능성 있는 구조",
            "strategies": [
                "성과 기반 점수표 만들기",
                "경쟁 요소 있는 활동 활용",
                "규칙적인 복습 계획 수립"
            ],
            "tips": [
                "정해진 시간 내 미션식 공부",
                "다른 사람과 비교하며 점검",
                "순서대로 정리된 자료 사용"
            ]
        },
        "ESFJ": {
            "style": "사람들과 협력하며 따뜻한 환경에서 잘 학습합니다.",
            "env": "공감 중심, 함께하는 활동이 많은 환경",
            "strategies": [
                "질문 주고받기 중심 스터디",
                "요약 후 발표하는 활동",
                "다른 사람 도우며 복습"
            ],
            "tips": [
                "공부한 내용을 이야기처럼 나누기",
                "누군가에게 설명할 기회 만들기",
                "감정 기반 피드백 주고받기"
            ]
        },
        "ISTP": {
            "style": "혼자서 문제를 해결하며 배우는 것을 좋아합니다.",
            "env": "실용 중심, 도전과제가 있는 환경",
            "strategies": [
                "문제풀이로 개념 익히기",
                "혼자 스스로 이해하고 요약",
                "시도 → 실패 → 수정 루틴"
            ],
            "tips": [
                "도전과제로 게임처럼 공부",
                "배운 걸 응용해보기",
                "반복 실습형 학습 선택"
            ]
        },
        "ISFP": {
            "style": "감각적이고 조용한 환경에서 창의적으로 학습합니다.",
            "env": "아늑하고 편안한 공간, 자율적인 분위기",
            "strategies": [
                "예시와 그림 활용해 개념 연결",
                "조용히 노트 정리",
                "실생활 사례와 연결하기"
            ],
            "tips": [
                "노트에 직접 그려보기",
                "배경 음악과 함께 공부",
                "시각 자료로 학습 흐름 표현"
            ]
        },
        "ESTP": {
            "style": "활동적이고 도전적인 상황에서 배움이 활발합니다.",
            "env": "다이나믹한 환경, 즉각적인 피드백이 있는 구조",
            "strategies": [
                "문제풀이나 퀴즈 활용",
                "직접 몸으로 실습하기",
                "실시간 경쟁 게임 방식"
            ],
            "tips": [
                "즉각적 보상을 활용한 학습",
                "성취를 눈으로 확인할 수 있게 정리",
                "한계 시간 정하고 몰입"
            ]
        },
        "ESFP": {
            "style": "재미와 감각적 요소가 있는 학습을 선호합니다.",
            "env": "밝고 생동감 있는 분위기, 사람과 함께",
            "strategies": [
                "연극, 역할극 활용 학습",
                "노래나 리듬 학습법 사용",
                "실제 경험과 연계된 활동"
            ],
            "tips": [
                "학습 내용을 몸으로 표현하기",
                "즐거운 보상과 함께 공부",
                "친구와 함께 퀴즈 게임"
            ]
        }
    }

    profile = learning_data.get(mbti)
    if profile:
        st.markdown("---")
        st.subheader("🧠 당신의 학습 성향 분석")
        st.markdown(f"**학습 스타일:** {profile['style']}")
        st.markdown(f"**잘 맞는 환경:** {profile['env']}")
        st.markdown("**📌 효과적인 학습 전략:**")
        for s in profile["strategies"]:
            st.markdown(f"- {s}")
        st.markdown("**✅ 공부 능률을 높이는 팁:**")
        for t in profile["tips"]:
            st.markdown(f"- {t}")
    else:
        st.warning("MBTI 정보가 누락되었습니다.")


