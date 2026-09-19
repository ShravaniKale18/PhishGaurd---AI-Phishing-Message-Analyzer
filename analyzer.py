import re
import math
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "verify",
    "login",
    "signin",
    "account",
    "password",
    "otp",
    "urgent",
    "suspended",
    "blocked",
    "click",
    "confirm",
    "security",
    "update",
    "payment",
    "refund",
    "winner",
    "prize"
]


def analyze_url(url):

    """Analyze a URL for common suspicious characteristics"""

    score = 0
    indicators = []

    try:
        parsed = urlparse(url)

        if not parsed.netloc:
            return {
                "score" : 0,
                "indicators" : ["Invalid URL"]
            }
    except Exception:
        return {
            "score" : 0,
            "indicators" : ["Invalid URL"]
        }

    domain = parsed.netloc.lower()


    if parsed.scheme != 'https':
        score += 15
        indicators.append("URL does not use HTTPS")

    if re.match(r"^\d{1,3}(\.\d{1,3}){3}", domain):
        score += 25
        indicators.append("URL uses an IP address instead of domain")

    if len(url) > 100:
        score += 10
        indicators.append("Unusually long URL")

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in url.lower():
            found_keywords.append(keyword)

    if found_keywords:
        score += min(len(found_keywords) * 5, 20)
        indicators.append(
            f"Suspicious keywords: {', '.join(found_keywords)}"
        )

    if domain.count(".") >= 3:
        score += 15
        indicators.append("Unusually many subdomains")

    if "@" in url:
        score += 20
        indicators.append("URL contains '@' which can hide the real destination")

    score = min(score, 100)

    return {
        "score" : score,
        "indicators" : indicators
    }


def analyze_message(message):
    """Analyze text for common phishing/social-engineering indicators."""

    score = 0
    indicators = []

    text = message.lower()

    urgency_keywords = [
        "urgent",
        "immediately",
        "act now",
        "within 24 hours",
        "last chance",
        "right now",
    ]

    threat_words = [
        "account suspended",
        "account blocked",
        "account will be closed",
        "legal action",
        "access revoked",
    ]


    credential_words = [
        "password",
        "username",
        "login",
        "verify your account",
        "credentials",
    ]

    payment_words = [
        "payment",
        "bank",
        "credit card",
        "debit card",
        "upi",
        "refund",
    ]


    if any(word in text for word in urgency_keywords):
        score += 20
        indicators.append("Urgency/Pressure detected")

    if any(word in text for word in threat_words):
        score += 20
        indicators.append("Account threat detected")

    if any(word in text for word in credential_words):
        score += 20
        indicators.append("Possible credential request")

    if "otp" in text or "one time password" in text:
        score += 20
        indicators.append("OTP request detected")

    if any(word in text for word in payment_words):
        score += 10
        indicators.append("Financial information/request detected")

    # Check for the external link in the message

    if re.search(r"https?://\S+", message):
        score += 10
        indicators.append("External link detected")

    score = min(score, 100)

    return {
        "score" : score,
        "indicators" : indicators
    }

def get_risk_level(score):
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"