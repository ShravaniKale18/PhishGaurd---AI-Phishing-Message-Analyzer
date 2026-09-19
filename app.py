import streamlit as st

from analyzer import (
    analyze_url,
    analyze_message,
    get_risk_level
)

from llm_analyzer import analyze_with_llm


# PAGE CONFIG

st.set_page_config(
    page_title="PhishGuard | AI Phishing Analyzer",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background: #0b1120;
    color: #e5e7eb;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- HEADER ---------- */

.hero {
    padding: 30px 35px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #111827 0%,
        #172554 100%
    );
    border: 1px solid #263653;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 17px;
    color: #94a3b8;
}

.shield {
    font-size: 45px;
}


/* ---------- SECTION HEADINGS ---------- */

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 25px;
    margin-bottom: 12px;
}


/* ---------- INPUT CARD ---------- */

.input-card {
    background: #111827;
    border: 1px solid #263653;
    border-radius: 16px;
    padding: 22px;
    margin-top: 10px;
}


/* ---------- RESULT CARDS ---------- */

.metric-card {
    background: #111827;
    border: 1px solid #263653;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    min-height: 130px;
}

.metric-title {
    font-size: 14px;
    color: #94a3b8;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
}


/* ---------- RISK BADGES ---------- */

.risk-high {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: #451a1a;
    color: #fca5a5;
    font-weight: 700;
}

.risk-medium {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: #422006;
    color: #fdba74;
    font-weight: 700;
}

.risk-low {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: #052e1b;
    color: #86efac;
    font-weight: 700;
}


/* ---------- INFO BOX ---------- */

.info-card {
    background: #0f172a;
    border: 1px solid #263653;
    border-radius: 14px;
    padding: 18px;
    margin-top: 15px;
}

.info-title {
    font-weight: 700;
    color: #e2e8f0;
}

.info-text {
    color: #94a3b8;
    font-size: 14px;
}


/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: #080d18;
    border-right: 1px solid #1e293b;
}


/* ---------- BUTTON ---------- */

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 48px;
    font-size: 16px;
    font-weight: 700;
}


/* ---------- TEXT AREA / INPUT ---------- */

textarea,
input {
    border-radius: 10px !important;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #1e293b;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:10px;">
            <div style="font-size:50px;">🛡️</div>
            <h2 style="color:white;">PhishGuard</h2>
            <p style="color:#94a3b8;">
                AI-powered phishing detection
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🔐 Detection Pipeline")

    st.markdown("""
    **01** → Input Analysis  
    **02** → Rule-Based Detection  
    **03** → Risk Scoring  
    **04** → AI Analysis  
    **05** → Security Recommendation
    """)

    st.divider()

    st.markdown("### 🧠 Detection Methods")

    st.markdown("""
    - Suspicious keywords
    - Urgency detection
    - Account threats
    - Credential requests
    - OTP requests
    - Financial requests
    - Suspicious URLs
    - URL structure analysis
    - AI-powered explanation
    """)

    st.divider()

    st.caption(
        "⚠️ PhishGuard provides a risk assessment "
        "and should not be treated as absolute proof "
        "that a message or URL is malicious."
    )


# HERO HEADER

st.markdown("""
<div class="hero">

    <div class="shield">🛡️</div>

    <div class="hero-title">
        PhishGuard
    </div>

    <div class="hero-subtitle">
        AI-Powered Phishing Message & URL Analyzer
    </div>

    <div style="
        margin-top:15px;
        color:#64748b;
        font-size:14px;
    ">
        Detect suspicious patterns, understand the risk,
        and get AI-powered security insights.
    </div>

</div>
""", unsafe_allow_html=True)


# INPUT SECTION

st.markdown(
    '<div class="section-title">🔍 What would you like to analyze?</div>',
    unsafe_allow_html=True
)

input_type = st.radio(
    "",
    ["💬 Message", "🔗 URL"],
    horizontal=True,
    label_visibility="collapsed"
)


# INPUT

st.markdown('<div class="input-card">', unsafe_allow_html=True)

if input_type == "💬 Message":

    user_input = st.text_area(
        "Suspicious Message",
        height=180,
        placeholder=(
            "Paste the suspicious message here...\n\n"
            "Example:\n"
            "URGENT! Your account has been suspended. "
            "Verify your account immediately."
        ),
        label_visibility="visible"
    )

else:

    user_input = st.text_input(
        "Suspicious URL",
        placeholder="https://example.com/login",
        label_visibility="visible"
    )

st.markdown('</div>', unsafe_allow_html=True)


# ANALYZE BUTTON

st.write("")

analyze_clicked = st.button(
    "🔍  Analyze for Phishing Risk",
    type="primary",
    use_container_width=True
)


# ANALYSIS

if analyze_clicked:

    if not user_input.strip():

        st.warning(
            "Please enter a message or URL before analyzing."
        )

    else:

        # RULE BASED ANALYSIS

        with st.spinner("Running security checks..."):

            if input_type == "🔗 URL":
                result = analyze_url(user_input)
            else:
                result = analyze_message(user_input)

        score = result["score"]
        indicators = result["indicators"]
        risk = get_risk_level(score)


        # RESULT HEADER

        st.divider()

        st.markdown(
            '<div class="section-title">📊 Security Analysis</div>',
            unsafe_allow_html=True
        )


        # METRICS

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        RISK SCORE
                    </div>

                    <div class="metric-value">
                        {score}/100
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col2:

            if risk == "HIGH":
                badge_class = "risk-high"
            elif risk == "MEDIUM":
                badge_class = "risk-medium"
            else:
                badge_class = "risk-low"

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        RISK LEVEL
                    </div>

                    <div style="margin-top:12px;">
                        <span class="{badge_class}">
                            {risk}
                        </span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col3:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-title">
                        INDICATORS FOUND
                    </div>

                    <div class="metric-value">
                        {len(indicators)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


        # =================================================
        # SCORE BAR
        # =================================================

        st.write("")

        st.progress(
            min(score / 100, 1.0),
            text=f"Risk assessment: {score}%"
        )


        # DETECTED INDICATORS

        st.markdown(
            '<div class="section-title">🔎 Detected Indicators</div>',
            unsafe_allow_html=True
        )

        if indicators:

            for indicator in indicators:

                st.markdown(
                    f"""
                    <div class="info-card">
                        <span style="color:#fbbf24;">
                            ⚠
                        </span>
                        &nbsp;
                        <span style="color:#e2e8f0;">
                            {indicator}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.success(
                "✓ No obvious phishing indicators were detected "
                "by the rule-based analyzer."
            )


        # AI ANALYSIS

        st.markdown(
            '<div class="section-title">🤖 PhishGuard AI Analysis</div>',
            unsafe_allow_html=True
        )

        with st.container():

            with st.spinner(
                "PhishGuard AI is analyzing the input..."
            ):

                try:

                    response = analyze_with_llm(
                        user_input,
                        score,
                        indicators
                    )

                    st.markdown(
                        '<div class="info-card">',
                        unsafe_allow_html=True
                    )

                    st.markdown(response)

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                except Exception as e:

                    st.error(
                        "AI analysis could not be completed."
                    )

                    st.caption(
                        f"Technical error: {e}"
                     # SAFETY RECOMMENDATI  st.markdown(
            '<div class="section-title">🛡️ Safety Reminder</div>',
            unsafe_allow_html=True
        )

        st.info(
            "Never share passwords, OTPs, banking credentials, "
            "or other sensitive information through suspicious "
            "links or messages. If a message claims to be from "
            "a bank or service, verify it through the organization's "
            "official app or website."
        )


# FOOTER

st.markdown(
    """
    <div class="footer">
        🛡️ PhishGuard &nbsp;|&nbsp;
        AI + Rule-Based Cybersecurity Analysis
        <br><br>
        Built for HackDevengers 24-Hour Hackathon
    </div>
    """,
    unsafe_allow_html=True
)