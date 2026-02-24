# SIFRA App - Complete Feature Analysis

## Overview
SIFRA is a comprehensive voice-based AI agent application built with a **Next.js/React frontend** and a **Python backend**. It leverages LiveKit for real-time communication and integrates multiple advanced AI capabilities.

---

## 🎯 Core Features

### 1. **Real-Time Voice Interaction**
- **LiveKit Integration**: Powered by LiveKit Agents for seamless voice communication
- **Bidirectional Audio**: Full-duplex voice conversation with the AI agent
- **Low-Latency Response**: Optimized for immediate user feedback
- **Audio Visualization**: Real-time audio level monitoring with BarVisualizer

### 2. **Multi-Modal Communication**

#### Chat System
- **Text-based Chat**: Send and receive messages from the AI agent
- **Chat Persistence**: Message history within session
- **Real-time Chat Updates**: Live message synchronization with agent responses
- **Chat UI**: Dedicated chat panel with scrollable message history

#### Transcription
- **Real-Time Transcription**: Live speech-to-text conversion
- **Merged Message Stream**: Combines transcriptions and chat messages seamlessly
- **Timestamp Tracking**: All messages timestamped for reference

#### Audio Processing
- **Microphone Control**: Toggle microphone on/off during sessions
- **Noise Cancellation**: BVC (Background Voice Cancellation) enabled
- **Audio Device Selection**: Choose from available input/output devices
- **Pre-Connect Buffer**: Optional buffering for improved performance

### 3. **Video Capabilities**
- **Camera Stream Support**: Enable/disable video input
- **Screen Sharing**: Share screen with the agent
- **Video Tile Display**: Shows agent avatar or video feed
- **Track Management**: Control video/audio tracks independently

### 4. **AI Agent Features**

#### LLM Integration
- **Google Realtime Model**: Uses Google's Kore voice-enabled LLM
- **Advanced Reasoning**: Custom thinking capability tool for complex analysis
- **Preemptive Generation**: Agent can proactively generate responses

#### Agent State Management
- **Connection States**: Connecting, Listening, Thinking, Speaking
- **Agent Availability Checking**: Validates agent initialization within 20 seconds
- **Session Management**: Automatic disconnect on agent unavailability

### 5. **Memory & Context System**

#### Memory Storage
- **Persistent Memory**: Stores conversations in JSON format
- **User Profiles**: Separate memory files per user (e.g., `Hamid_22_memory.json`)
- **Memory Extraction**: Automatically extracts and stores conversation context
- **Historical Backups**: Maintains archived versions of previous conversations

#### Context Awareness
- **Real-Time Context**: Agent receives current chat history
- **Conversation Context**: Understands previous exchanges within session
- **User Identification**: Associates conversations with specific users

### 6. **System Control & Automation**

#### Keyboard & Mouse Control
- **PyAutoGUI Integration**: Programmatic keyboard/mouse input
- **Window Management**: Control application windows
- **Automated Tasks**: Execute system-level automation

#### File Management
- **File Opening**: Open files based on agent commands
- **File Operations**: Programmatic file handling capabilities

### 7. **Web Integration**

#### Search Capabilities
- **Google Search**: Perform web searches via agent commands
- **DuckDuckGo Search**: Alternative search engine support
- **Search Result Processing**: Parse and return relevant information

#### Weather Integration
- **Real-Time Weather Data**: Fetch current weather information
- **Location-Based**: Weather retrieval for specified locations

### 8. **User Interface**

#### Customization
- **Branding**: Configurable company name and logo
- **Color Themes**: Customizable accent colors (light/dark)
- **UI Text**: Configurable button text and descriptions
- **Logo Management**: Support for dark mode logos

#### Theme Support
- **Light/Dark Mode**: System preference detection with next-themes
- **Smooth Transitions**: Motion-based animations for UI changes
- **Responsive Design**: Mobile-optimized interface

#### Session Flow
- **Welcome Screen**: Initial interface before connecting
- **Session View**: Main interaction interface
- **Control Bar**: Floating control panel with key actions
- **Device Selection**: Pick input/output devices before session

### 9. **Error Handling & Notifications**

#### Toast Notifications
- **Alert System**: Toast-based notifications using Sonner library
- **Error Messages**: Display connection/device errors
- **Status Updates**: Real-time status notifications
- **User Feedback**: Contextual error descriptions

#### Media Device Error Handling
- **Device Detection**: Identify media device issues
- **Error Recovery**: Graceful fallback on device errors
- **User Notification**: Alert users of audio/video problems

### 10. **Session Management**

#### Connection Lifecycle
- **Automatic Connection**: One-click session initiation
- **Token Management**: JWT-based authentication
- **Connection Details API**: Endpoint for obtaining tokens
- **Graceful Disconnection**: Proper cleanup on disconnect

#### Room Management
- **LiveKit Room Integration**: Secure room-based communication
- **Participant Tracking**: Monitor agent presence
- **Room Event Handling**: Listen for connection state changes

---

## 🛠️ Technology Stack

### Frontend
- **Framework**: Next.js 15.5.2 with React 19
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4 with custom animations
- **UI Components**: Radix UI components (Select, Toggle, Label, Scroll Area)
- **Animation**: Motion.js for smooth transitions
- **Icons**: Phosphor Icons library
- **Toast Notifications**: Sonner

### Backend
- **Runtime**: Python 3.x
- **LiveKit Integration**: LiveKit Agents SDK
- **LLM**: Google Generative AI (Realtime model)
- **Libraries**:
  - LangChain for conversation management
  - PyAutoGUI for system control
  - Google Cloud APIs (Speech-to-Text, Text-to-Speech)
  - DuckDuckGo Search
  - SQLAlchemy for database ORM

### Communication
- **Real-Time**: LiveKit protocol
- **WebRTC**: For media streaming
- **REST API**: For token retrieval

---

## 📱 UI Components

### Main Views
- **Welcome Screen**: Entry point with "Talk to Sifra" button
- **Session View**: Main conversation interface
- **Chat Panel**: Scrollable message history

### Control Elements
- **Agent Control Bar**: Contains all session controls
- **Track Toggles**: Microphone, camera, screen share controls
- **Device Select**: Audio input/output device picker
- **Chat Input**: Text message composition area
- **Disconnect Button**: End session control

### Display Components
- **Media Tiles**: Shows video feeds or agent avatar
- **Chat Messages**: Displays conversation history
- **Agent Tile**: Shows agent presence and status
- **Avatar Tile**: Displays agent avatar (if using virtual avatar)
- **Transcription Display**: Real-time speech-to-text output

---

## 🔄 Data Flow

```
User Input (Voice/Text)
    ↓
Frontend (React App)
    ↓
LiveKit Connection
    ↓
Python Agent Backend
    ↓
Google Realtime LLM + Tools
    ↓
Memory & Context System
    ↓
System Actions (File, Web, Control)
    ↓
Response Generation
    ↓
Frontend Display
```

---

## 🎨 Key Configurations

### App Configuration (app-config.ts)
```typescript
{
  companyName: 'Sifra',
  pageTitle: 'Sifra',
  pageDescription: 'A voice agent built with Sifra',
  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,
  startButtonText: 'Talk To Sifra',
}
```

### Environment Variables
```
LIVEKIT_API_KEY
LIVEKIT_API_SECRET
LIVEKIT_URL
```

---

## 🚀 Advanced Features

### Custom Tools
- **Thinking Capability**: Extended reasoning for complex queries
- **Memory Extraction**: Automatic knowledge base building
- **Custom Prompts**: Role-based prompts (Jarvis, Daily Protocol)

### Session Features
- **Preemptive Reply Generation**: Agent generates responses before user finishes speaking
- **20-second Initialization Timeout**: Ensures agent availability
- **Chat Open/Close Animation**: Smooth UI transitions

### Developer Features
- **Debug Mode**: Toggle debug information (in development)
- **Hot Reload**: Turbopack-enabled fast development
- **TypeScript Support**: Full type safety
- **Concurrent Development**: Run frontend + backend simultaneously

---

## 📊 Supported Interactions

### Voice
- ✅ Real-time speech recognition
- ✅ Natural language understanding
- ✅ Voice response generation
- ✅ Audio level visualization

### Text
- ✅ Chat message input
- ✅ Message history display
- ✅ Transcription display

### System Integration
- ✅ Window/application control
- ✅ Keyboard/mouse automation
- ✅ File operations
- ✅ Web search
- ✅ Weather lookup

### Media
- ✅ Camera video streaming
- ✅ Screen sharing
- ✅ Audio streaming
- ✅ Device selection

---

## 🔐 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Room-based Access**: Isolated conversation rooms
- **API Key Management**: Server-side credential handling
- **Environment-based Secrets**: Secure credential storage

---

## 📈 Scalability Considerations

- **Concurrent Users**: LiveKit room-based architecture supports multiple sessions
- **Memory Management**: JSON-based conversation storage
- **Stateless Frontend**: Can run behind CDN/load balancer
- **Background Jobs**: Async memory extraction processing

---

## 🎯 Use Cases

1. **Personal Assistant**: Daily scheduling, reminders, information lookup
2. **Customer Service**: Chat and voice support with memory
3. **System Automation**: Voice-controlled system tasks
4. **Information Retrieval**: Web search and weather data
5. **Accessibility**: Voice interface for users with disabilities
6. **Research**: Real-time conversation transcription and analysis

---

## 📝 Notes

- Application is named "Sifra" (Persian origin, likely meaning "wisdom" or "secret")
- Branding: Blue accent color (#0075f2ff light mode, #1fd5f9 dark mode)
- Designed for single or multiple concurrent users
- Full TypeScript type safety throughout
- Responsive design for desktop and mobile
- Modern UI with smooth animations and transitions

---

**Last Updated**: November 26, 2025
