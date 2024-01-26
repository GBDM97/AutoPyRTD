const outputArray = () =>
  Array.from(document.querySelectorAll('[id^="BOOK"]'))
    .map((e) => {
      return {
        strike: e
          .querySelector('[id^="lblAtivoNome"]')
          .textContent.match(/\s([^ ]+)$/)[0]
          .trim(),
        buyPrice: e.querySelector(
          '[id^="tblGridOfertasCompra"] .onClickBook .TD_col3'
        ).textContent,
        sellPrice: e.querySelector(
          '[id^="tblGridOfertasVenda"] .onClickBook .TD_col3'
        ).textContent,
      };
    })
    .sort((a, b) => parseFloat(a.strike) - parseFloat(b.strike));

setInterval(() => {
  fetch("http://127.0.0.1:8000/post/", {
    method: "POST",
    body: JSON.stringify({ optionsData: outputArray() }),
  });
}, 10000);
