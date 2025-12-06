# Assistant Intelligent ENSAM Meknès

**Authors:** AMLLAL Amine & HAJJI Mohamed  
**Supervisor:** M. BARBARA Idriss  
**Academic Year:** 2025-2026  
**Institution:** École Nationale Supérieure d'Arts et Métiers Meknès, Université Moulay Ismail

---

## 📋 Overview

The **Assistant Intelligent ENSAM Meknès** is an AI-powered conversational agent designed to centralize dispersed academic information and provide instant, accurate responses to students, faculty, and administrative staff. By leveraging advanced Natural Language Understanding (NLU) and a comprehensive knowledge base, this assistant reduces administrative workload and alleviates student stress related to accessing critical academic resources.

### Core Problem Solved

Students and staff at ENSAM Meknès often face challenges in accessing fragmented information across multiple sources—contact directories, course schedules, internship opportunities, curriculum details, and career statistics. This intelligent assistant consolidates these resources into a single, accessible, 24/7 conversational interface.

---

## 🏗️ Architecture Overview

The system is built on **Botpress Cloud**, a sophisticated conversational AI platform that handles natural language processing, context management, and knowledge retrieval. The architecture follows this workflow:

```
User Query → Botpress Cloud (NLU Engine) → Knowledge Base Search → Contextual Response Generation → API Response
```

### Botpress: The Intelligence Core

Botpress serves as the brain of the system, providing:

- **Natural Language Understanding (NLU):** Interprets user intent from queries in natural language (French/English).
- **Context Management:** Maintains conversation state to provide coherent, multi-turn dialogues.
- **Knowledge Base Integration:** Dynamically searches and extracts relevant information from structured PDF documents.
- **REST API:** Exposes webhooks for seamless integration with client applications.

---

## 📚 Knowledge Base Configuration

The assistant's intelligence is powered by **6 carefully curated PDF documents** that form the core knowledge base. Each document serves a specific domain of academic information:

| Document | Content Description |
|----------|---------------------|
| `CONTACTS_profs.pdf` | Complete directory of professor emails, office locations, and departmental affiliations |
| `Filières.pdf` | Detailed descriptions of engineering majors: GI (Génie Industriel), IATD (Ingénierie Avancée et Technologies Digitales), GEPS (Génie Énergétique et Procédés Spéciaux) |
| `Programme_reforme.pdf` | Curriculum structure, ECTS credit distribution, course modules, and evaluation methodologies |
| `Document_Insertion.pdf` | Alumni career statistics, employment rates, industry sectors, and market insertion data |
| Additional course materials | Google Drive links to syllabus documents, lecture notes, and supplementary resources |
| Schedule information | Academic calendars, exam timetables, and semester planning |

### Knowledge Extraction Pipeline

1. **Query Reception:** User submits a natural language query through any connected client.
2. **Intent Classification:** Botpress NLU identifies the query category (contact lookup, program information, schedule retrieval, etc.).
3. **Document Search:** The system performs semantic search across the indexed PDF knowledge base.
4. **Context Assembly:** Relevant excerpts are extracted and assembled into a coherent context.
5. **Response Generation:** The AI generates a natural, conversational response based on the extracted information.
6. **API Delivery:** The response is returned as a JSON payload via the Botpress REST API.

---

## ✨ Key Features

### 🔍 **Instant Professor Contact Lookup**
Retrieve professor email addresses, office numbers, and departments in seconds. No more searching through outdated directories.

**Example Query:** *"Quel est l'email du professeur de mécanique des fluides?"*

### 🎓 **Engineering Major Information**
Get comprehensive details about the three engineering tracks:
- **GI (Génie Industriel):** Industrial processes, optimization, supply chain management.
- **IATD (Ingénierie Avancée et Technologies Digitales):** Digital transformation, AI, IoT, Industry 4.0.
- **GEPS (Génie Énergétique et Procédés Spéciaux):** Energy systems, sustainable processes, thermodynamics.

**Example Query:** *"Quelles sont les différences entre GI et IATD?"*

### 📖 **Curriculum and Program Details**
Access detailed information about:
- ECTS credit distribution across semesters
- Course modules and prerequisites
- Evaluation methodologies and grading systems
- Reform updates and curriculum changes

**Example Query:** *"Combien d'ECTS pour le module de programmation en 1ère année?"*

### 📊 **Alumni Career Statistics**
Explore insertion data including:
- Employment rates by graduating class
- Industry sector distribution
- Average starting salaries
- Top recruiting companies

**Example Query:** *"Quel est le taux d'insertion des diplômés ENSAM?"*

### 📁 **Course Material Access**
Direct links to Google Drive repositories containing:
- Course syllabi
- Lecture notes and presentations
- Lab manuals and project guidelines

**Example Query:** *"Où puis-je trouver les supports du cours de résistance des matériaux?"*

### ⏰ **24/7 Availability**
Unlike administrative offices, the assistant operates round-the-clock, providing immediate responses at any time.

---

## 🔗 Client Integration Example

While the Botpress backend handles all intelligence and knowledge retrieval, client applications can integrate with the assistant through the **Botpress REST API**. This section demonstrates a lightweight integration using **Streamlit** as a proof-of-concept user interface.

### Streamlit: A Simple API Client

Streamlit serves solely as a demonstration layer to showcase how external applications can consume the Botpress API. It is **not** a core component of the system architecture.

**Integration Flow:**
```
User Input (Streamlit UI) → HTTP POST Request → Botpress Webhook → JSON Response → Display in Streamlit
```

### Conceptual Integration Code

```python
import streamlit as st
import requests

# Botpress API Configuration
BOTPRESS_WEBHOOK_URL = "https://webhook.botpress.cloud/your-bot-id"

# Send user query to Botpress
def query_botpress(user_message):
    payload = {
        "type": "text",
        "text": user_message
    }
    response = requests.post(BOTPRESS_WEBHOOK_URL, json=payload)
    return response.json()

# Streamlit UI
st.title("Assistant ENSAM Meknès")
user_input = st.text_input("Posez votre question:")

if user_input:
    bot_response = query_botpress(user_input)
    st.write(bot_response["text"])
```

**Note:** This is a simplified example. Production implementations should include authentication, error handling, session management, and rate limiting.

---

## 🚀 Roadmap & Future Perspectives

### Short-Term Improvements
- **Real-Time Database Synchronization:** Automatically update the knowledge base when new documents are published by the administration.
- **Multi-Language Support:** Expand NLU capabilities to handle Arabic queries.
- **Analytics Dashboard:** Track frequently asked questions to identify gaps in documentation.

### Medium-Term Enhancements
- **Voice Recognition:** Enable voice-based queries for hands-free interaction.
- **Mobile Application:** Develop native Android/iOS apps for better accessibility.
- **Proactive Notifications:** Send alerts about exam schedules, deadline reminders, and important announcements.

### Long-Term Vision
- **Personalized Learning Assistant:** Provide tailored study recommendations based on student performance.
- **Integration with ERP Systems:** Direct connection to administrative databases for real-time enrollment, grade lookups, and transcript generation.
- **Multi-Campus Deployment:** Extend the system to other ENSAM campuses across Morocco.

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Conversational AI Platform** | Botpress Cloud |
| **Natural Language Understanding** | Botpress NLU Engine |
| **Knowledge Base** | PDF Document Indexing |
| **API Integration** | REST API (Webhooks) |
| **Demo Client** | Streamlit (Python) |
| **Deployment** | Botpress Cloud Hosting |

---

## 📖 Usage Guidelines

### For Students
1. Access the assistant through the designated client interface.
2. Type your question in natural language (French or English).
3. Receive instant, accurate responses with source citations.
4. Use follow-up questions to drill deeper into specific topics.

### For Administrators
1. Update knowledge base PDFs when curriculum or contact information changes.
2. Monitor conversation logs to identify frequently asked questions.
3. Review analytics to improve documentation quality.

---

## 👥 Credits & Acknowledgments

**Project Team:**
- **AMLLAL Amine** 
- **HAJJI Mohamed**

**Academic Supervision:**
- **M. BARBARA Idriss** – Project Supervisor

**Institution:**
- École Nationale Supérieure d'Arts et Métiers (ENSAM) Meknès
- Université Moulay Ismail

**Special Thanks:**
- ENSAM Administration for providing comprehensive academic documentation.
- Botpress Community for technical guidance and best practices.

---

## 📄 License

This project is developed for academic purposes at ENSAM Meknès. All rights reserved to the authors and the institution.

---

**Built with ❤️ for the ENSAM Meknès community**
