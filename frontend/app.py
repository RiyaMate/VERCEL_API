import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Lab3 Demo", page_icon="🔬")

# Get base URL from secrets
BASE_URL = st.secrets["BACKEND_URL"]

def call_root_endpoint():
    """Call the root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def call_health_endpoint():
    """Call the health check endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def call_env_demo_endpoint():
    """Call the environment demo endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/env-demo")
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# Main app
st.title("🔬 Lab3 Demo")
st.write("A simple demo showcasing FastAPI endpoints with environment variables")

# Create three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Root Endpoint")
    if st.button("Call Root"):
        response = call_root_endpoint()
        st.json(response)

with col2:
    st.subheader("Health Check")
    if st.button("Check Health"):
        response = call_health_endpoint()
        st.json(response)

with col3:
    st.subheader("Env Demo")
    if st.button("Get Env Value"):
        response = call_env_demo_endpoint()
        st.json(response)

# Add some information about the configuration
st.divider()
st.subheader("Configuration")
st.write(f"Backend URL: `{BASE_URL}`")
st.info("The backend URL is configured using .streamlit/secrets.toml")
