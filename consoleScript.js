Array.from(document.querySelectorAll('[id^="BOOK"]')).forEach((e) => {
  console.log(
    e.querySelector('[id^="lblAtivoNome"]').textContent.match(/\s([^ ]+)$/)[0]
  );
  Array.from(e.querySelectorAll('[id^="tblGridOfertas"]')).forEach((ee) =>
    console.log(ee.querySelector('[class^="onClickBook"] .TD_col3').textContent)
  );
});

fetch("http://127.0.0.1:8000/post/", {
  method: "POST",
  body: JSON.stringify({ eae: "meo" }),
});
