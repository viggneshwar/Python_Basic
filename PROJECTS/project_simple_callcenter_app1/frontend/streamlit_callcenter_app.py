import streamlit as st
from project_simple_callcenter_app1.installation_util.installation_cost import CostingClass

st.set_page_config(page_title="Call Center Installation Cost Calculator", layout="centered")

st.title("Call Center - Installation Cost Estimator")
st.write("This mini app demonstrates class instantiation and class member functions.")

st.header("Create Costing Class Instance")

product_name = st.selectbox(
        "Select Product:",
        ["voip", "stb", "router", "switch", "other"],
        index=0,
        help="Select the product to calculate installation time")

cost_per_hour = st.number_input(
    "Enter the cost per hour (₹):",
    min_value=0,
    step=50,
    value=100,
)

if st.button("Create CostingClass Object"):
    st.session_state["costing_obj"] = CostingClass(cost_per_hour)
    st.success(f"CostingClass object created with cost_per_hour = ₹{cost_per_hour}")
    st.write(f"Object Memory Address: {hex(id(st.session_state['costing_obj']))}")

if "costing_obj" in st.session_state:
    st.header("Select Product & Calculate")

    if st.button("Calculate"):
        obj = st.session_state["costing_obj"]

        install_time = obj.calculate_installtime(product_name)

        total_cost = obj.calculate_cost(install_time)

        st.subheader("Installation Summary")
        st.write(f"**Product:** {product_name}")
        st.write(f"**Cost Per Hour:** ₹{obj.cost_per_hour}")
        st.write(f"**Installation Time:** {install_time} hours")
        st.write(f"**Total Cost:** ₹{total_cost}")
        st.success("Calculation completed")
