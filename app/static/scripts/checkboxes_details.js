const details_all = document.querySelectorAll(" details.student_selector") //

function all_checked(list) {
    for (let el of list) {
        if (!el.checked) return false
    }
    return true
}

for (let det of details_all) {
    let summary_input = det.querySelector("summary input");
    summary_input.addEventListener("change", (e) => {
        for (let input of det.querySelectorAll("input")) {
            input.checked = det.querySelector("summary input").checked;
        }
    })

    det.addEventListener("click", (e) => {
        if (e.target != summary_input
            && all_checked(det.querySelectorAll("input")) != summary_input.checked) {
            summary_input.checked = all_checked(det.querySelectorAll("input"));
        }
    })
}

document.querySelector("input[type=button].select_all").addEventListener(
    "click", e => {
        change_all();
    }
)

function change_all() {
    let checkboxes = document.querySelectorAll("input[type=checkbox]");
    let flag = all_checked(checkboxes);
    for (let el of checkboxes) {
        el.checked = !flag;
    }
}