let submit = document.querySelector(".add-student input.submit")
let block = document.querySelector(".add-student")
let add_student_btn = document.querySelector(".add-student-btn")


add_student_btn.addEventListener(
    "click",
    evt => block.classList.remove("hidden")
)


block.addEventListener("pointerdown", evt => {
    if (evt.target == block) {
        block.classList.add("hidden")
    }
})


submit.addEventListener("click", async function (evt) {
    let res = new FormData();
    for (let field of document.querySelectorAll(
            ".add-student input:not(.submit, .add-student-link)"
            )) {
        res.append(field.name, field.value);
        field.value = "";
    }
    await fetch(
        document.querySelector("input[type=hidden].add-student-link").value,
        {
            method: "POST",
            body: res
        }
    );
    block.classList.add("hidden")
})
