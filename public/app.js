const form = document.getElementById("genForm");
const statusEl = document.getElementById("status");
const resultEl = document.getElementById("result");
const outputImg = document.getElementById("output");
const submitBtn = form.querySelector("button");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  submitBtn.disabled = true;
  submitBtn.textContent = "Generating...";
  resultEl.classList.add("hidden");
  statusEl.textContent = "Starting generation...";

  const payload = {
    prompt: document.getElementById("prompt").value.trim(),
    negative: document.getElementById("negative").value.trim(),
    model: document.getElementById("model").value,
    steps: parseInt(document.getElementById("steps").value, 10),
    cfg: parseFloat(document.getElementById("cfg").value),
  };

  try {
    const res = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();

    if (!res.ok) {
      const msg = typeof data.error === "string"
        ? data.error
        : data.error?.message || JSON.stringify(data.error);
      throw new Error(msg);
    }

    statusEl.textContent = "Done!";
    outputImg.src = data.imageUrl;
    resultEl.classList.remove("hidden");
  } catch (err) {
    statusEl.textContent = `Error: ${err.message}`;
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Generate";
  }
});
