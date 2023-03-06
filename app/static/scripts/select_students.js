function send_students(type) {
    let students = document.querySelectorAll("input:checked.student_checkbox");
    let ids = Array.from(students).map(val => val.id.slice(1) - 0);
    if (!ids.length) {
        return;
    }
    let url = document.querySelector("input.gen_url").value
    let res = fetch(
        url,
        {
            method: "POST",
            body: ids.toString()
        }
    )
}