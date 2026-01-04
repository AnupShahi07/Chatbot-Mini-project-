const input = document.getElementById("message");
const chatBox = document.getElementById("chat-box");

function addMessage(text, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${sender}`;
  messageDiv.textContent = text;

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const userMessage = input.value.trim();
  if (userMessage === "") return;

  addMessage(userMessage, "user");
  input.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    addMessage(data.response, "bot");

  } catch (error) {
    addMessage("Sorry, something went wrong.", "bot");
    console.error(error);
  }
}

// Send message on Enter key
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});
