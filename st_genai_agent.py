import streamlit as st
import oci
import genai_agent_service_bmc_python_client

# OCI Configuration
CONFIG_PROFILE = "NextGen"
config = oci.config.from_file()
#endpoint = "https://agent-runtime.generativeai.us-chicago-1.oci.oraclecloud.com"
#agent_endpoint_id = "ocid1.genaiagentendpoint.oc1.us-chicago-1.12345"
endpoint = st.secrets["endpoint"] #make sure to put these in secrets.toml file
agent_endpoint_id = st.secrets["agent_endpoint_id"] #make sure to put these in secrets.toml file

# Streamlit UI
st.set_page_config(page_title="OpsGenAI Bot", 
                   page_icon="🤖", layout="centered", 
                   initial_sidebar_state="expanded", menu_items=None)
logo_image_path = st.secrets["logo"] 
st.logo(logo_image_path) 
INIT_MESSAGE = {"role": "assistant", "content": "Hi! I am Oracle Generative AI! How may I help you?"}

AVATAR_MAPPING = {
    "user": ":material/record_voice_over:",
    "assistant": "o.png"
    }

st.title("OpsGenAI Bot")
st.subheader("Powered by Oracle Generative AI")
# ist.info("Check out the [architecure diagram](https://raw.githubusercontent.com/cgpavlakos/genai_agent/main/RAG%20Demo%20Diagram.png), [product page](https://www.oracle.com/artificial-intelligence/generative-ai/agents/), and [source code](https://github.com/cgpavlakos/genai_agent/tree/main) to see how the Oracle Data Platform and Generative AI come together for this demo of a fully secure and private RAG chatbot.")

# Sidebar
with st.sidebar:
    if st.button("Reset Chat", type="primary", use_container_width=True, help="Reset chat history and clear screen"):
        st.session_state.messages = []  
        st.session_state.session_id = None  
        st.rerun()  
st.sidebar.markdown(
    """
    ## About

    This demo leverages the power of **Oracle's Cloud Data Platform** to provide you with a seamless and informative retrieval-augmented generation (RAG) chat experience , to provide information to the IGIU teams by training models with internal documents . 
    ## Features
    - **Secure & Private:** All data remains confidential within your Oracle Cloud tenancy, benefiting from all of the built-in security features.
    - **Chat with the GenAI Agent:** Have a conversation - ask questions and get insightful answers.
    - **View Citations:** Explore the sources behind the agent's responses to validate the responses are grounded. 
    - **Reset Chat:** A button to clear the session history and start fresh. 


    """
)

# Initialize chat history and session ID in session state
if "messages" not in st.session_state:
    st.session_state.messages = [INIT_MESSAGE]
if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Create GenAI Agent Runtime Client (only if session_id is None)
if st.session_state.session_id is None:
    genai_agent_runtime_client = genai_agent_service_bmc_python_client.GenerativeAiAgentRuntimeClient(
        config=config,
        service_endpoint=endpoint,
        retry_strategy=oci.retry.NoneRetryStrategy(),
        timeout=(10, 240)
    )

    # Create session
    create_session_details = genai_agent_service_bmc_python_client.models.CreateSessionDetails(
        display_name="display_name", idle_timeout_in_seconds=10, description="description"
    )
    create_session_response = genai_agent_runtime_client.create_session(create_session_details, agent_endpoint_id)
    
    # Store session ID
    st.session_state.session_id = create_session_response.data.id

    # Check if welcome message exists and append to message history
    if hasattr(create_session_response.data, 'welcome_message'):
        st.session_state.messages.append({"role": "assistant", "content": create_session_response.data.welcome_message})


# Display chat messages from history (including initial welcome message, if any)
for message in st.session_state.messages:
    avatar = AVATAR_MAPPING.get(message["role"], "o.png")  # Default to "o.png" if not found
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Get user input
if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar=":material/record_voice_over:"):
        st.markdown(user_input)

    # Execute session (re-use the existing session)
    genai_agent_runtime_client = genai_agent_service_bmc_python_client.GenerativeAiAgentRuntimeClient(
            config=config, 
            service_endpoint=endpoint,
            retry_strategy=oci.retry.NoneRetryStrategy(), 
            timeout=(10, 240)
        )
    # Display a spinner while waiting for the response
    with st.spinner("Working..."):  # Spinner for visual feedback 
        execute_session_details = genai_agent_service_bmc_python_client.models.ExecuteSessionDetails(
        user_message=str(user_input), should_stream=False  # You can set this to True for streaming responses
     )
        execute_session_response = genai_agent_runtime_client.execute_session(agent_endpoint_id, st.session_state.session_id, execute_session_details)

    # Display agent response
    if execute_session_response.status == 200:
        response_content = execute_session_response.data.message.content
        st.session_state.messages.append({"role": "assistant", "content": response_content.text})
        with st.chat_message("assistant"):
            st.markdown(response_content.text)
     # Display citations
        if response_content.citations:
         with st.expander("Citations"):  # Collapsable section
            for i, citation in enumerate(response_content.citations, start=1):
                st.write(f"**Citation {i}:**")  # Add citation number
                st.markdown(f"**Source:** [{citation.source_location.url}]({citation.source_location.url})") 
                st.text_area("Citation Text", value=citation.source_text, height=200) # Use st.text_area for better formatting   
    else:
        st.error(f"API request failed with status: {execute_session_response.status}")
