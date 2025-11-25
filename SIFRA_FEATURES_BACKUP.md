# SIFRA - Complete System Backup Documentation
**Backup Date**: November 26, 2025

---

## 📋 Executive Summary

SIFRA is an advanced, full-stack voice AI agent application integrating real-time voice communication, intelligent memory management, system automation, and multi-modal user interfaces. The project Dconsists of a modern React/Next.js frontend with TypeScript and a sophisticated Python backend powered by LiveKit and Google's Generative AI.

---

## 🎯 Major Features Overview

### Core Capabilities
1. **Real-Time Voice Agent Interaction** - Bidirectional voice communication with AI
2. **Multi-Modal Communication** - Voice, text chat, and transcription support
3. **Video & Screen Sharing** - Camera streaming and desktop sharing
4. **Persistent Memory System** - Conversation history and user profiles
5. **System Automation** - Keyboard/mouse control and file operations
6. **Web Integration** - Google search, weather data, and web services
7. **Customizable UI** - Dark/light themes, branding, and responsive design
8. **Real-Time Transcription** - Live speech-to-text conversion
9. **Advanced AI Reasoning** - Extended thinking capability for complex queries
10. **Error Handling & Notifications** - Toast-based user feedback system

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   SIFRA Full Stack System                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────┐       ┌──────────────────────┐  │
│  │  Frontend Layer      │       │  Backend Layer       │  │
│  │  (React/Next.js)     │◄─────►│  (Python)            │  │
│  ├──────────────────────┤       ├──────────────────────┤  │
│  │ • TypeScript UI      │       │ • LiveKit Agents     │  │
│  │ • Tailwind CSS       │       │ • Google Realtime    │  │
│  │ • Radix UI Comps     │       │ • Memory Management  │  │
│  │ • Motion.js Anims    │       │ • System Tools       │  │
│  │ • Real-time Updates  │       │ • Web Services       │  │
│  └──────────────────────┘       └──────────────────────┘  │
│           │                              │                 │
│           └──────────────────┬───────────┘                 │
│                              │                             │
│                    ┌─────────▼──────────┐                 │
│                    │  LiveKit Protocol   │                 │
│                    │  Real-time Media    │                 │
│                    └────────────────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 💻 Frontend Architecture (React/Next.js)

### Technology Stack
- **Framework**: Next.js 15.5.2 (Turbopack enabled)
- **Runtime**: React 19.0.0
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4 + PostCSS
- **UI Library**: Radix UI (components, hooks)
- **Animation**: Motion.js v12.16.0
- **Icons**: Phosphor Icons React
- **Notifications**: Sonner (toast library)
- **Theme**: next-themes v0.4.6
- **Media Client**: livekit-client v2.15.5
- **LiveKit Components**: @livekit/components-react v2.9.14
- **Utilities**: clsx, class-variance-authority, tailwind-merge

### Frontend Directory Structure
```
agent-starter-react/
├── app/
│   ├── (app)/                    # Route group
│   │   ├── layout.tsx            # App layout
│   │   ├── page.tsx              # Main page
│   │   └── opengraph-image.tsx   # OG image generation
│   ├── api/
│   │   └── connection-details/   # Token generation endpoint
│   │       └── route.ts
│   ├── components/               # App-level components
│   │   ├── Container.tsx
│   │   ├── Tabs.tsx
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── base/page.tsx
│   │   └── livekit/page.tsx
│   ├── globals.css               # Global styles
│   ├── layout.tsx                # Root layout
│   └── fonts/                    # Font files
│
├── components/
│   ├── livekit/                  # LiveKit-specific components
│   │   ├── agent-control-bar/    # Control panel for agent
│   │   │   ├── agent-control-bar.tsx
│   │   │   └── hooks/
│   │   │       ├── use-agent-control-bar.ts
│   │   │       └── use-publish-permissions.ts
│   │   ├── chat/                 # Chat system
│   │   │   ├── chat-entry.tsx
│   │   │   ├── chat-input.tsx
│   │   │   ├── chat-message-view.tsx
│   │   │   └── hooks/utils.ts
│   │   ├── agent-tile.tsx        # Agent display
│   │   ├── avatar-tile.tsx       # Avatar display
│   │   ├── device-select.tsx     # Audio device picker
│   │   ├── media-tiles.tsx       # Video/screen display
│   │   ├── track-toggle.tsx      # Media track controls
│   │   └── video-tile.tsx        # Video display
│   │
│   ├── ui/                       # Reusable UI components
│   │   ├── alert.tsx
│   │   ├── button.tsx
│   │   ├── select.tsx
│   │   ├── sonner.tsx
│   │   └── toggle.tsx
│   │
│   ├── app.tsx                   # Main app component
│   ├── provider.tsx              # Context providers
│   ├── session-view.tsx          # Active session view
│   ├── alert-toast.tsx           # Toast alert system
│   ├── theme-toggle.tsx          # Dark/light mode toggle
│   └── welcome.tsx               # Welcome screen
│
├── hooks/
│   ├── useChatAndTranscription.ts    # Merged messages hook
│   ├── useConnectionDetails.ts       # Token management
│   └── useDebug.ts                   # Debug mode hook
│
├── lib/
│   ├── types.ts                  # TypeScript interfaces
│   └── utils.ts                  # Utility functions
│
├── public/                       # Static assets
│   └── [logos, images]
│
├── Configuration Files
│   ├── app-config.ts             # App configuration
│   ├── package.json              # Dependencies
│   ├── tsconfig.json             # TypeScript config
│   ├── next.config.ts            # Next.js config
│   ├── tailwind.config.mjs        # Tailwind config
│   ├── postcss.config.mjs         # PostCSS config
│   ├── eslint.config.mjs          # ESLint rules
│   ├── components.json            # Shadcn/ui config
│   └── pnpm-lock.yaml             # Dependency lock file
│
└── Dev Files
    ├── README.md
    ├── TEMPLATE.md
    ├── renovate.json              # Auto-dependency updates
    ├── taskfile.yaml              # Task definitions
    └── LICENSE
```

### Frontend Configuration
```typescript
// app-config.ts - Key Configuration
{
  companyName: 'Sifra',
  pageTitle: 'Sifra',
  pageDescription: 'A voice agent built with Sifra',
  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,
  logo: '/lk-logo.svg',
  logoDark: '/lk-logo-dark.svg',
  accent: '#0075f2ff',              // Light mode: Blue
  accentDark: '#1fd5f9',            // Dark mode: Cyan
  startButtonText: 'Talk To Sifra',
  agentName: undefined
}
```

### Key Frontend Features
- **Real-Time Chat**: Live message display with transcriptions
- **Media Controls**: Mic, camera, screen share toggles
- **Device Management**: Audio input/output device selection
- **Audio Visualization**: BarVisualizer for audio levels
- **Smooth Animations**: Motion.js transitions and micro-interactions
- **Responsive Design**: Mobile-first, desktop-optimized layout
- **Theme Support**: Light/dark mode with system detection
- **Error Boundaries**: Toast notifications for errors
- **Session Management**: Welcome → Session → Disconnect flow

---

## 🐍 Backend Architecture (Python/LiveKit)

### Technology Stack
- **Runtime**: Python 3.x with async/await support
- **LiveKit SDK**: livekit-agents v1.2.1
- **LLM**: Google Generative AI (Realtime model with voice)
- **Speech-to-Text**: Google Cloud Speech v2.33.0
- **Text-to-Speech**: Google Cloud Text-to-Speech v2.27.0
- **Conversation**: LangChain v0.3.26 + LangChain Community
- **System Control**: PyAutoGUI v0.9.54 (keyboard/mouse)
- **Search**: DuckDuckGo Search integration
- **Audio Processing**: Noise cancellation (BVC), sounddevice
- **Database**: SQLAlchemy v2.0.41 + aiofiles
- **HTTP**: aiohttp v3.12.14
- **Utilities**: pydantic v2.11.7, python-dotenv v1.1.1

### Backend Directory Structure
```
SIFRA_code/
├── Core Agent Files
│   ├── agent.py                  # Main agent entrypoint
│   ├── memory_loop.py            # Conversation memory processor
│   ├── memory_store.py           # Memory database layer
│   └── .env                      # Environment variables
│
├── Prompt Management
│   ├── SIFRA_prompts.py          # Main system prompts
│   ├── Jarvis_prompts.py         # Alternate prompt set
│   └── SIFRA_reasoning.py        # Thinking capability logic
│
├── System Integration Tools
│   ├── keyboard_mouse_CTRL.py    # PyAutoGUI wrapper
│   ├── SIFRA_window_CTRL.py      # Window management
│   ├── SIFRA_file_opener.py      # File operations
│   ├── SIFRA_get_weather.py      # Weather API integration
│   └── SIFRA_google_search.py    # Web search integration
│
├── Data Storage
│   ├── conversations/
│   │   ├── Hamid_22_memory.json  # User conversation store
│   │   └── old_backups/          # Archived conversations
│   │       ├── *.json.archived
│   │       ├── *.json.bak.archived
│   │       └── *.json.old.archived
│   │
│   ├── KMS/                      # Knowledge Management System
│   │   └── logs/                 # System logs
│   │
│   └── control_log.txt           # Operation log
│
├── Dependencies
│   ├── requirements.txt           # Python package list
│   └── __pycache__/              # Python cache
│
└── Virtual Environment
    └── .venv/                    # Python virtual environment
```

### Backend Configuration
```python
# Key Backend Settings (agent.py)
REPLY_TIMEOUT = 30                # Response timeout in seconds
MODEL_VOICE = "kore"              # Google Realtime voice
NOISE_CANCELLATION = BVC()         # Background Voice Cancellation
LLM = google.beta.realtime.RealtimeModel(voice="kore")
```

### Core Backend Components

#### 1. **Agent System (agent.py)**
- Main entrypoint for LiveKit agent
- Handles real-time voice processing
- Manages session lifecycle
- Integrates with Google Realtime LLM
- Preemptive response generation

#### 2. **Memory Management**
- **memory_loop.py**: Extracts and processes conversations
- **memory_store.py**: Persistent storage layer
- User-specific memory files (JSON)
- Automatic conversation backup
- Historical version management

#### 3. **Prompt System**
- **SIFRA_prompts.py**: Core system instructions
- **Jarvis_prompts.py**: Alternative personality
- Dynamic prompt injection
- Role-based instructions
- Custom thinking protocols

#### 4. **AI Reasoning**
- **SIFRA_reasoning.py**: Extended thinking capability
- Complex problem decomposition
- Multi-step reasoning chains
- Tool integration logic

#### 5. **System Tools**
- **keyboard_mouse_CTRL.py**: Automate user input
  - Type text, click mouse
  - Keyboard shortcuts
  - Movement tracking
  
- **SIFRA_window_CTRL.py**: Window management
  - List open windows
  - Switch applications
  - Window positioning
  
- **SIFRA_file_opener.py**: File operations
  - Open documents
  - File path resolution
  - Batch operations
  
- **SIFRA_get_weather.py**: Weather integration
  - Current conditions
  - Forecast data
  - Location-based queries
  
- **SIFRA_google_search.py**: Web search
  - Query processing
  - Result parsing
  - Information extraction

---

## 🔄 LiveKit Workflow & Real-Time Communication

### Connection Flow
```
1. User clicks "Talk To Sifra" (Frontend)
   ↓
2. Request token from /api/connection-details (Frontend)
   ↓
3. Server generates JWT token (Backend API)
   ↓
4. Frontend connects to LiveKit URL with token
   ↓
5. Python agent joins same room
   ↓
6. Bidirectional audio/video established
   ↓
7. Real-time communication begins
```

### LiveKit Components
- **Room**: Isolated session container
- **Participants**: Frontend user + Python agent
- **Tracks**: Audio (mic/speaker), Video (camera/screen)
- **Messages**: Chat messages via LiveKit protocol
- **Events**: Connection state, media events

### Audio Pipeline
```
User Microphone
    ↓
WebRTC Audio Stream (encrypted)
    ↓
LiveKit Room
    ↓
Python Agent (Receives)
    ↓
Google Speech-to-Text (optional)
    ↓
LLM Processing
    ↓
Response Generation
    ↓
Text-to-Speech (optional)
    ↓
Audio Stream Back
    ↓
User Speaker
```

### Session States
- **Disconnected**: No active connection
- **Connecting**: Room connection in progress
- **Connected**: Active LiveKit room
- **Agent Listening**: Ready for user input
- **Agent Thinking**: Processing query
- **Agent Speaking**: Generating response
- **Disconnected**: Session ended

---

## 📡 API Integrations

### 1. **LiveKit Services**
- **Room Management**: Create/delete rooms
- **Access Tokens**: JWT generation
- **Participant Tracking**: Monitor agent/user
- **Recording**: Optional session recording
- **Analytics**: Connection metrics

### 2. **Google Generative AI**
- **Realtime LLM**: google.beta.realtime.RealtimeModel
- **Speech Recognition**: Google Cloud Speech-to-Text
- **Speech Synthesis**: Google Cloud Text-to-Speech
- **Voice Models**: Kore (selected for SIFRA)

### 3. **External Services**
- **Weather API**: Real-time weather data
- **Search API**: DuckDuckGo search integration
- **Web Scraping**: Data extraction

### 4. **System APIs**
- **PyAutoGUI**: Desktop automation
- **PyGetWindow**: Window management
- **PyScreeze**: Screenshot capture
- **Pynput**: Low-level input control

---

## 🧠 Memory System Architecture

### Storage Structure
```
conversations/
├── Hamid_22_memory.json          # Active user profile
│   ├── user_id: "Hamid_22"
│   ├── conversations: [...]      # Message history
│   ├── context: {...}            # Accumulated context
│   └── metadata: {...}           # Timestamps, etc.
│
└── old_backups/
    ├── Gaurav_22_memory.json.archived
    ├── Gaurav_22_memory.json.bak.archived
    └── Gaurav_22_memory.json.old.archived
```

### Memory Features
- **Per-User Profiles**: Separate memory for each user
- **Conversation History**: Full chat/transcription logs
- **Context Accumulation**: Building knowledge base
- **Automatic Extraction**: Periodic memory updates
- **Backup Versioning**: Multiple save points
- **Archive System**: Old conversations preserved

### Memory Extraction Process
1. Extract key information from current session
2. Process with memory loop handler
3. Update user's memory file
4. Create backup copy
5. Maintain version history

---

## 🛠️ Automation Capabilities

### System-Level Control
- **Keyboard Automation**: Type, hotkeys, special keys
- **Mouse Control**: Movement, clicks, drag & drop
- **Window Management**: List, focus, resize windows
- **Application Launching**: Start programs via command

### File Operations
- **File Opening**: Launch files with default apps
- **Directory Navigation**: Traverse file system
- **File Reading**: Text/content extraction
- **Batch Operations**: Process multiple files

### Information Retrieval
- **Web Search**: Query and results parsing
- **Weather Data**: Current and forecast
- **Real-Time Data**: Live information feeds

### Interactive Capabilities
- **Form Filling**: Automated data entry
- **System Navigation**: Menu interaction
- **Screenshot Capture**: Desktop recording
- **Clipboard Operations**: Copy/paste automation

---

## 📦 Project Dependencies Summary

### Frontend Dependencies (51 packages)
- LiveKit: @livekit/components-react, livekit-client, @livekit/protocol
- UI: @radix-ui/* (5 packages), sonner, motion
- Styling: tailwindcss, tailwind-merge, class-variance-authority
- Utils: jose, mime, clsx, buffer-image-size
- Dev Tools: TypeScript, ESLint, Prettier, Tailwind plugins

### Backend Dependencies (103 packages)
- **AI/ML**: google-genai, google-cloud-speech, google-cloud-texttospeech, langchain
- **LiveKit**: livekit, livekit-agents, livekit-api, livekit-plugins-google
- **Audio**: sounddevice, livekit-plugins-noise-cancellation
- **System**: pyautogui, pygetwindow, pyscreeze, pynput, pywin32
- **Web**: aiohttp, httpx, requests, duckduckgo-search
- **Database**: sqlalchemy, aiofiles
- **Utils**: pydantic, python-dotenv, click, colorama, tqdm

---

## 🔐 Security & Environment

### Environment Variables (Required)
```env
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
LIVEKIT_URL=https://your-livekit-server-url
GOOGLE_API_KEY=your_google_api_key
```

### Authentication Flow
1. User initiates session
2. Frontend requests token from /api/connection-details
3. Backend validates request
4. Server generates JWT with LiveKit credentials
5. Frontend uses token to connect to LiveKit
6. Python agent authenticates separately
7. Both join same isolated room

### Data Privacy
- Room-based isolation per session
- Token expiration enforcement
- No persistent user data (unless opted-in)
- Memory system for conversation context

---

## 🚀 Development Workflow

### Package Manager
- **pnpm**: Package manager (v9.15.9)
- Faster than npm, uses monorepo patterns

### Development Scripts
```bash
# Frontend + Backend concurrently
pnpm dev              # Runs next:dev + backend

# Frontend only
pnpm next:dev         # Next.js dev server with Turbopack

# Backend only
pnpm backend          # Python agent.py in dev mode

# Building & Deployment
pnpm build            # Next.js production build
pnpm start            # Start production server

# Code Quality
pnpm lint             # ESLint check
pnpm format           # Prettier formatting
pnpm format:check     # Check formatting
```

### Development Stack
- **Hot Reload**: Turbopack for instant updates
- **Concurrent Run**: Runs frontend + backend simultaneously
- **Live Updates**: Changes reflected immediately
- **Type Checking**: TypeScript compilation
- **Code Formatting**: Prettier + ESLint

---

## 📊 Project Metrics

### Frontend
- **Lines of React/TypeScript**: ~2,000+
- **Components**: 25+ custom components
- **Hooks**: 3 main custom hooks
- **CSS**: Tailwind utility classes
- **Pages**: Dynamic routing with Next.js

### Backend
- **Python Files**: 10+ core modules
- **Lines of Python**: ~3,000+
- **LLM Integration**: Google Realtime
- **Tools**: 5+ automation tools
- **Memory Profiles**: Per-user persistent storage

### Overall
- **Total Size**: ~500MB (with node_modules + venv)
- **Dependencies**: 150+ total packages
- **Supported Platforms**: Web (any browser), Desktop OS integration
- **Scalability**: Multi-room support, concurrent users

---

## 🎯 Use Cases & Applications

### Personal Assistant
- Daily scheduling and reminders
- Information lookup and research
- System automation and control
- Calendar and note management

### Customer Service
- Chat and voice support
- Issue resolution with web search
- Document/file retrieval
- Knowledge base integration

### System Administration
- Remote system control
- Automated task execution
- System monitoring
- Batch operations

### Accessibility
- Voice-first interface for disabled users
- Hands-free system control
- Audio output for visual content
- Voice-to-text documentation

### Research & Development
- Conversation analysis
- Real-time transcription
- Data extraction automation
- Multi-modal interaction study

---

## 🔄 Version Control & Backup

### Repository Structure
```
SIFRA v-3 - Copy/
├── agent-starter-react/     # Frontend application
├── SIFRA_code/              # Backend application
├── APP_FEATURES.md          # Feature documentation
└── SIFRA_FEATURES_BACKUP.md # This backup file
```

### Backup Strategy
- **Database Backups**: Memory files in /conversations/
- **Version Control**: Git repository recommended
- **Full Backups**: Periodic complete project copies
- **Archived History**: old_backups/ folder

---

## 📝 Maintenance Notes

### Regular Maintenance
- Update npm/pnpm dependencies monthly
- Update Python packages quarterly
- Review memory files for cleanup
- Archive old conversations

### Performance Optimization
- Clear browser cache periodically
- Monitor memory usage (Python backend)
- Clean __pycache__ directories
- Optimize database queries

### Troubleshooting
- Check LiveKit connection status
- Verify API key validity
- Review error logs in control_log.txt
- Check system audio device availability

---

## ✅ Deployment Checklist

### Pre-Deployment
- [ ] Update environment variables
- [ ] Test all features locally
- [ ] Run linting & formatting
- [ ] Update dependencies
- [ ] Create database backups
- [ ] Test with production credentials

### Deployment
- [ ] Build frontend (pnpm build)
- [ ] Prepare Python environment
- [ ] Copy to production server
- [ ] Verify LiveKit connection
- [ ] Test agent initialization
- [ ] Monitor logs

### Post-Deployment
- [ ] Verify all features working
- [ ] Check error logs
- [ ] Monitor performance metrics
- [ ] Set up automated backups

---

## 📚 Additional Resources

### Documentation
- [LiveKit Documentation](https://docs.livekit.io/)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
- [Google Generative AI Docs](https://ai.google.dev/)
- [Python AsyncIO](https://docs.python.org/3/library/asyncio.html)

### Key Files for Reference
- `app-config.ts`: UI/branding configuration
- `agent.py`: Backend agent logic
- `SIFRA_prompts.py`: LLM instructions
- `memory_loop.py`: Memory processing
- `package.json`: Frontend dependencies

---

## 📄 File Summary

**Total Files**: 200+
**Total Directories**: 25+
**Node Modules**: ~2000 files
**Python Packages**: 103 dependencies
**Lock Files**: pnpm-lock.yaml, requirements.txt

---

**Backup Created**: November 26, 2025
**Project Status**: Active Development
**Version**: 3.0 (Copy)

---

*This documentation serves as a complete system backup reference for the SIFRA voice agent application.*
