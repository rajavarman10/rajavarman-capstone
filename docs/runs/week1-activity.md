# Week 1 Activity — System Prompt Voice Exploration

## Prompt A — "You are concise."

Quantum entanglement is a phenomenon where two or more particles become linked in such a way that the state of one particle instantaneously influences the state of the other, regardless of the distance separating them. This interconnectedness defies classical intuitions about separability and locality, challenging our understanding of space and information transfer in quantum mechanics.

## Prompt B — "You are a kindergarten teacher. Explain like the listener is five years old."

Quantum entanglement is a phenomenon where two or more particles become interconnected in such a way that the state of one particle instantaneously influences the state of the other, regardless of the distance separating them. This non-local connection challenges classical intuitions about separateness and locality in physics, leading to intriguing implications for quantum mechanics and information processing.

## Prompt C — "You are a Shakespearean poet. Reply in iambic verse where possible."

Quantum entanglement is a phenomenon where two or more particles become interlinked, such that the state of one particle instantaneously influences the state of the other, regardless of the distance separating them. This non-local correlation challenges classical intuitions about separability and locality, leading to implications for quantum computing and information theory.

## Prompt D — "You are a brilliant but impatient physicist. You explain accurately but you don't have time for niceties."

Quantum entanglement is a phenomenon where two or more particles become linked such that the state of one particle instantly influences the state of the other, regardless of the distance separating them. This connection defies classical intuitions about locality and separability, leading to implications for quantum computing and information theory.

## What changed?

The core physics content stayed essentially identical across all four answers — the description of entanglement, the mention of non-locality, and the length (two sentences) barely varied. What I expected to change the most — voice and tone (kindergarten-simple, Shakespearean verse, grumpy-terse) — actually shifted only slightly here; none of the personas (teacher, poet, physicist) came through strongly in wording or style. This is likely because `temperature` in this script is set low (0.3), which pushes the model toward its most "safe"/literal completion and suppresses stylistic risk-taking even when the system prompt asks for it — so the system prompt still steers behavior, but its effect is dampened at low temperature. In a real product, I'd reach for a system-prompt change (and likely a higher temperature) instead of fine-tuning whenever I need to adjust tone, audience, or persona without touching the underlying facts — it's near-zero cost and takes effect immediately, versus fine-tuning which costs real time and money.
