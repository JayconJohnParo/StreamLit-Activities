# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:32:14 2025
@author: Administrator
"""

import streamlit as st

# Sidebar Filters
st.sidebar.title("🔍 Filters & Options")
topic = st.sidebar.selectbox(
    "Choose a Topic:",
    ["Data Warehousing", "ETL Processes", "Enterprise Data Management", "Data Governance"]
)
filter_value = st.sidebar.slider("🔧 Importance Level", 0, 100, 50)

# Main Title
st.title("🏢 Data Warehousing & Enterprise Data Management")
st.write(f"You selected **{topic}** with an importance level of **{filter_value}**.")

# Layout with Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏗️ Data Warehousing Architecture")
    st.write("""
    - Central repository built for analytics.
    - Uses OLAP systems for faster queries.
    - Includes staging, integration, and access layers.
    """)

with col2:
    st.subheader("🔄 ETL: Extract, Transform, Load")
    st.write("""
    - **Extract** from operational systems, files, APIs.
    - **Transform** with cleaning, deduplication, schema matching.
    - **Load** into structured warehouse tables.
    """)

# Tabs for organized content
tab1, tab2 = st.tabs(["📚 Core Concepts", "📊 Business Applications"])

with tab1:
    st.markdown("### Definitions & Frameworks")
    st.markdown("""
    - **Enterprise Data Management (EDM)**: Governance and quality control of data across an organization.
    - **Metadata Management**: Handles definitions and relationships of data.
    - **Master Data Management (MDM)**: Ensures consistency of key data entities (e.g., customers, products).
    """)

with tab2:
    st.markdown("### Use Cases in Industry")
    st.markdown("""
    - **Retail**: Unified customer profiles across platforms.
    - **Healthcare**: Standardized patient records and compliance.
    - **Finance**: Risk modeling and fraud detection through historical data.
    """)

# Expander for extra info
with st.expander("📖 More Information"):
    st.write("""
    Data Warehousing and EDM are the backbone of modern data strategy.
    They ensure that data is accurate, accessible, and aligned with business needs.
    With the rise of cloud platforms and real-time processing, organizations can make faster, data-driven decisions.
    """)
