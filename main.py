import streamlit as st
import random
import streamlit as st

st.set_page_config(page_title="MBTI 학습 성향 분석기", page_icon="📘")

st.title("📘 MBTI 기반 학습 성향 분석기")
st.write("🧠 나에게 맞는 학습 방법을 찾고 싶다면? 지금 바로 알아보세요!")

# MBTI 소개
with st.expander("📖 MBTI란 무엇인가요?"):
    st.markdown("""
MBTI는 사람의 성격을 4가지 지표로 나누어 총 16가지 유형으로 분류하는 성격 유형 검사입니다. 😊  
- **E / I** : 에너지를 외부에서 얻는가? 내부에서 얻는가?  
- **S / N** : 현실적인가? 직관적인가?  
- **T / F** : 논리적인가? 감정적인가?  
- **J / P** : 계획적인가? 즉흥적인가?

이 MBTI 성향을 바탕으로, 각자에게 **가장 잘 맞는 학습 전략과 공부 습관**을 제안해드릴게요! 📚✨
""")

# 질문 구성
questions = {
    "EI": [
        ("사람들과 함께 있을 때 에너지가 생긴다", "혼자 있을 때 에너지가 충전된다"),
        ("여러 친구들과 대화하는 걸 좋아한다", "한두 명과 깊이 있는 대화가 좋다"),
        ("즉흥적인 외출을 자주 한다", "집에서 혼자 있는 게 편하다"),
        ("여러 사람이 모인 자리가 편하다", "혼잡한 환경은 피하고 싶다"),
        ("말로 표현하는 게 자연스럽다", "글로 표현하는 게 더 편하다"),
        ("활동적인 모임이 좋다", "차분한 분위기가 좋다")
    ],
    "SN": [
        ("경험한 사실 위주로 이야기하는 걸 좋아한다", "상상이나 가능성 위주로 말하는 걸 좋아한다"),
        ("구체적인 설명을 선호한다", "추상적인 개념도 잘 이해한다"),
        ("기억은 실제 있었던 일 위주다", "머릿속으로 떠오른 상상이 많다"),
        ("지금 할 수 있는 일이 중요하다", "나중을 위한 가능성이 중요하다"),
        ("현실적인 계획을 세운다", "직관과 영감을 믿는 편이다"),
        ("문제 해결 시 경험을 참고한다", "새로운 접근법을 찾으려 한다")
    ],
    "TF": [
        ("객관적인 사실로 판단한다", "감정과 상황을 고려해 판단한다"),
        ("비판을 해도 거리낌이 없다", "비판보다 기분을 상하지 않게 하는 게 중요하다"),
        ("논리적인 것이 중요하다", "공감이 더 중요하다"),
        ("의사결정에 분석을 중시한다", "의사결정에 감정을 고려한다"),
        ("문제가 생기면 사실을 먼저 본다", "문제가 생기면 사람의 입장을 먼저 본다"),
        ("원칙이 중요하다", "사람 사이의 조화가 더 중요하다")
    ],
    "JP": [
        ("일정표대로 계획하는 걸 좋아한다", "계획 없이 즉흥적으로 움직인다"),
        ("일을 미리미리 끝내는 편이다", "마감 직전까지 미루는 편이다"),
        ("정리정돈이 잘 된 상태가 좋다", "조금 어질러져 있어도 괜찮다"),
        ("계획이 틀어지면 스트레스 받는다", "계획이 틀어져도 괜찮다"),
        ("선택을 쉽게 하고 유지하는 편이다", "선택 후에도 자주 바꾸는 편이다"),
        ("미리 준비해두는 걸 좋아한다", "필요할 때 맞춰서 준비하는 편이다")
    ]
}

mbti_scores = {k: 0 for k in "EISNTFJP"}

st.subheader("📋 MBTI 유형 테스트 시작!")
for key, pairs in questions.items():
    st.markdown(f"**{key} 문항**")
    for idx, (a, b) in enumerate(pairs):
        choice = st.radio(f"{a} / {b}", [a, b], key=f"{key}_{idx}")
        if choice == a:
            mbti_scores[key[0]] += 1
        else:
            mbti_scores[key[1]] += 1

if st.button("✅ MBTI 결과 & 학습 성향 보기"):
    mbti = ""
    mbti += "E" if mbti_scores["E"] > mbti_scores["I"] else "I"
    mbti += "S" if mbti_scores["S"] > mbti_scores["N"] else "N"
    mbti += "T" if mbti_scores["T"] > mbti_scores["F"] else "F"
    mbti += "J" if mbti_scores["J"] > mbti_scores["P"] else "P"

    st.success(f"🎯 당신의 MBTI는 **{mbti}** 입니다!")

    from mbti_learning_profiles import learning_styles
    profile = learning_styles.get(mbti)

    if profile:
        st.subheader("🧠 학습 성향 설명")
        st.write(profile["설명"])
        st.markdown("### 📌 공부 능률을 높이는 팁:")
        for tip in profile["학습 팁"]:
            st.markdown(f"- {tip}")
    else:
        st.warning("이 MBTI 유형의 분석 정보가 누락되었어요 😥")
ㅍ

