# Technical Context

## Technology Stack

### Core Technologies
1. **Python Environment**
   - Python 3.11 or higher
   - uv package installer
   - Virtual environment management

2. **Browser Technology**
   - Chrome/Chromium browser
   - Chrome DevTools Protocol
   - Browser debugging capabilities

3. **Development Tools**
   - Claude Desktop integration
   - MCP Inspector for debugging
   - Environment configuration management

## Dependencies

### Primary Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| browser-use | ==0.1.19 | Core browser automation capabilities |
| fastapi | >=0.115.6 | API server framework |
| fastmcp | >=0.4.1 | MCP server framework |
| instructor | >=1.7.2 | Structured output prompting |
| langchain | >=0.3.14 | LLM framework integration |

### AI/ML Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| langchain-google-genai | >=2.1.1 | Google AI integration |
| langchain-openai | >=0.2.14 | OpenAI model integration |
| langchain-ollama | >=0.2.2 | Local model execution |
| openai | >=1.59.5 | OpenAI API client |

### Utility Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| Pillow | >=10.1.0 | Image processing |
| python-dotenv | >=1.0.1 | Environment management |
| pydantic | >=2.10.5 | Data validation |
| pyperclip | >=1.9.0 | Clipboard operations |
| uvicorn | >=0.22.0 | ASGI server |

## Technical Requirements

### Environment Configuration
```bash
# API Integration
ANTHROPIC_API_KEY=required
OPENAI_API_KEY=optional
GOOGLE_API_KEY=optional
AZURE_OPENAI_API_KEY=optional

# Browser Settings
CHROME_PATH=optional
CHROME_USER_DATA=optional
CHROME_DEBUGGING_PORT=9222
CHROME_DEBUGGING_HOST=localhost
CHROME_PERSISTENT_SESSION=false

# Model Configuration
MCP_MODEL_PROVIDER=anthropic
MCP_MODEL_NAME=claude-3-5-sonnet-20241022
MCP_TEMPERATURE=0.3
MCP_MAX_STEPS=30
MCP_USE_VISION=true
MCP_MAX_ACTIONS_PER_STEP=5
```

### Development Setup
1. **Repository Setup**
   ```bash
   git clone https://github.com/JovaniPink/mcp-browser-use.git
   cd mcp-browser-use
   ```

2. **Environment Setup**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   uv sync
   ```

3. **Server Launch**
   ```bash
   uv run mcp-browser-use
   ```

## Technical Constraints

### System Requirements
1. **Operating Systems**
   - Linux (primary support)
   - macOS (primary support)
   - Windows (primary support)
   - Docker/WSL (testing needed)

2. **Browser Requirements**
   - Chrome/Chromium installation
   - Debugging port availability
   - User data directory access

3. **Network Requirements**
   - Port 9222 available for Chrome debugging
   - API endpoint accessibility
   - Stable internet connection

### Security Considerations
1. **Browser Security**
   - Controlled browser access
   - Sandbox limitations
   - User data protection

2. **API Security**
   - Secure key management
   - Rate limiting
   - Access control

3. **Data Security**
   - Session data handling
   - Cookie management
   - State persistence

## Development Patterns

### Code Organization
```
src/
├── mcp_browser_use/
│   ├── agent/
│   │   ├── custom_agent.py
│   │   ├── custom_massage_manager.py
│   │   └── custom_prompts.py
│   ├── browser/
│   │   ├── config.py
│   │   └── custom_browser.py
│   ├── controller/
│   │   └── custom_controller.py
│   └── utils/
│       └── agent_state.py
```

### Testing Approach
1. Unit testing with standard Python tools
2. Integration testing for browser control
3. End-to-end testing for full workflows
4. Security testing for browser integration

### Documentation Standards
1. Inline code documentation
2. API documentation
3. Setup and configuration guides
4. Security considerations
5. Contribution guidelines

## Development Tools

### Primary Tools
1. Visual Studio Code
2. Chrome DevTools
3. MCP Inspector
4. Python debugging tools

### Testing Tools
1. Python testing framework
2. Browser automation testing
3. Security scanning tools
4. Performance monitoring

### Deployment Tools
1. Git version control
2. Package management (uv)
3. Environment management
4. Continuous integration
