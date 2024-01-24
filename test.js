Array.from(
    document.querySelectorAll('[id^="BOOK"]')
)
.forEach(
        e => 
            Array.from(
                e.querySelectorAll('[id^="tblGridOfertas"]')
            ).forEach(
                ee => console.log(
                    ee.querySelector(
                    '[class^="onClickBook"] .TD_col3'
                    ).textContent
                )
            )
)