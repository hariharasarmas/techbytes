**Demo App for Oracle Cloud Generative AI Services**

The RAG Agent leverages the power of Oracle's Cloud Data Platform to provide you with a seamless and informative retrieval-augmented generation (RAG) chat experience through Oracle Generative AI Agents, which is currently in beta.

**Generative AI Agent (Beta) Features**
Secure & Private: All data remains confidential within your Oracle Cloud tenancy, benefiting from all of the built-in security features.

Chat with the GenAI Agent: Have a conversation - ask questions and get insightful answers.

View Citations: Explore the sources behind the agent's responses to validate the responses are grounded.

Reset Chat: A button to clear the session history and start fresh.

**Underlying Architecture**

![image](https://github.com/user-attachments/assets/f06e446a-de25-489e-a9a6-2aa4a091c15b)

Object Storage: Stores private data files for the knowledge base with AES256 encryption.

Generative AI Agents (Beta): Provides the RAG pipeline as a PaaS service.

Generative AI Service: Can be either shared or dedicated hosting, with your choice of Cohere and Meta for Large Language Model (LLM).

Compute: A virtual machine hosts the Streamlit app to provide the UI.

**Try Out in Your Oracle Cloud Tenancy**

**Before you start**

You must have an Oracle Cloud Account subscribed to the Chicago, Frankfurt, or London region

You must already have an Generative AI Agents (beta) endpoint available

this app only provides a front end

currently only available with whitelisting in Chicago region

You must set up oci config in order to authenticate to the agent endpoint.
You must update .streamlit/secrets.toml

agent_endpoint_id

compartment_id

other items as noted in comments

**Oracle Cloud Free Tier**

Did you know you can sign up for an Oracle Cloud Free Tier Account?

You get $300 in credits for 30 days to use on all available services

You get Always Free Resources for as long as you want them including but not limited to:

Oracle Autonmous Database with APEX

NoSQL Database

2 AMD Compute Instances with 1/8 OCPU and 1 GB RAM each

Up to 4 ARM Compute Instances with a combined total of 4 OCPU and 24 GB of RAM

200 GB Block Storage

20 GB Object and Archive Storage

Security Services including Certificates, Valut and Bastion (managed SSH jumpbox)

Observability Services including Logging, Monitoring, Notifications

Networking Services including VCN, Load Balancer, Site-to-Site VPN, and 10 TB of outbound data transfer per month

If you are one of my customers I can get you up to 60 days and $500 in credits. Reach out to me directly and I will get you set up.

**Get started**

Set up Generative AI Agents service and note the agent_endpoint_id

Make sure you have port 8501 open on security list

Launch a VM with Oracle Linux 8 image and attach setup.sh as cloud-init script

SSH into your VM (opc@ipaddress) and check the log at /home/opc/genai_agent_setup.log
Run setup.sh if you did not add it as cloud-init script

Set up OCI config

Update .streamlit/secrets.toml with your agent_endpoint_id and compartment_id

Use run.sh to run the demo

Your application will be running on http://server-ip-address:8501

**Screenshots**

![image](https://github.com/user-attachments/assets/dc0985b5-00c0-4757-b7a7-6b4f3f92f04d)

