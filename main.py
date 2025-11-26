import streamlit as st
import pandas as pd
from datetime import datetime

#-------------------------
# Mock Data
#-------------------------
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

#-------------------------
# Page Layout
#-------------------------
st.set_page_config(page_title="Regulatory Intelligence Feed", layout="wide")

st.title("📰 Regulatory Intelligence Feed")
st.caption("Card-based intelligence UI – Prototype")

#-------------------------
# Filters
#-------------------------
with st.container():
    col1, col2, col3 = st.columns([2,1,1])
    search = col1.text_input("🔍 Search updates...", placeholder="e.g. oncology, GMP, vaccine")
    region_filter = col2.multiselect("🌍 Region", ["US", "EU", "UK"], default=[])
    impact_filter = col3.multiselect("⚠ Impact Level", ["High", "Medium", "Low"], default=[])

# Filter logic
filtered = []
for item in data:
    if search and search.lower() not in item["title"].lower() and search.lower() not in item["summary"].lower():
        continue
    if region_filter and item["region"] not in region_filter:
        continue
    if impact_filter and item["impact"] not in impact_filter:
        continue
    filtered.append(item)

st.write("")  

#-------------------------
# Card Renderer
#-------------------------
def render_card(item):
    with st.container():
        st.markdown(f"""
        <div style="
            border:1px solid #d3d3d3;
            padding:18px;
            border-radius:10px;
            margin-bottom:15px;
            background:#fafafa;">
            
            <div style="display:flex; justify-content:space-between;">
                <strong style="font-size:18px;">{item['title']}</strong>
                <span style="font-size:14px; color:gray;">{item['date']}</span>
            </div>

            <p style="margin-top:6px; font-size:15px;">{item['summary']}</p>

            <div style="margin-top:10px;">
                <span style="background:#eef;padding:4px 8px;border-radius:6px;margin-right:6px;">
                    {item['agency']}
                </span>
                <span style="background:#efe;padding:4px 8px;border-radius:6px;margin-right:6px;">
                    Region: {item['region']}
                </span>
                <span style="background:#fee;padding:4px 8px;border-radius:6px;margin-right:6px;">
                    Impact: {item['impact']}
                </span>
                <span style="background:#f0f0f0;padding:4px 8px;border-radius:6px;margin-right:6px;">
                    Score: {item['score']}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"🧠 Show AI Summary ({item['agency']})", key=item['title']):
            st.info(f"LLM Summary:\n\nThis regulation is likely to impact compliance reporting requirements and operational workflows.")

# Render filtered cards
if not filtered:
    st.warning("No matching results. Try adjusting filters.")
else:
    for item in filtered:
        render_card(item)

# Optional bottom assistant
st.markdown("---")
st.subheader("💬 Ask the Intelligence Assistant")
user_query = st.text_input("Ask a question like: 'Show high-risk oncology alerts in the last month'")

if st.button("Generate Insight"):
    st.success("✨ AI Response Placeholder:\n\nBased on current data, FDA and EMA issued 2 significant oncology guidance changes impacting post-market safety compliance.")

