const apiUrl = "http://127.0.0.1:5000/predict";

const form = document.getElementById("predictionForm");
const resultCard = document.getElementById("resultCard");
const resultText = document.getElementById("resultText");

const getFormData = () => {
  return {
    age: Number(document.getElementById("age").value),
    job: document.getElementById("job").value,
    marital: document.getElementById("marital").value,
    education: document.getElementById("education").value,
    default: document.getElementById("default").value,
    balance: Number(document.getElementById("balance").value),
    housing: document.getElementById("housing").value,
    loan: document.getElementById("loan").value,
    contact: document.getElementById("contact").value,
    day: Number(document.getElementById("day").value),
    month: document.getElementById("month").value,
    duration: Number(document.getElementById("duration").value),
    campaign: Number(document.getElementById("campaign").value),
    pdays: Number(document.getElementById("pdays").value),
    previous: Number(document.getElementById("previous").value),
    poutcome: document.getElementById("poutcome").value
  };
};

const validateFormData = (data) => {
  for (const key in data) {
    if (data[key] === "" || data[key] === null || Number.isNaN(data[key])) {
      return false;
    }
  }
  return true;
};

const setLoadingState = () => {
  resultCard.className = "result-card result-neutral";
  resultText.innerHTML = `
    <div class="result-content">
      <div class="result-main">Processando previsão...</div>
      <div class="result-sub">Aguarde enquanto o modelo analisa os dados do cliente.</div>
    </div>
  `;
};

const setSuccessResult = (prediction, probability = null) => {
  const aderiu = prediction === 1 || prediction === "yes" || prediction === "sim";

  resultCard.className = aderiu
    ? "result-card result-success"
    : "result-card result-danger";

  resultText.innerHTML = `
    <div class="result-content">
      <div class="result-main">
        ${aderiu ? "Cliente com potencial de adesão" : "Cliente com baixa probabilidade de adesão"}
      </div>
      <div class="result-sub">
        Resultado previsto: <strong>${aderiu ? "Sim" : "Não"}</strong>
      </div>
      ${
        probability !== null
          ? `<div class="result-sub">Probabilidade estimada: <strong>${(probability * 100).toFixed(2)}%</strong></div>`
          : ""
      }
    </div>
  `;
};

const setErrorResult = (message) => {
  resultCard.className = "result-card result-danger";
  resultText.innerHTML = `
    <div class="result-content">
      <div class="result-main">Erro ao realizar previsão</div>
      <div class="result-sub">${message}</div>
    </div>
  `;
};

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = getFormData();

  if (!validateFormData(formData)) {
    setErrorResult("Preencha todos os campos corretamente antes de continuar.");
    return;
  }

  try {
    setLoadingState();

    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    });

    if (!response.ok) {
      throw new Error("Não foi possível obter resposta do servidor.");
    }

    const data = await response.json();

    /*
      Esperado do backend, por exemplo:
      {
        "prediction": 1,
        "probability": 0.82
      }
    */

    setSuccessResult(data.prediction, data.probability ?? null);
  } catch (error) {
    console.error("Erro:", error);
    setErrorResult("Verifique se o backend Flask está rodando corretamente.");
  }
});

form.addEventListener("reset", () => {
  setTimeout(() => {
    resultCard.className = "result-card";
    resultText.innerHTML = "Preencha os dados do cliente para visualizar a previsão.";
  }, 50);
});