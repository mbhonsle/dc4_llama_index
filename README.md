# 🚀 DC4 LlamaIndex: Salesforce Data Cloud Integration

> **Unlock the power of your Salesforce Data Cloud with intelligent vector search and RAG capabilities!**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.13.0+-green.svg)](https://docs.llamaindex.ai/)

## 🌟 What is DC4 LlamaIndex?

DC4 LlamaIndex is a powerful Python library that seamlessly bridges **Salesforce Data Cloud** with **LlamaIndex**, enabling you to build sophisticated RAG (Retrieval-Augmented Generation) applications using your Salesforce data. Transform your customer data into intelligent, searchable knowledge that powers AI-driven insights and personalized experiences.

## ✨ Key Features

- 🔗 **Native Data Cloud Integration**: Direct connection to Salesforce Data Cloud's Query Service API
- 🧠 **Vector Search Capabilities**: Leverage Data Cloud's built-in vector search for semantic similarity
- 📊 **Intelligent Data Loading**: Custom LlamaIndex reader for seamless data ingestion
- 🔐 **Secure Authentication**: Built-in Salesforce authentication using `pydc-auth`
- ⚡ **High Performance**: Optimized for large-scale data processing and retrieval
- 🎯 **RAG-Ready**: Perfect foundation for building retrieval-augmented generation applications

## 🏗️ Architecture

```
Salesforce Data Cloud → Query Service API → DC4 LlamaIndex → LlamaIndex Framework → Your RAG Application
```

The library provides a custom `DataCloudDataLoader` that:
1. Connects to Salesforce Data Cloud via the Query Service API
2. Executes vector search queries against your embedding bundles
3. Returns structured documents ready for LlamaIndex processing
4. Enables semantic search across your Salesforce data

## 🚀 Quick Start

### Installation

```bash
pip install dc-llama-index
```

### Basic Usage

```python
from datacloud.readers.query_svc import QueryServiceClient
from main.datacloud_data_loader import DataCloudDataLoader
from llama_index.core import VectorStoreIndex

# Initialize the Data Cloud loader
loader = DataCloudDataLoader(
    db_path="your_data_cloud_instance",
    chunk_table="your_chunk_table",
    vector_table="your_vector_table", 
    text_column="your_text_column"
)

# Load documents from Data Cloud
documents = loader.load_data()

# Create a vector index
index = VectorStoreIndex.from_documents(documents)

# Build a query engine
query_engine = index.as_query_engine()

# Query your Salesforce data!
response = query_engine.query("What are the top customer concerns this quarter?")
print(response)
```

### Advanced Vector Search

```python
# Direct Query Service API usage
client = QueryServiceClient()

# Execute custom SQL with vector search
query_data = {
    "sql": """
    SELECT 
        index.RecordId__c,
        index.score__c,
        chunk.Chunk__c
    FROM 
        vector_search(TABLE(your_vector_table), 'your_text_column', 'search query', 10) AS index
    JOIN 
        your_chunk_table AS chunk
    ON 
        index.RecordId__c = chunk.RecordId__c
    """
}

results = client.read_data(query_data)
```

## 🔧 Configuration

Set up your environment variables:

```bash
# Salesforce authentication
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password
SALESFORCE_SECURITY_TOKEN=your_security_token
SALESFORCE_DOMAIN=your_domain
```

## 🎯 Use Cases

- **🤖 Intelligent Customer Support**: Build AI assistants that understand your customer data
- **📈 Sales Intelligence**: Create smart sales tools with real-time customer insights
- **🎨 Marketing Personalization**: Develop targeted campaigns using customer behavior data
- **📊 Business Analytics**: Generate insights from your Salesforce data using natural language
- **🔍 Knowledge Management**: Build searchable knowledge bases from your CRM data

## 🛠️ Requirements

- Python 3.12+
- Salesforce Data Cloud account with Query Service API access
- LlamaIndex 0.13.0+
- Valid Salesforce authentication credentials

## 📚 Dependencies

- `llama-index>=0.13.0` - Core LlamaIndex framework
- `pydc-auth>=0.1.3` - Salesforce Data Cloud authentication
- `httpx>=0.28.1` - HTTP client for API calls
- `pydantic>=2.7.3` - Data validation and settings
- `python-dotenv>=1.0.0` - Environment variable management

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LlamaIndex](https://docs.llamaindex.ai/) for the amazing RAG framework
- [Salesforce Data Cloud](https://www.salesforce.com/data/) for the powerful data platform
- The open-source community for inspiration and support

---

**Ready to transform your Salesforce data into intelligent insights?** 🚀

[Get Started Now](#quick-start) | [View Documentation](#configuration) | [Report Issues](https://github.com/mbhonsle/dc4_llama_index/issues)