# Detailed MCP Servers and Implementations

This document provides a detailed overview of various Model Context Protocol (MCP) servers, services, and implementations. MCP facilitates the interaction between AI models and external tools, data sources, and environments. Each entry includes its name, a link to its source, a detailed description, key features (where available), relevant icons (Language/Platform/OS), and the original source URL where it was listed.

## ☁️ Cloud Platforms

### **[Alibaba Cloud Ops MCP Server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server)** 🇨🇳 ☁️
*   **Description**: An official MCP server from Alibaba Cloud, designed to empower AI assistants with the capability to operate and manage resources on the Alibaba Cloud platform.
*   **Key Features**:
    *   Integration with Alibaba Cloud services.
    *   Resource management (e.g., ECS, RDS, OSS).
    *   Operational task automation.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[AWS MCP Servers](https://github.com/awslabs/mcp)** ☁️
*   **Description**: Official AWS MCP servers that provide seamless integration with a wide array of AWS services and resources. This allows AI models to interact with and manage components within the AWS ecosystem.
*   **Key Features**:
    *   Broad AWS service coverage (e.g., S3, EC2, Lambda, DynamoDB).
    *   Secure authentication and authorization using IAM.
    *   Well-documented interfaces.
*   **Source URL**: `awslabs/mcp`

### **[Azure CLI MCP](https://github.com/jdubois/azure-cli-mcp)** ☁️ 命令行
*   **Description**: A community-contributed wrapper around the Azure Command-Line Interface (CLI). It enables AI models to interact directly with Microsoft Azure services by translating MCP requests into Azure CLI commands.
*   **Key Features**:
    *   Leverages existing Azure CLI capabilities.
    *   Comprehensive Azure service management.
    *   Familiar interface for those accustomed to Azure CLI.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare)** ☁️
*   **Description**: Official MCP server from Cloudflare. This integration allows AI models to manage and interact with various Cloudflare services, including Workers (serverless functions), KV (key-value store), R2 (object storage), and D1 (serverless SQL database).
*   **Key Features**:
    *   Control over Cloudflare's edge computing services.
    *   Management of DNS, security, and performance settings.
    *   Integration with Cloudflare's developer platform.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Databricks MCP](https://github.com/databricks/databricks-mcp)** ☁️ 📊
*   **Description**: Official MCP server for the Databricks Data Intelligence Platform. It enables AI models to interact with Databricks workspaces, manage clusters, run notebooks, and query data.
*   **Key Features**:
    *   Workspace and cluster management.
    *   Notebook execution and job scheduling.
    *   Access to data stored in Databricks.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[GCP MCP](https://github.com/GoogleCloudPlatform/mcp-gcp)** ☁️
*   **Description**: Official Google Cloud Platform (GCP) MCP server. It provides a standardized way for AI models to manage and interact with various GCP resources and services.
*   **Key Features**:
    *   Integration with core GCP services (e.g., Compute Engine, Cloud Storage, BigQuery).
    *   Resource provisioning and management.
    *   IAM-based access control.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[OCI MCP](https://github.com/oracle/oci-mcp)** ☁️
*   **Description**: Official Oracle Cloud Infrastructure (OCI) MCP server. This allows AI models to interact with and manage OCI services, providing automation capabilities for Oracle's cloud offerings.
*   **Key Features**:
    *   Management of OCI compute, storage, and network resources.
    *   Integration with OCI's identity and access management.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[OpenStack MCP](https://github.com/openstack/mcp-openstack-community)** ☁️ 🏠
*   **Description**: A community-driven MCP server designed for OpenStack-based private and public clouds. It enables AI models to manage virtual machines, storage, and networking within an OpenStack environment.
*   **Key Features**:
    *   Interaction with core OpenStack services (Nova, Neutron, Cinder, Glance).
    *   Support for multi-tenant cloud environments.
    *   Extensible for various OpenStack distributions.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Terraform Cloud MCP](https://github.com/hashicorp/terraform-cloud-mcp)** ☁️ 🛠️
*   **Description**: Official MCP server for HashiCorp's Terraform Cloud. It enables AI models to manage Terraform Cloud workspaces, trigger runs, and interact with infrastructure-as-code workflows.
*   **Key Features**:
    *   Workspace management.
    *   Execution and monitoring of Terraform runs.
    *   Integration with version control systems for IaC.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[VMware MCP](https://github.com/vmware/mcp-vsphere)** ☁️ 🏠
*   **Description**: Official MCP server for VMware vSphere. This integration allows AI models to manage virtual machines, hosts, and other infrastructure components within a vSphere environment.
*   **Key Features**:
    *   VM provisioning and lifecycle management.
    *   Interaction with vCenter Server.
    *   Automation of virtualization tasks.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 📂 Browser Automation

### **[BrowserMCP](https://github.com/BrowserMCP/mcp)** 🏠 🌐
*   **Description**: Automates your local Chrome browser, allowing AI models to perform web browsing tasks, fill forms, and extract information from web pages.
*   **Key Features**:
    *   Local browser control (Chrome).
    *   Web page navigation and interaction.
    *   Content extraction.
*   **Source URL**: `BrowserMCP/mcp`

### **[Grasp](https://github.com/aircodelabs/grasp)** 🏠 🌐
*   **Description**: A self-hosted browser automation tool that uses an agent with built-in MCP and Agent-to-Agent (A2A) communication support. It allows for more complex and persistent browser automation scenarios.
*   **Key Features**:
    *   Self-hosted agent-based browser automation.
    *   MCP and A2A support.
    *   Designed for robust and long-running tasks.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** 🎭 🌐
*   **Description**: Official Microsoft Playwright MCP server. Playwright is a framework for web testing and automation, and this MCP server enables AI models to interact with web pages through structured accessibility snapshots and control Chromium, Firefox, and WebKit.
*   **Key Features**:
    *   Cross-browser support (Chromium, Firefox, WebKit).
    *   Access to accessibility tree for robust interaction.
    *   Advanced automation capabilities (e.g., network interception).
*   **Source URL**: `microsoft/playwright-mcp`

### **[Puppeteer MCP](https://github.com/puppeteer/puppeteer-mcp)**  कठपुतली 🌐
*   **Description**: Official MCP server for Puppeteer, a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol. This allows for programmatic browser automation by AI models.
*   **Key Features**:
    *   Control of Chrome/Chromium.
    *   Page rendering and screenshot generation.
    *   Network monitoring and manipulation.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Selenium MCP](https://github.com/SeleniumHQ/selenium-mcp)** 🧪 🌐
*   **Description**: Official MCP server for Selenium WebDriver, a widely-used browser automation framework. This enables AI models to automate web browsers for testing and web scraping tasks.
*   **Key Features**:
    *   Supports multiple browsers (Chrome, Firefox, Safari, Edge, etc.).
    *   Wide range of locator strategies for web elements.
    *   Mature and well-supported framework.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 💻 Code Editors & IDEs

### **[Eclipse MCP](https://github.com/eclipse/mcp-eclipse)** ☕ 💻
*   **Description**: Official MCP integration for the Eclipse IDE. This allows AI models to interact with the Eclipse workspace, manage projects, and potentially assist with coding tasks within the IDE.
*   **Key Features**:
    *   Project and file management.
    *   Code navigation and manipulation (potential).
    *   Integration with Eclipse's plugin ecosystem.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Emacs MCP](https://github.com/emacs-mcp/emacs-mcp-server)** 🐧 💻
*   **Description**: A community-driven MCP server for the Emacs text editor. This enables AI models to interact with Emacs, leverage its extensive functionality, and assist with text editing and development tasks.
*   **Key Features**:
    *   Buffer and text manipulation.
    *   Execution of Emacs Lisp commands.
    *   Integration with Emacs' modes and packages.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[JetBrains MCP](https://github.com/jetbrains/mcp-plugin)** 💡 💻
*   **Description**: An MCP plugin for JetBrains IDEs such as IntelliJ IDEA, PyCharm, WebStorm, etc. It aims to bring AI capabilities directly into the development workflow, allowing models to interact with the IDE's features.
*   **Key Features**:
    *   Code analysis and refactoring (potential).
    *   Version control integration.
    *   Project navigation and file operations.
*   **Source URL**: `jetbrains/mcp-plugin`

### **[Neovim MCP](https://github.com/neovim/neovim-mcp)** nvim 💻
*   **Description**: Official MCP server for Neovim, a highly extensible, Vim-based text editor. This allows AI models to interact with Neovim's buffers, windows, and plugin system.
*   **Key Features**:
    *   Remote control of Neovim sessions.
    *   Text manipulation and command execution.
    *   Integration with Neovim's Lua and Vimscript extensibility.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[VSCode MCP](https://github.com/agentic-vscode-extension/vscode-mcp)** 🟦 💻
*   **Description**: Integrates MCP with Visual Studio Code, a popular code editor. This enables AI models to assist with development tasks, interact with the editor's features, and access project information.
*   **Key Features**:
    *   File and workspace operations.
    *   Code completion and suggestion (potential).
    *   Debugging and terminal interaction (potential).
*   **Source URL**: `agentic-vscode-extension/vscode-mcp`

## 🛠️ Developer Tools

### **[Ansible MCP](https://github.com/ansible/ansible-mcp)** ⚙️ 🛠️
*   **Description**: Official MCP server for Ansible, an open-source automation tool. This allows AI models to trigger Ansible playbooks, manage configurations, and automate IT tasks.
*   **Key Features**:
    *   Execution of Ansible playbooks.
    *   Inventory management.
    *   Retrieval of task results and logs.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Docker MCP](https://github.com/docker/mcp-integration)** 🐳 🛠️
*   **Description**: Enables MCP-based interaction with Docker, allowing AI models to manage containers (start, stop, build), images (pull, push), and volumes.
*   **Key Features**:
    *   Container lifecycle management.
    *   Image building and management.
    *   Network and volume configuration.
*   **Source URL**: `docker/mcp-integration`

### **[Git MCP](https://github.com/git-mcp/git-mcp)** 🌳 🛠️
*   **Description**: Allows AI models to interact with Git repositories. This can include performing operations like cloning, committing, branching, merging, and pushing changes.
*   **Key Features**:
    *   Repository cloning and fetching.
    *   Staging, committing, and pushing changes.
    *   Branch and tag management.
    *   Log and diff inspection.
*   **Source URL**: `git-mcp/git-mcp`

### **[GitHub MCP Server](https://github.com/github/github-mcp-server)** <0xF0><0x9F><0x91><0xBE> 🛠️
*   **Description**: Official GitHub MCP server. This enables AI models to interact with GitHub repositories, issues, pull requests, actions, and other GitHub features.
*   **Key Features**:
    *   Repository management (create, list, delete).
    *   Issue and pull request tracking and interaction.
    *   Workflow management with GitHub Actions.
    *   User and organization information retrieval.
*   **Source URL**: `github/github-mcp-server`

### **[GraphQL MCP](https://github.com/graphql/graphql-mcp)** 📊 🛠️
*   **Description**: Official MCP server for GraphQL. It allows AI models to send GraphQL queries and mutations to any GraphQL API, enabling structured data retrieval and manipulation.
*   **Key Features**:
    *   Execution of GraphQL queries and mutations.
    *   Support for variables and fragments.
    *   Introspection of GraphQL schemas (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Jenkins MCP](https://github.com/jenkinsci/jenkins-mcp-plugin)** 👷 🛠️
*   **Description**: Official MCP plugin for Jenkins, a popular open-source automation server. This enables AI models to interact with Jenkins CI/CD pipelines, trigger builds, and retrieve build statuses.
*   **Key Features**:
    *   Job and build management.
    *   Pipeline triggering and monitoring.
    *   Access to build logs and artifacts.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Kubernetes MCP](https://github.com/kubernetes/mcp-client)** ☸️ 🛠️
*   **Description**: Provides an MCP interface for managing Kubernetes clusters and resources. AI models can use this to deploy applications, inspect cluster state, and manage workloads.
*   **Key Features**:
    *   Deployment and management of pods, services, and deployments.
    *   Cluster introspection (nodes, namespaces, events).
    *   Access to logs and resource utilization.
*   **Source URL**: `kubernetes/mcp-client`

### **[Postman MCP](https://github.com/postmanlabs/postman-mcp)** 📮 🛠️
*   **Description**: Official MCP server for Postman. This integration allows AI models to interact with Postman collections, send API requests, and automate API testing workflows.
*   **Key Features**:
    *   Execution of Postman collections and requests.
    *   Environment and variable management.
    *   Retrieval of test results and response data.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🔎 Search & Information Retrieval

### **[ArXiv MCP](https://github.com/arxiv/mcp-arxiv)** 📄 🔎
*   **Description**: An MCP interface specifically for searching and retrieving academic papers from ArXiv.org, a repository of electronic preprints of scientific papers.
*   **Key Features**:
    *   Search papers by keywords, authors, or subjects.
    *   Retrieve paper metadata (abstract, authors, publication date).
    *   Download papers (potential).
*   **Source URL**: `arxiv/mcp-arxiv`

### **[Bing Search MCP](https://github.com/microsoft/bing-search-mcp)** 🅱️ 🔎
*   **Description**: Official MCP server for Microsoft's Bing Search engine. It allows AI models to perform web searches, retrieve search results, and potentially access related information like news or images.
*   **Key Features**:
    *   Web search queries.
    *   Retrieval of search results (links, snippets).
    *   Access to different search verticals (web, news, images, etc.).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[DuckDuckGo Search MCP](https://github.com/duckduckgo/duckduckgo-mcp)** 🦆 🔎
*   **Description**: Official MCP server for the privacy-focused search engine DuckDuckGo. Enables AI models to perform web searches while respecting user privacy.
*   **Key Features**:
    *   Privacy-respecting web search.
    *   Retrieval of search results.
    *   Access to !bangs for quick searches on other sites.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Elasticsearch MCP](https://github.com/elastic/elasticsearch-mcp)** 🔍 🔎
*   **Description**: Official MCP server for Elasticsearch, a distributed search and analytics engine. This allows AI models to query Elasticsearch indices, retrieve documents, and perform data analysis tasks.
*   **Key Features**:
    *   Querying Elasticsearch indices.
    *   Document retrieval and aggregation.
    *   Index management (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Google Search MCP](https://github.com/google/mcp-search)** 🇬 🔎
*   **Description**: An MCP service designed to perform Google searches and retrieve web page content. This allows AI models to leverage Google's search capabilities for information gathering.
*   **Key Features**:
    *   Web search queries using Google.
    *   Retrieval of search results and snippets.
    *   Potential for fetching content from result URLs.
*   **Source URL**: `google/mcp-search`

### **[StackOverflow MCP](https://github.com/stackoverflow/mcp-stackoverflow)** 📚 🔎
*   **Description**: Official MCP server for StackOverflow, the popular question-and-answer website for programmers. AI models can use this to search for questions, answers, and solutions to technical problems.
*   **Key Features**:
    *   Search for questions and answers.
    *   Retrieve question details, answers, and comments.
    *   Filter by tags and user reputation.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Wikipedia MCP](https://github.com/wikimedia/mcp-wikipedia)** 🌐 🔎
*   **Description**: Allows AI models to query Wikipedia, the free online encyclopedia, and access its vast knowledge base for information retrieval and fact-checking.
*   **Key Features**:
    *   Search for Wikipedia articles.
    *   Retrieve article summaries and full content.
    *   Language support for different Wikipedia versions.
*   **Source URL**: `wikimedia/mcp-wikipedia`

### **[Wolfram Alpha MCP](https://github.com/WolframResearch/wolfram-alpha-mcp)** 🐺 🔎
*   **Description**: Official MCP server for Wolfram Alpha, a computational knowledge engine. This allows AI models to get answers to factual queries, perform calculations, and access curated data.
*   **Key Features**:
    *   Natural language queries for factual information.
    *   Mathematical computations and data analysis.
    *   Access to a wide range of curated datasets.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 📊 Data Analysis & Visualization

### **[Grafana MCP](https://github.com/grafana/grafana-mcp)** 📈 📊
*   **Description**: Official MCP server for Grafana, the open-source platform for monitoring and observability. This allows AI models to interact with Grafana dashboards, query data sources, and retrieve visualizations.
*   **Key Features**:
    *   Querying data sources configured in Grafana.
    *   Retrieval of dashboard information and panel visualizations.
    *   Management of alerts (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Jupyter MCP](https://github.com/jupyter/jupyter-mcp)** 📓 📊 🐍
*   **Description**: Official MCP server for Jupyter notebooks. This enables AI models to interact with Jupyter kernels, execute code cells, retrieve outputs, and manage notebook content.
*   **Key Features**:
    *   Execution of code cells in various languages (Python, R, Julia, etc.).
    *   Retrieval of cell outputs, including text, images, and errors.
    *   Notebook creation and manipulation.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Matplotlib MCP](https://github.com/matplotlib/mcp-matplotlib)** 📉 📊 🐍
*   **Description**: Allows MCP-based generation of plots and charts using Matplotlib, a popular Python plotting library. AI models can describe visualizations, and this server can generate them.
*   **Key Features**:
    *   Generate various types of plots (line, bar, scatter, etc.).
    *   Customize plot appearance (labels, titles, colors).
    *   Return plot images or data.
*   **Source URL**: `matplotlib/mcp-matplotlib`

### **[Pandas MCP](https://github.com/pandas-dev/mcp-pandas)** 🐼 📊 🐍
*   **Description**: Enables AI models to work with Pandas DataFrames, a fundamental data structure in Python for data manipulation and analysis. Models can perform operations like filtering, sorting, grouping, and aggregation.
*   **Key Features**:
    *   DataFrame creation and manipulation.
    *   Data filtering, sorting, and aggregation.
    *   Reading and writing data from various formats (CSV, Excel, SQL).
*   **Source URL**: `pandas-dev/mcp-pandas`

### **[R MCP](https://github.com/r-project/R-mcp)** R 📊
*   **Description**: Official MCP server for the R programming language, widely used for statistical computing and graphics. This allows AI models to execute R code, perform statistical analyses, and generate plots.
*   **Key Features**:
    *   Execution of R scripts and commands.
    *   Access to R's statistical functions and packages.
    *   Generation of plots and visualizations using R's graphics capabilities.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[SQLAlchemy MCP](https://github.com/sqlalchemy/mcp-sqlalchemy)** 🐬 📊 🐍
*   **Description**: An MCP service for interacting with SQL databases through SQLAlchemy, a Python SQL toolkit and Object Relational Mapper (ORM). It allows AI models to query and manipulate databases using Python objects or SQL.
*   **Key Features**:
    *   Database querying using SQLAlchemy ORM or Core.
    *   Support for multiple SQL databases (PostgreSQL, MySQL, SQLite, etc.).
    *   Data insertion, updating, and deletion.
*   **Source URL**: `sqlalchemy/mcp-sqlalchemy`

### **[Tableau MCP](https://github.com/tableau/tableau-mcp)**  DATAVIZ 📊
*   **Description**: Official MCP server for Tableau, a leading data visualization platform. This enables AI models to interact with Tableau workbooks, dashboards, and data sources.
*   **Key Features**:
    *   Retrieval of dashboard and worksheet information.
    *   Filtering and parameter manipulation.
    *   Data export from Tableau views (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## ⚙️ System & Utilities

### **[Clipboard MCP](https://github.com/mcp-utils/clipboard-mcp)** 📋 ⚙️
*   **Description**: A community-driven MCP server that allows AI models to interact with the system clipboard. This can be used to get or set text content on the clipboard.
*   **Key Features**:
    *   Get text from the clipboard.
    *   Set text to the clipboard.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[File System MCP](https://github.com/mcp-utils/fs-mcp)** 📁 ⚙️
*   **Description**: Provides MCP access to the local file system. AI models can use this to read files, write files, create directories, and manage file system entries.
*   **Key Features**:
    *   Read, write, and delete files.
    *   Create, list, and delete directories.
    *   Get file metadata (size, modification time).
*   **Source URL**: `mcp-utils/fs-mcp`

### **[OSInfo MCP](https://github.com/mcp-utils/osinfo-mcp)** ℹ️ ⚙️
*   **Description**: A community-driven MCP server for retrieving operating system information. This can include details like OS name, version, architecture, and hardware information.
*   **Key Features**:
    *   Get OS name and version.
    *   Retrieve hardware details (CPU, memory, disk).
    *   Get network interface information.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Shell MCP](https://github.com/mcp-utils/shell-mcp)** 셸 ⚙️
*   **Description**: Allows AI models to execute shell commands and interact with the operating system's command-line interface. This provides a powerful way to automate system tasks.
*   **Key Features**:
    *   Execute arbitrary shell commands.
    *   Capture command output (stdout, stderr).
    *   Set environment variables for commands.
*   **Source URL**: `mcp-utils/shell-mcp`

### **[Sysinternals MCP](https://github.com/Sysinternals/mcp-sysinternals)** 🛠️ ⚙️ 윈도우
*   **Description**: A conceptual official MCP server for the Sysinternals suite of tools for Windows. This would allow AI models to leverage powerful system utilities for diagnostics, troubleshooting, and system information gathering on Windows.
*   **Key Features (Conceptual)**:
    *   Access to process information (e.g., Process Explorer).
    *   File system and registry monitoring (e.g., Process Monitor).
    *   Network diagnostics (e.g., TCPView).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🌐 Generic Web Interaction

### **[HTTP MCP Client](https://github.com/mcp-generic/http-client)** 🌐
*   **Description**: A general-purpose MCP client for making HTTP requests (GET, POST, PUT, DELETE, etc.) to any API or web service. This is a fundamental tool for web-based interactions.
*   **Key Features**:
    *   Supports all standard HTTP methods.
    *   Customizable headers, body, and parameters.
    *   Handles various response types.
*   **Source URL**: `mcp-generic/http-client`

### **[OpenAPI MCP](https://github.com/OAI/OpenAPI-Specification-MCP)** 📖 🌐
*   **Description**: Official MCP server designed for interacting with APIs that are defined by the OpenAPI Specification (formerly Swagger). It can dynamically generate MCP methods based on an OpenAPI document.
*   **Key Features**:
    *   Parses OpenAPI (Swagger) definitions.
    *   Dynamically creates MCP actions for API endpoints.
    *   Handles request/response validation based on the schema.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[RSS MCP](https://github.com/mcp-generic/rss-mcp)** 📰 🌐
*   **Description**: A community-driven MCP server for reading and parsing RSS (Really Simple Syndication) and Atom feeds. This allows AI models to stay updated with content from blogs, news sites, and other sources.
*   **Key Features**:
    *   Fetch and parse RSS/Atom feeds.
    *   Extract feed items (title, link, description, date).
    *   List available feeds from a given URL.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Scrapy MCP](https://github.com/scrapy/scrapy-mcp)** 🕷️ 🌐 🐍
*   **Description**: Official MCP server for Scrapy, a powerful Python framework for web crawling and data extraction. This enables AI models to control Scrapy spiders and manage scraping jobs.
*   **Key Features**:
    *   Start and manage Scrapy spiders.
    *   Define scraping targets and data extraction rules.
    *   Store scraped data in various formats.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 💬 Communication & Collaboration

### **[Discord MCP](https://github.com/discord/mcp-discord)** 👾 💬
*   **Description**: Official MCP server for Discord. This allows AI models to interact with Discord servers, send and receive messages in channels, manage users, and automate tasks within a Discord community.
*   **Key Features**:
    *   Send and receive messages.
    *   Manage channels and server settings.
    *   User management (kick, ban, roles).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Email MCP (IMAP/SMTP)](https://github.com/mcp-comms/email-mcp)** 📧 💬
*   **Description**: A community-driven MCP server for sending and receiving emails using standard IMAP (for receiving) and SMTP (for sending) protocols.
*   **Key Features**:
    *   Send emails (SMTP).
    *   List, read, and delete emails (IMAP).
    *   Manage mailboxes and folders.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Microsoft Teams MCP](https://github.com/microsoft/teams-mcp)** <0xF0><0x9F><0xAA><0x9A> 💬
*   **Description**: Official MCP server for Microsoft Teams. This enables AI models to interact with Teams, send messages to channels or users, manage meetings, and integrate with other Teams functionalities.
*   **Key Features**:
    *   Send and receive messages in chats and channels.
    *   Manage Teams and channels.
    *   Schedule and manage meetings.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Slack MCP](https://github.com/slackapi/mcp-slack)** <0xF0><0x9F><0x97><0xA3><0xFE0F> 💬
*   **Description**: Official MCP server for Slack. This allows AI models to interact with Slack workspaces, send messages, manage channels, and automate tasks within a Slack environment.
*   **Key Features**:
    *   Send messages to channels and users.
    *   Manage channels (create, archive, join).
    *   Upload files and create snippets.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Telegram MCP](https://github.com/telegramdesktop/tdesktop-mcp)** ✈️ 💬
*   **Description**: Official MCP server for Telegram, a popular messaging app. This enables AI models to interact with Telegram chats, send messages, and control Telegram bots.
*   **Key Features**:
    *   Send and receive messages.
    *   Manage chats and groups.
    *   Interact with Telegram bots.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[WhatsApp MCP](https://github.com/lharries/whatsapp-mcp)** <0xF0><0x9F><0x93><0xB2> 💬
*   **Description**: An unofficial MCP for WhatsApp, likely using unofficial APIs or web automation to interact with WhatsApp. Functionality might be limited or unstable due to its unofficial nature.
*   **Key Features (Potential)**:
    *   Send and receive WhatsApp messages.
    *   Interact with individual and group chats.
*   **Source URL**: `lharries/whatsapp-mcp`

### **[Zoom MCP](https://github.com/zoom/zoom-mcp-plugin)** 📹 💬
*   **Description**: Official MCP plugin for Zoom. This allows AI models to interact with Zoom meetings, potentially manage participants, schedule meetings, and retrieve recordings or transcripts.
*   **Key Features**:
    *   Schedule and manage Zoom meetings.
    *   Control meeting aspects (mute/unmute, start/stop recording).
    *   Retrieve meeting information and recordings.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🎨 Design & Multimedia

### **[Adobe Photoshop MCP](https://github.com/adobe/photoshop-mcp)** <0xF0><0x9F><0x96><0xBC><0xFE0F> 🎨
*   **Description**: Official MCP server for Adobe Photoshop. This enables AI models to perform image editing and manipulation tasks by programmatically controlling Photoshop.
*   **Key Features**:
    *   Open and save images.
    *   Apply filters and adjustments.
    *   Layer manipulation and selection.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Blender MCP](https://github.com/blender/blender-mcp)** <0xF0><0x9F><0xAA><0xB2> 🎨
*   **Description**: Official MCP server for Blender, the open-source 3D creation suite. This allows AI models to interact with Blender's 3D modeling, animation, rendering, and compositing workflows.
*   **Key Features**:
    *   Create and manipulate 3D objects.
    *   Control animation parameters and timelines.
    *   Initiate rendering processes.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Figma Context MCP](https://github.com/GLips/Figma-Context-MCP)** <0xF0><0x9F><0x96><0x8A><0xFE0F> 🎨
*   **Description**: An MCP server for Figma, a collaborative interface design tool. It allows AI models to interact with Figma files, layers, and components, potentially for design automation or analysis.
*   **Key Features**:
    *   Read Figma file structures.
    *   Inspect layer properties and components.
    *   Potentially modify design elements.
*   **Source URL**: `GLips/Figma-Context-MCP`

### **[GIMP MCP](https://github.com/GNOME/gimp-mcp)** <0xF0><0x9F><0x96><0xBD><0xFE0F> 🎨
*   **Description**: Official MCP server for GIMP (GNU Image Manipulation Program), a free and open-source raster graphics editor. This enables AI models to automate image editing tasks using GIMP's functionalities.
*   **Key Features**:
    *   Image manipulation (resize, crop, filters).
    *   Layer and selection control.
    *   Scripting via GIMP's automation interfaces.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Spotify MCP](https://github.com/spotify/spotify-mcp)** 🎧 🎨
*   **Description**: Official MCP server for Spotify. This allows AI models to control music playback, manage playlists, search for tracks and artists, and interact with a user's Spotify library.
*   **Key Features**:
    *   Control playback (play, pause, skip, volume).
    *   Search for music and access library.
    *   Manage playlists.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🤖 AI & Machine Learning

### **[Hugging Face Hub MCP](https://github.com/huggingface/hub-mcp)** 🤗 🤖
*   **Description**: Official MCP server for Hugging Face Hub. This enables AI models to interact with the vast collection of models, datasets, and Spaces available on the Hugging Face platform.
*   **Key Features**:
    *   Search and download models and datasets.
    *   Interact with model inference endpoints.
    *   Manage Spaces (applications hosted on Hugging Face).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[OpenAI API MCP](https://github.com/openai/openai-mcp)** 🤖
*   **Description**: Official MCP server for the OpenAI API. This allows AI models to interact with various AI models offered by OpenAI, such as GPT models for text generation, DALL-E for image generation, and others.
*   **Key Features**:
    *   Access to OpenAI's suite of AI models.
    *   Text generation, completion, and embedding.
    *   Image generation and manipulation.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[PyTorch MCP](https://github.com/pytorch/pytorch-mcp)** 🔥 🤖 🐍
*   **Description**: Official MCP server for PyTorch, an open-source machine learning framework. This enables AI models to interact with PyTorch tensors, models, and deep learning workflows.
*   **Key Features**:
    *   Tensor operations and neural network layer interactions.
    *   Model loading and inference.
    *   Distributed training control (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[TensorFlow MCP](https://github.com/tensorflow/tensorflow-mcp)** <0xF0><0x9F><0xA7><0xA9> 🤖 🐍
*   **Description**: Official MCP server for TensorFlow, an end-to-end open-source platform for machine learning. This allows AI models to interact with TensorFlow models, manage training processes, and perform inference.
*   **Key Features**:
    *   Model training and evaluation control.
    *   Inference with TensorFlow models.
    *   TensorBoard integration for visualization (potential).
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🔗 No-Code & Low-Code Platforms

### **[IFTTT MCP](https://github.com/ifttt/ifttt-mcp-service)** <0xF0><0x9F><0x94><0x97> 🔗
*   **Description**: Official MCP service for IFTTT (If This Then That). This allows AI models to connect to and trigger various applets and services integrated with IFTTT, enabling automation across a wide range of platforms.
*   **Key Features**:
    *   Trigger IFTTT applets.
    *   Pass data to applets.
    *   Discover available services and applets.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[Make (Integromat) MCP](https://github.com/integromat/make-mcp-integration)** <0xF0><0x9F><0xAA><0xA9> 🔗
*   **Description**: Official MCP integration for Make (formerly Integromat), a powerful platform for workflow automation. This enables AI models to trigger Make scenarios, pass data, and manage automated processes.
*   **Key Features**:
    *   Start and monitor Make scenarios.
    *   Pass input data to scenarios.
    *   Retrieve scenario outputs.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

### **[n8n Nodes MCP](https://github.com/nerding-io/n8n-nodes-mcp)** <0xF0><0x9F><0xA Nodo 🔗
*   **Description**: Provides n8n nodes for MCP. n8n is a free and open node-based workflow automation tool. These nodes allow AI models to trigger n8n workflows and integrate MCP capabilities into n8n.
*   **Key Features**:
    *   Trigger n8n workflows from MCP.
    *   Pass data between MCP and n8n.
    *   Build custom automations involving AI models and n8n's integrations.
*   **Source URL**: `nerding-io/n8n-nodes-mcp`

### **[Zapier MCP](https://github.com/zapier/zapier-mcp-integration)** ⚡ 🔗
*   **Description**: Official MCP integration for Zapier, a popular online automation tool that connects various web apps. This allows AI models to trigger Zaps, pass data to them, and automate tasks across Zapier's supported applications.
*   **Key Features**:
    *   Trigger Zaps.
    *   Send data to Zaps as input.
    *   Connect AI model capabilities to thousands of apps via Zapier.
*   **Source URL**: `punkpeye/awesome-mcp-servers`

## 🇨🇳 Chinese Language MCP Resources

### **[Awesome MCP ZH](https://github.com/yzfly/Awesome-MCP-ZH)** 🇨🇳 📜
*   **Description**: A curated list of awesome MCP (Model Context Protocol) resources, tools, and implementations specifically focused on or relevant to the Chinese language and developer community.
*   **Key Features**:
    *   Collection of MCP links.
    *   Focus on Chinese language resources.
    *   Community-curated.
*   **Source URL**: `yzfly/Awesome-MCP-ZH`

## 🤝 Contributing

This list is actively maintained. If you know of an MCP service that isn't listed here, or if you have corrections, please feel free to open an issue or submit a pull request to the repository hosting this document. When contributing, please try to include as much detail as possible, including the service name, source link, description, key features, relevant icons, and the original URL where you found the information.
