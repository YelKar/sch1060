async function send_students(type) {
    let ids = get_selected();
    if (!ids.length) {
        return;
    }
    let url = document.querySelector("input[type=hidden].gen_url").value
    let res = await fetch(
        url,
        {
            method: "POST",
            body: JSON.stringify({
                ids: ids,
                document: document.querySelector("input[type=hidden].document_for_gen").value,
                type: type
            })
        }
    );
    let downloadURL = await res.text();
    if (downloadURL == "Error") {
        return;
    }
    goto(downloadURL, true);
}


function get_selected() {
    let students = document.querySelectorAll("input:checked.student_checkbox");
    return Array.from(students).map(val => val.id.slice(1) - 0);
}
