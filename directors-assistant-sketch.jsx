import { useState, useEffect, useRef } from "react";

// ---------------------------------------------------------------
// THROWAWAY SKETCH — Concept 1: "The Director's Assistant"
// Pretend data only. No AI hooked up. This exists so Luca can FEEL
// the concept before Step 4 scoring. The real V1 gets built by Luca.
// ---------------------------------------------------------------

const SAMPLE_PLAN = {
  title: "Lego Stop-Motion Movie",
  steps: [
    {
      emoji: "🧱",
      title: "Build your set",
      say: "First, build your set! Make the place where your story happens. You have ten minutes — build fast like a movie crew!",
      roles: null,
      then: null,
    },
    {
      emoji: "🤖",
      title: "Place your character",
      say: "Now place your character at the start of the story. Where does your hero begin?",
      roles: null,
      then: null,
    },
    {
      emoji: "🎥",
      title: "Move… and snap!",
      say: "Animator: move the character a tiny bit. Camera operator: press the button. Move, snap, move, snap! Switch jobs every five snaps.",
      roles: ["🧍 Animator", "📸 Camera operator"],
      then: null,
    },
    {
      emoji: "🍿",
      title: "Watch your movie",
      say: "Time to watch your movie! You made that! Every single picture was your work.",
      roles: null,
      then: null,
    },
    {
      emoji: "🎉",
      title: "Free Lego time!",
      say: "You finished like real filmmakers. Now — free Lego play time. You earned it!",
      roles: null,
      then: "reward",
    },
  ],
};

function speak(text) {
  if (!("speechSynthesis" in window)) return;
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.rate = 0.95;
  u.pitch = 1.1;
  window.speechSynthesis.speak(u);
}

export default function DirectorsAssistant() {
  const [screen, setScreen] = useState("staff"); // staff | making | kids
  const [current, setCurrent] = useState(0);
  const [projectText, setProjectText] = useState(
    "Stop-motion with Legos, 4 kids, 45 minutes"
  );
  const plan = SAMPLE_PLAN;
  const step = plan.steps[current];
  const timerRef = useRef(null);

  useEffect(() => {
    return () => {
      window.speechSynthesis && window.speechSynthesis.cancel();
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, []);

  const startMaking = () => {
    setScreen("making");
    timerRef.current = setTimeout(() => {
      setScreen("kids");
      setCurrent(0);
      speak(plan.steps[0].say);
    }, 1800);
  };

  const goTo = (i) => {
    setCurrent(i);
    speak(plan.steps[i].say);
  };

  // ------------------------- STAFF SCREEN -------------------------
  if (screen === "staff") {
    return (
      <div style={sx.shell}>
        <style>{fontCss}</style>
        <div style={sx.staffCard}>
          <div style={sx.clapTop}>
            {[...Array(7)].map((_, i) => (
              <div
                key={i}
                style={{
                  ...sx.clapStripe,
                  background: i % 2 ? "#FFD23F" : "#1B2A4A",
                }}
              />
            ))}
          </div>
          <div style={{ padding: "34px 34px 38px" }}>
            <div style={sx.eyebrow}>STAFF SIDE · sketch, not the real build</div>
            <h1 style={sx.staffTitle}>What are we making today?</h1>
            <textarea
              value={projectText}
              onChange={(e) => setProjectText(e.target.value)}
              rows={3}
              style={sx.input}
            />
            <button style={sx.bigButton} onClick={startMaking}>
              🎬 Make the plan
            </button>
            <p style={sx.footnote}>
              In the real V1, Claude reads this sentence and generates the step
              cards. In this sketch, a pretend Lego plan appears.
            </p>
          </div>
        </div>
      </div>
    );
  }

  // ------------------------- MAKING SCREEN -------------------------
  if (screen === "making") {
    return (
      <div style={sx.shell}>
        <style>{fontCss}</style>
        <div style={sx.makingWrap}>
          <div style={sx.spinner}>🎬</div>
          <div style={sx.makingText}>Your director is thinking…</div>
        </div>
      </div>
    );
  }

  // ------------------------- KID SCREEN -------------------------
  const isReward = step.then === "reward";
  return (
    <div style={sx.shell}>
      <style>{fontCss}</style>
      <div style={sx.kidWrap}>
        {/* Film-strip progress */}
        <div style={sx.filmStrip}>
          {plan.steps.map((s, i) => (
            <button
              key={i}
              onClick={() => goTo(i)}
              style={{
                ...sx.frame,
                background:
                  i === current ? "#FF5A5F" : i < current ? "#3EC97E" : "#243B63",
                transform: i === current ? "scale(1.12)" : "scale(1)",
              }}
              aria-label={"Step " + (i + 1) + ": " + s.title}
            >
              <span style={{ fontSize: 26 }}>{i < current ? "✓" : s.emoji}</span>
            </button>
          ))}
        </div>

        {/* Big current-step card */}
        <div
          style={{
            ...sx.stepCard,
            background: isReward ? "#FFD23F" : "#FFF8EC",
          }}
        >
          <div style={sx.stepEyebrow}>
            {isReward ? "THEN — YOU EARNED IT" : `STEP ${current + 1} OF ${plan.steps.length}`}
          </div>
          <div style={sx.stepEmoji}>{step.emoji}</div>
          <div style={sx.stepTitle}>{step.title}</div>

          {step.roles && (
            <div style={sx.rolesRow}>
              {step.roles.map((r) => (
                <div key={r} style={sx.roleChip}>
                  {r}
                </div>
              ))}
              <div style={sx.roleSwap}>🔄 switch every 5 snaps</div>
            </div>
          )}

          <button style={sx.hearButton} onClick={() => speak(step.say)}>
            🔊 Hear it
          </button>
        </div>

        {/* Nav */}
        <div style={sx.navRow}>
          <button
            style={{ ...sx.navButton, opacity: current === 0 ? 0.35 : 1 }}
            disabled={current === 0}
            onClick={() => goTo(current - 1)}
          >
            ← Back
          </button>
          {current < plan.steps.length - 1 ? (
            <button style={{ ...sx.navButton, ...sx.navNext }} onClick={() => goTo(current + 1)}>
              We did it! Next →
            </button>
          ) : (
            <button style={{ ...sx.navButton, ...sx.navNext }} onClick={() => setScreen("staff")}>
              🎬 New project
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

const fontCss = `
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Nunito:wght@600;800&display=swap');
* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
@keyframes wobble { 0%,100%{transform:rotate(-8deg)} 50%{transform:rotate(8deg)} }
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
`;

const sx = {
  shell: {
    minHeight: "100vh",
    background: "#1B2A4A",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: 18,
    fontFamily: "'Nunito', sans-serif",
  },
  // staff
  staffCard: {
    width: "100%",
    maxWidth: 560,
    background: "#FFF8EC",
    borderRadius: 24,
    overflow: "hidden",
    boxShadow: "0 24px 60px rgba(0,0,0,.45)",
  },
  clapTop: { display: "flex", height: 26 },
  clapStripe: { flex: 1, transform: "skewX(-20deg) scaleX(1.2)" },
  eyebrow: {
    fontSize: 12,
    fontWeight: 800,
    letterSpacing: "0.12em",
    color: "#FF5A5F",
    marginBottom: 10,
  },
  staffTitle: {
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 34,
    lineHeight: 1.1,
    color: "#1B2A4A",
    margin: "0 0 18px",
  },
  input: {
    width: "100%",
    fontSize: 19,
    fontFamily: "'Nunito', sans-serif",
    fontWeight: 600,
    padding: 16,
    borderRadius: 14,
    border: "3px solid #1B2A4A",
    background: "#fff",
    color: "#1B2A4A",
    resize: "none",
  },
  bigButton: {
    marginTop: 18,
    width: "100%",
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 24,
    fontWeight: 800,
    padding: "18px 20px",
    borderRadius: 16,
    border: "none",
    background: "#FF5A5F",
    color: "#fff",
    cursor: "pointer",
    boxShadow: "0 6px 0 #C23A3F",
  },
  footnote: { marginTop: 16, fontSize: 13, color: "#6B7A99", lineHeight: 1.5 },
  // making
  makingWrap: { textAlign: "center", color: "#FFF8EC" },
  spinner: { fontSize: 84, animation: "wobble 0.9s ease-in-out infinite" },
  makingText: {
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 28,
    marginTop: 14,
  },
  // kid screen
  kidWrap: { width: "100%", maxWidth: 640 },
  filmStrip: {
    display: "flex",
    gap: 10,
    justifyContent: "center",
    marginBottom: 20,
  },
  frame: {
    width: 58,
    height: 58,
    borderRadius: 14,
    border: "3px solid #FFF8EC",
    cursor: "pointer",
    transition: "transform .15s ease",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  stepCard: {
    borderRadius: 28,
    padding: "30px 26px 34px",
    textAlign: "center",
    boxShadow: "0 24px 60px rgba(0,0,0,.45)",
  },
  stepEyebrow: {
    fontSize: 13,
    fontWeight: 800,
    letterSpacing: "0.14em",
    color: "#FF5A5F",
  },
  stepEmoji: { fontSize: 110, lineHeight: 1.15, margin: "6px 0" },
  stepTitle: {
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 44,
    lineHeight: 1.05,
    color: "#1B2A4A",
  },
  rolesRow: {
    display: "flex",
    gap: 10,
    justifyContent: "center",
    flexWrap: "wrap",
    marginTop: 16,
  },
  roleChip: {
    background: "#1B2A4A",
    color: "#FFF8EC",
    fontWeight: 800,
    fontSize: 17,
    padding: "10px 16px",
    borderRadius: 999,
  },
  roleSwap: {
    background: "#FFD23F",
    color: "#1B2A4A",
    fontWeight: 800,
    fontSize: 15,
    padding: "10px 14px",
    borderRadius: 999,
  },
  hearButton: {
    marginTop: 22,
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 26,
    fontWeight: 800,
    padding: "16px 34px",
    borderRadius: 999,
    border: "none",
    background: "#3EC97E",
    color: "#fff",
    cursor: "pointer",
    boxShadow: "0 6px 0 #2A9159",
  },
  navRow: { display: "flex", gap: 12, marginTop: 20 },
  navButton: {
    flex: 1,
    fontFamily: "'Baloo 2', sans-serif",
    fontSize: 21,
    fontWeight: 800,
    padding: "16px 10px",
    borderRadius: 16,
    border: "3px solid #FFF8EC",
    background: "transparent",
    color: "#FFF8EC",
    cursor: "pointer",
  },
  navNext: {
    background: "#FF5A5F",
    border: "3px solid #FF5A5F",
  },
};
