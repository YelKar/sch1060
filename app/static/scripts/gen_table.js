async function generate_table() {
    let students = document.querySelectorAll("input:checked.student_checkbox");
    let ids = Array.from(students).map(val => val.id.slice(1) - 0);
    if (!ids.length) {
        return;
    }
    let url = document.querySelector("input[type=hidden].gen_url").value
    let res = await fetch(
        url,
        {
            method: "POST",
            body: JSON.stringify({
                ids: ids
            })
        }
    );
    let downloadURL = await res.text();
    goto(downloadURL, true);
}