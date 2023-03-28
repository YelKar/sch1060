

// file_input.addEventListener("change", load_file)
function load_file(link, name, body) {
    async function g(e) {
        let file = Array.from(this.files).slice(-1)[0];
        const formData = new FormData();
        formData.append(name || "file", file);
        console.log(body)

        for (let [k, v] of Object.entries(body || {})){
            formData.append(k, v);
        }
        await fetch(
            link || document.querySelector("input[type=hidden]#load_file_link").value,
            {
                method: "POST",
                body: formData
            }
        )
        // window.location.reload();
    }
    return g;
}