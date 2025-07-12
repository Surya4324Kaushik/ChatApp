document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("message-input");
  input.addEventListener("keyup", e => {
    if (e.key === "Enter") {
      document.getElementById("send-btn").click();
    }
  });
});