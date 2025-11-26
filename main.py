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
        "summary": "Significant update impacting post-market surveillance reporting requirements for oncology molecules."
    },
    {
        "agency": "EMA",
        "region": "EU",
        "date": "2025-11-20",
        "impact": "Medium",
        "score": 74,
        "title": "EMA updates GMP clause for sterile manufacturing",
        "summary": "Revision focuses on sterility validation and batch release documentation."
    },
    {
        "agency": "MHRA",
        "region": "UK",
        "date": "2025-11-19",
        "impact": "Low",
        "score": 56,
        "title": "MHRA device reporting rule refinement",
        "summary": "Minor revision in reporting timelines for medical device complaints."
    },
]

# -------------------------
# Page Header
# -------------------------
st.title("📄 Regulatory Intelligence Feed")
st.write("Prototype text-based mock UI")

# -------------------------
# Filters
# -------------------------
col1, col2, col3 = st.columns([2, 1, 1])
search = col1.text_input("Search updates...")
region_filter = col2.multiselect("Region", ["US", "EU", "UK"])
impact_filter = col3.multiselect("Impact Level", ["High", "Medium", "Low"])

# -------------------------
# Apply Filters
# -------------------------
filtered = []

for item in data:
    if search and search.lower() not in item["title"].lower():
        continue
    if region_filter and item["region"] not in region_filter:
        continue
    if impact_filter and item["impact"] not in impact_filter:
        continue
    filtered.append(item)

# -------------------------
# Render Text Cards
# -------------------------
st.divider()

if not filtered:
    st.warning("No matching results. Try adjusting filters.")

for item in filtered:
    with st.container():
        st.subheader(item["title"])
        st.write(f"**Agency:** {item['agency']} | **Region:** {item['region']} | **Date:** {item['date']}")
        st.write(f"**Impact:** {item['impact']} | **Score:** {item['score']}")
        
        st.write("\n**Summary:**")
        st.write(item['summary'])

        if st.button(f"Generate AI Summary ({item['agency']})", key=item['title']):
            st.success("AI Summary placeholder: This regulatory update may require internal compliance review and documentation updates.")

        st.divider()

# -------------------------
# Bottom Section
# -------------------------
st.caption("Regulatory Intelligence UI Mock • v0.2")

