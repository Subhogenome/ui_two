import streamlit as st
import pandas as pd

st.set_page_config(page_title="Regulatory Intelligence Feed", layout="wide")

# -------------------------
# Mock Data
# -------------------------
data = [
    {
        "agency": "FDA",
        "region": "US",
        "date": "2025-11-22",
        "impact": "High",
        "score": 92,
        "title": "FDA issues new guidance on Clinical Oncology Drug Safety",
        "summary": "Significant update impacting post-market surveillance reporting requirements for oncology molecules.",
        "topics": ["Oncology", "Post-Market", "Drug Safety"]
    },
    {
        "agency": "EMA",
        "region": "EU",
        "date": "2025-11-20",
        "impact": "Medium",
        "score": 74,
        "title": "EMA updates GMP clause for sterile manufacturing",
        "summary": "Revision focuses on sterility validation and batch release documentation.",
        "topics": ["GMP", "Manufacturing", "Quality System"]
    },
    {
        "agency": "MHRA",
        "region": "UK",
        "date": "2025-11-19",
        "impact": "Low",
        "score": 56,
        "title": "MHRA device reporting rule refinement",
        "summary": "Minor revision in reporting timelines for medical device complaints.",
        "topics": ["Medical Device", "Safety", "Reporting"]
    },
]

# -------------------------
# UI Header
# -------------------------
st.title("📰 Regulatory Intelligence Feed")
st.subheader("Modern card-based UI mock")

# -------------------------
# Filters
# -------------------------
col1, col2, col3 = st.columns([2, 1, 1])
search = col1.text_input("🔍 Search updates...")
region_filter = col2.multiselect("🌍 Region", ["US", "EU", "UK"])
impact_filter = col3.multiselect("⚠ Impact Level", ["High", "Medium", "Low"])

filtered = []

for item in data:
    if search and search.lower() not in item["title"].lower():
        continue
    if region_filter and item["region"] not in region_filter:
        continue
    if impact_filter and item["impact"] not in impact_filter:
        continue
    filtered.append(item)

st.write("")

# -------------------------
# Card Renderer
# -------------------------
def render_card(item):
    card_html = f"""
    <div style="
        border:1px solid #ddd;
        border-radius:12px;
        padding:18px;
        margin-bottom:18px;
        background:white;
        box-shadow:0px 2px 5px rgba(0,0,0,0.05);">

        <h4 style="margin:0; font-size:18px;">{item['title']}</h4>
        <p style="color:gray; font-size:13px;">{item['date']} • {item['agency']} • {item['region']}</p>

        <p style="font-size:15px; margin-top:8px;">{item['summary']}</p>

        <div style="margin-top:10px;">
            <span style="background:#ffe5e5; padding:6px; border-radius:6px; margin-right:8px;">
                Impact: {item['impact']}
            </span>
            <span style="background:#e7f3ff; padding:6px; border-radius:6px; margin-right:8px;">
                Score: {item['score']}
            </span>
        </div>
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)

    if st.button(f"🔍 View AI Summary ({item['agency']})", key=item['title']):
        st.success("AI Summary: Placeholder text summarizing impact and compliance context.")


# Render cards
if not filtered:
    st.warning("No results found. Try different filters.")
else:
    for item in filtered:
        render_card(item)

st.markdown("---")
st.caption("Prototype UI — Regulatory Intelligence System — v0.1")

