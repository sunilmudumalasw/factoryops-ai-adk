import pandas as pd
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st

from tools.factory_health_tool import analyze_factory_health
from business.audit_log import log_decision

st.set_page_config(
    page_title="FactoryOps AI",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 FactoryOps AI")
st.subheader("Multi-Agent Manufacturing COO")

if "report" not in st.session_state:
    st.session_state.report = None

if "decision_status" not in st.session_state:
    st.session_state.decision_status = None

if st.button("Analyze Factory"):
    st.session_state.report = analyze_factory_health()
    st.session_state.decision_status = None

if st.session_state.report:

    report = st.session_state.report

    st.header("🏭 Factory Health Report")

    # Overall Status
    st.error(f"Overall Factory Status: {report['overall_status']}")

    # Top Priority
    st.warning(f"Top Priority: {report['top_priority']}")

    # Executive Summary
    st.subheader("Executive Summary")
    st.info(report["executive_summary"])
    st.divider()

    st.subheader("🧠 Executive Decision")

    decision = report["executive_decision"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Risk Level", decision["risk_level"])
        st.metric("Business Priority", decision["business_priority"])

    with col2:
        st.metric("Business Impact", decision["estimated_business_impact"])

    if decision["approval_required"]:
        st.error("⚠ Executive Approval Required")
    else:
        st.success("✅ No Approval Required")

    if decision["approval_required"] and st.session_state.decision_status is None:
        col1, col2 = st.columns(2)

        with col1:
            if st.button("✅ Approve Decision"):
                log_decision("APPROVED", decision)
                st.session_state.decision_status =   "APPROVED"
                st.rerun()

        with col2:
            if st.button("❌ Reject Decision"):
                log_decision("REJECTED", decision)
                st.session_state.decision_status = "REJECTED"
                st.rerun()
    if st.session_state.decision_status == "APPROVED":
        st.success("✅ Executive Decision Approved")

        st.info(
            """
**Next Action**

• Launch immediate quality investigation

• Notify Quality Manager

• Schedule corrective action review

• Monitor defect trend over the next production cycle
"""
    )

    elif st.session_state.decision_status == "REJECTED":
        st.warning("❌ Executive Decision Rejected")

        st.info(
            """
**Next Action**

• Recommendation has been cancelled

• No operational changes will be executed

• Continue monitoring factory health
"""
    )

    st.info(f"**Recommended Action:** {decision['recommended_action']}")

    st.caption(f"Reason: {decision['reason']}")
    st.divider()

    st.subheader("Key Performance Indicators")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Factory Status",
            report["overall_status"]
        )

    with kpi2:
        st.metric(
            "Top Priority",
            report["top_priority"]
        )

    with kpi3:
        st.metric(
            "Critical Defects",
            report["quality"]["critical_defects"]
        )

    with kpi4:
        st.metric(
            "Low Stock Items",
            report["inventory"]["low_stock_count"]
        )

    # Three Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🏭 Production")
        production_status = report["production"]["status"]

        if production_status == "Critical":
            st.error(f"🔴 {production_status}")
        elif production_status == "Warning":
            st.warning(f"🟡 {production_status}")
        else:
            st.success(f"🟢 {production_status}")
        st.metric("Machines", report["production"]["total_machines"])
        st.metric("Avg Speed", f"{report['production']['average_speed']:.2f}")

    with col2:
        st.subheader("📦 Inventory")
        inventory_status = report["inventory"]["status"]

        if inventory_status == "Critical":
            st.error(f"🔴 {inventory_status}")
        elif inventory_status == "Attention Required":
            st.warning(f"🟡 {inventory_status}")
        else:
            st.success(f"🟢 {inventory_status}")
        st.metric("Low Stock", report["inventory"]["low_stock_count"])
        st.metric("Lead Time", report["inventory"]["average_lead_time"])

    with col3:
        st.subheader("🔍 Quality")
        quality_status = report["quality"]["status"]

        if quality_status == "Critical":
            st.error(f"🔴 {quality_status}")
        elif quality_status == "Warning":
            st.warning(f"🟡 {quality_status}")
        else:
            st.success(f"🟢 {quality_status}")
        st.metric("Critical Defects", report["quality"]["critical_defects"])
        st.metric("Repair Cost", f"${report['quality']['average_repair_cost']:.2f}")

    st.divider()

    st.subheader("Recommended Actions")

    st.write("1. " + report["quality"]["recommendation"])
    st.write("2. " + report["inventory"]["recommendation"])
    st.write("3. " + report["production"]["recommendation"])

    st.divider()

    st.subheader("📊 Quality Defect Distribution")

    defect_df = pd.DataFrame(
        {
            "Defect Type": report["quality"]["defect_types"].keys(),
            "Count": report["quality"]["defect_types"].values(),
        }
    )

    st.bar_chart(
        defect_df.set_index("Defect Type")
    )