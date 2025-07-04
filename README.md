# AI Resume Agent 🤖

A sophisticated personal career assistant designed to streamline and elevate the job application process. This agent leverages the power of Google's Gemini 2.5 Pro model to generate highly tailored, professional-grade application documents, including optimized resumes, compelling cover letters, and detailed Key Selection Criteria (KSC) responses.

## ✨ Key Features

### 📄 Resume Optimization
- **ATS-Friendly**: Generates resumes optimized for Applicant Tracking Systems
- **Job-Specific**: Tailors content to match job descriptions and requirements
- **Industry-Focused**: Specialized for Victorian community services sector (adaptable to other domains)

### ✉️ Cover Letter Generation
- **Personalized**: Creates compelling, professional cover letters
- **Company-Specific**: Tailors content to specific companies and roles
- **Professional Tone**: Maintains appropriate business communication standards

### 📝 KSC Response Generation
- **STAR Method**: Uses Situation, Task, Action, Result framework
- **Evidence-Based**: Draws from personal experience database
- **Comprehensive**: Addresses all selection criteria thoroughly

### 🧠 Smart Personalization
- **Dynamic Templates**: Uses user profile data instead of hardcoded values
- **Experience Database**: Leverages `my_experiences.yaml` for relevant examples
- **Context-Aware**: Adapts to user's career goals and objectives

### ☁️ Modern Web Interface
- **Streamlit-Based**: Clean, intuitive web interface
- **Responsive Design**: Works on desktop and mobile devices
- **Real-Time Generation**: Live document generation with progress tracking
- **Download Ready**: Exports documents as `.docx` files

## 🏛️ Architecture Overview

### Core Design Principles

1. **Separation of Concerns**: Clean separation between data generation, templating, and presentation
2. **Structured AI Outputs**: Uses Pydantic schemas to ensure consistent, validated AI responses
3. **Template-Based Rendering**: Jinja2 templates for flexible document formatting
4. **User-Centric Configuration**: Eliminates hardcoded personal information
5. **Robust Error Handling**: Comprehensive exception management and retry logic

### Architecture Components

```
AI Resume Agent
├── 🤖 AI Layer (Gemini 2.5 Pro)
│   ├── Structured Output Generation
│   ├── Prompt Engineering
│   └── Response Validation
├── 📋 Data Layer
│   ├── User Profile Management
│   ├── Experience Database
│   └── Knowledge Base
├── 🎨 Presentation Layer
│   ├── Jinja2 Templates
│   ├── Document Generation
│   └── Export Functionality
└── 🌐 Interface Layer
    ├── Streamlit Web App
    ├── File Upload/Processing
    └── User Configuration
```

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Model** | Google Gemini 2.5 Pro | Content generation and optimization |
| **Web Framework** | Streamlit | User interface and interaction |
| **Data Validation** | Pydantic | Schema validation and settings management |
| **Templating** | Jinja2 | Document formatting and rendering |
| **File Processing** | PyPDF2, python-docx | PDF reading and Word document generation |
| **Configuration** | pydantic-settings, python-dotenv | Environment and user settings |
| **Testing** | Pytest | Comprehensive test coverage |
| **Retry Logic** | Tenacity | Robust API call handling |

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-resume-agent.git
   cd ai-resume-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

5. **Run the application**
   ```bash
   streamlit run src/web/streamlit_app.py
   ```

## 📁 Project Structure

```
ai-resume-agent/
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .env.example
├── 📄 .gitignore
├── 📁 data/
│   ├── 📁 input/          # User uploaded files
│   └── 📁 output/         # Generated documents
├── 📁 src/
│   ├── 📁 ai_resume_agent/
│   │   ├── 📄 agent.py                 # Main orchestrator
│   │   ├── 📄 prompt_builder.py        # Prompt management
│   │   ├── 📄 resume_optimizer.py      # Resume optimization logic
│   │   ├── 📄 cover_letter.py          # Cover letter generation
│   │   ├── 📄 ksc_response.py          # KSC response generation
│   │   ├── 📁 schemas/
│   │   │   └── 📄 models.py            # Pydantic data models
│   │   ├── 📁 prompts/
│   │   │   └── 📄 Prompts.yaml         # AI prompts
│   │   ├── 📁 utils/
│   │   │   ├── 📄 config.py            # Configuration management
│   │   │   ├── 📄 exceptions.py        # Custom exceptions
│   │   │   ├── 📄 file_processor.py    # File handling
│   │   │   ├── 📄 llm.py               # AI model interface
│   │   │   └── 📄 Logger.py            # Logging utilities
│   │   └── 📁 knowledge/
│   │       ├── 📄 loader.py            # Knowledge loading
│   │       └── 📁 sources/
│   │           └── 📄 my_experiences.yaml  # Personal experience database
│   ├── 📁 templates/
│   │   ├── 📄 resume_template.md       # Resume template
│   │   ├── 📄 cover_letter_template.md # Cover letter template
│   │   └── 📄 ksc_template.md          # KSC template
│   └── 📁 web/
│       └── 📄 streamlit_app.py         # Web interface
└── 📁 tests/
    ├── 📄 conftest.py                  # Test configuration
    ├── 📄 test_agent.py                # Agent tests
    └── 📄 test_comprehensive.py        # Comprehensive test suite
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional - User Profile
USER_FULL_NAME=Your Full Name
USER_EMAIL=your.email@example.com
USER_PHONE=+61 400 000 000
USER_ADDRESS=Your Address

# Optional - App Settings
LOG_LEVEL=INFO
GEMINI_MODEL_NAME=gemini-2.5-pro
```

### User Profile Setup

The application includes a user profile system that eliminates hardcoded personal information:

1. **First-time Setup**: Configure your profile through the web interface
2. **Environment Variables**: Set USER_* variables in `.env` file
3. **Runtime Configuration**: Update profile settings in the sidebar

## 🧪 Testing

### Run All Tests
```bash
pytest
```

### Run Specific Test Categories
```bash
# Unit tests
pytest tests/test_agent.py -v

# Integration tests
pytest tests/test_comprehensive.py -v

# Test coverage
pytest --cov=src tests/
```

### Test Structure
- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end workflow testing
- **Mock Tests**: External service simulation
- **Configuration Tests**: Settings validation

## 🔧 Key Improvements Over Original Design

### 1. **User Profile System**
- ✅ Eliminates hardcoded personal information
- ✅ Dynamic template rendering
- ✅ Environment-based configuration
- ✅ Runtime profile updates

### 2. **Enhanced Error Handling**
- ✅ Custom exception classes
- ✅ Comprehensive error messages
- ✅ Retry logic for API calls
- ✅ Graceful degradation

### 3. **Improved Testing**
- ✅ Comprehensive test suite
- ✅ Mock-based testing
- ✅ Integration tests
- ✅ Configuration validation tests

### 4. **Better Configuration Management**
- ✅ Pydantic-based settings
- ✅ Environment variable validation
- ✅ Type checking and validation
- ✅ Singleton pattern for settings

### 5. **Enhanced User Interface**
- ✅ Improved Streamlit interface
- ✅ Better error messages
- ✅ Progress tracking
- ✅ File validation
- ✅ Responsive design

### 6. **Dependency Management**
- ✅ Version-pinned requirements
- ✅ Security considerations
- ✅ Compatibility testing
- ✅ Minimal dependency footprint

## 🚀 Deployment

### Local Development
```bash
streamlit run src/web/streamlit_app.py
```

### Streamlit Community Cloud
1. Push code to GitHub
2. Connect to Streamlit Community Cloud
3. Set environment variables in app settings
4. Deploy pointing to `src/web/streamlit_app.py`

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
COPY data/ data/

EXPOSE 8501
CMD ["streamlit", "run", "src/web/streamlit_app.py", "--server.address=0.0.0.0"]
```

## 🔐 Security Considerations

- **API Key Management**: Never commit API keys to version control
- **Input Validation**: File upload validation and sanitization
- **Error Handling**: Secure error messages without sensitive data exposure
- **Dependencies**: Regular security updates and vulnerability scanning

## 📊 Performance Considerations

- **Caching**: Knowledge base and configuration caching
- **Retry Logic**: Exponential backoff for API calls
- **File Processing**: Efficient PDF text extraction
- **Memory Management**: Proper resource cleanup

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini team for the powerful AI model
- Streamlit team for the excellent web framework
- The open-source community for the underlying technologies

## 📞 Support

For questions, issues, or contributions, please:
- Open an issue on GitHub
- Check the documentation
- Review the test suite for examples

---

*Built with ❤️ for job seekers everywhere*