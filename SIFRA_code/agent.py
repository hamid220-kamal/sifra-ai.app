from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, ChatContext, ChatMessage
from livekit.plugins import google, noise_cancellation

# Import your custom modules
from SIFRA_prompts import instructions_prompt, Reply_prompts,Hamid_SIFRA_Daily_Protocol, SIFRA_Ultimate_Prompt
from memory_loop import MemoryExtractor
from SIFRA_reasoning import thinking_capability
from memory_store import MemoryStore
load_dotenv()

REPLY_TIMEOUT = 30  # Increase timeout to 30 seconds

class Assistant(Agent):
    def __init__(self, chat_ctx) -> None:
        super().__init__(chat_ctx = chat_ctx,
                        instructions=instructions_prompt,
                        llm=google.beta.realtime.RealtimeModel(voice="kore"),
                        tools=[thinking_capability]
                                )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        preemptive_generation=True
    )
    
    #getting the current memory chat
    current_ctx = session.history.items
    

    await session.start(
        room=ctx.room,
        agent=Assistant(chat_ctx=current_ctx), #sending currenet chat to llm in realtime
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )
    await session.generate_reply(
        instructions=Reply_prompts
    )
    conv_ctx = MemoryExtractor()
    await conv_ctx.run(current_ctx)
    


async def initialize_agent():
    config = {
        "timeout": REPLY_TIMEOUT,
        "user_id": "Hamid_22"
    }
    # ...existing code...


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

