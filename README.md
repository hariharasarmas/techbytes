**Demo App for Oracle Cloud Generative AI Services**

The RAG Agent harnesses the capabilities of Oracle's Cloud Data Platform to deliver a seamless and insightful retrieval-augmented generation (RAG) chat experience, powered by Oracle Generative AI Agents


**Architecture**

![image](https://github.com/user-attachments/assets/f06e446a-de25-489e-a9a6-2aa4a091c15b)

Object Storage: Securely stores private data files for the knowledge base using AES-256 encryption.

Generative AI Agents: Deliver the RAG pipeline as a Platform-as-a-Service (PaaS) solution

Compute: A virtual machine hosts the Streamlit application, powering the user interface


**Generative AI Agent Features**

Secure and Private: Your data remains fully confidential within your Oracle Cloud tenancy, protected by Oracle's comprehensive security features

Chat with the GenAI Agent: Engage in a conversation, ask questions, and receive insightful, meaningful answers

View Citations: Explore the sources behind the agent's responses to validate the responses are grounded.

Reset Chat: Click to clear the session history and begin a new conversation.


**Explore it within your Oracle Cloud tenancy**

**Before you start**

You must have an Oracle Cloud Account subscribed to one of the following regions: Chicago, Frankfurt, or London.

You must have access to a Generative AI Agents endpoint

This app provides only the front-end interface.

Availability: Currently, it is only accessible through whitelisting in the Chicago region

OCI Configuration: You must configure your OCI settings to authenticate to the agent endpoint.

Update Secrets File: Modify the .streamlit/secrets.toml file to include the following:

agent_endpoint_id

compartment_id

Other required items as mentioned in the comments within the file

**Oracle Cloud Free Tier**

You can sign up for an Oracle Cloud Free Tier Account, which offers a range of free services

You get $300 in credits for 30 days to use on all available services

Oracle Autonmous Database with APEX

Provides 20 GB of Object Storage and 20 GB of Archive Storage

You get Always Free Resources for as long as you want them including but not limited to:

2 AMD Compute Instances with 1/8 OCPU and 1 GB RAM each

You can get up to 4 ARM Compute Instances, offering a combined total of 4 OCPUs and 24 GB of RAM

Networking Services, including Virtual Cloud Network (VCN), Load Balancer, Site-to-Site VPN, and 10 TB of outbound data transfer per month, enabling secure and scalable networking for your cloud infrastructure

200 GB Block Storage

Security Services including Certificates, Valut and Bastion (managed SSH jumpbox)

Observability Services including Logging, Monitoring, Notifications



**Get started**

Set up the Generative AI Agents service in your Oracle Cloud account, and make sure to note the agent_endpoint_id for authentication and integration purposes.

Launch a VM with Oracle Linux 

SSH into your VM 

Set up OCI config

Copy the provided code into your VM

Update the .streamlit/secrets.toml file by adding your agent_endpoint_id and compartment_id to the appropriate sections as specified in the file

If you want to run in isolated enveironent. Run in conda environment as below
conda activate <path>

You can run the steamlit application as below
streamlit run st_genai_agent.py --server.port 3119 

Your application will be running on http://server-ip-address:3119
If you have linux UI installed you can access your application or else you can access using VNC or x11 forwarding


**Screenshots**

![image](https://github.com/user-attachments/assets/dc0985b5-00c0-4757-b7a7-6b4f3f92f04d)

