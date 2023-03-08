async function send_students(type) {
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


function goto(url, download=false) {
    let linkElement = document.createElement("a")
    if (download) {
        linkElement.download = download;
    }
    linkElement.href = url;
    linkElement.click()
}
